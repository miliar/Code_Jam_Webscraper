#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
//#include <unordered_map>

using namespace std;
int A[27];

int main(){
	ofstream out;
	out.open("1b.out");
	ifstream in;
	in.open("1b.in");
	int t;
	in>>t;
	for(int r=1;r<=t;r++){
		int n,tot=0,tote=0,tmp,mx1=0,mx2=0,in1=0,in2=0,i,j;
		in>>n;
		memset(A,0,sizeof A);
		for(i=1;i<=n;i++){
			in>>tmp;
			A[i]+=tmp;
			tot+=tmp;
			tote+=tmp;
		}
		//tote=tot;
		//cout<<tote;
		out<<"Case #"<<r<<": ";
		if(tote%2)
			tote+=1;
		for(i=0;i<tote/2;i++){
			mx1=0;mx2=0;in1=0;in2=0;
			for(j=1;j<27;j++){
			if(A[j]>mx2)
				{
					if(A[j]>mx1){
						mx2=mx1;
						in2=in1;
						mx1=A[j];
						in1=j;
					}
					else{
						mx2=A[j];
						in2=j;
					}
				}
			//cout<<A[j]<<" ";
			}
			if(A[in1]==A[in2]){
				
				//cout<<"hell1";
				if((tot-2)!=1){
					out<<(char)('A'+in1-1)<<(char)('A'+in2-1);
					A[in1]--;A[in2]--;
					tot-=2;
				}
				else
				{
					out<<(char)('A'+in1-1);
					A[in1]--;tot-=1;
				}
					//mx2--;mx1--;
			}
			else{
				out<<(char)('A'+in1-1)<<(char)('A'+in1-1);
				//cout<<"hell2";
				A[in1]--;A[in1]--;
				tot-=2;
				//mx1-=2;
			}
			out<<" ";
		}
		out<<"\n";
	}
}
