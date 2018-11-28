#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

string sol(int a, int b, string ss)
{
	if(ss.size()==1) return "NO";
	bool first=false;
	bool second=false;
	char res='1';
	int sign=1;
	for(int j=0;j<b;j++){
		for(int i=0;i<a;i++){
			switch (res) {
				case '1':
				if(ss[i]=='1') res='1';
				if(ss[i]=='i') {
					res='i';
					first = true;
				}
				if(ss[i]=='j') res='j';
				if(ss[i]=='k') {
					res='k';
					if(first) second=true;
				}
				break;
				case 'i':
				if(ss[i]=='1') 
				{
					res='i';
					first=true;
				}
				if(ss[i]=='i') {
					res='1';
					sign=-sign;
				}
				if(ss[i]=='j') {
					res='k';
					if(first) second=true;
				}
				if(ss[i]=='k') 
				{
					res='j';
					sign=-sign;
				}
				break;
				case 'j':
				if(ss[i]=='1') res='j';
				if(ss[i]=='i') {
					res='k';
					sign=-sign;
					if(first) second=true;
					}
				if(ss[i]=='j') 
				{
					res='1';
					sign=-sign;
				}
				if(ss[i]=='k') {
					res='i';
					first = true;
				}
				break;
				case 'k':
				if(ss[i]=='1') {
					res='k';
					if(first) second=true;
				}
				if(ss[i]=='i') res='j';
				if(ss[i]=='j') {
					res='i';
					sign=-sign;
					first=true;
				}
				if(ss[i]=='k') {
					res='1';
					sign=-sign;
				
			   }
			   break;	
				default:
					break;
			}
		}
	}
	if((res-'0')*sign==-1 && first && second) return "YES";
	else return "NO";
}

int main(){
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("C-small-attempt0.out.txt","w",stdout);
	int tt;
	cin>>tt;
	int aa,bb;
	string ss;
	for(int qq=1;qq<=tt;qq++){
		cout<<"Case #"<<qq<<": ";
		cin>>aa>>bb>>ss;
		cout<<sol(aa,bb,ss)<<endl;
	}
	return 0;
}

