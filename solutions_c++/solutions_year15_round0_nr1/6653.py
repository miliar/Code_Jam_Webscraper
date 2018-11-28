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

using namespace std;

int main(){
	freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tt;
	cin>>tt;
	int a,count,res;
	string s;
	for(int qq=1;qq<=tt;qq++){
		cout<<"Case #"<<qq<<": ";
		cin>>a;
		cin>>s;
		count=s[0]-'0';
		res=0;
		if(a==0){
			cout<<res<<endl;
			continue; 
		};
		for(int i=1;i<=a;i++){
			if(s[i]=='0') continue;
		    if(count<i){
			    res+=i-count;
				count+=res;			    
			 }
			count+=s[i]-'0';
		}
		cout<<res<<endl;
	}
	return 0;
}

