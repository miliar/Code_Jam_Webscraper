#include <bits/stdc++.h>
using namespace std;
map<string,bool>M;
int main(){
	int test;
	cin>>test;
	int n,m,c=0;
	cin>>n>>m;
	cout<<"Case #1:"<<endl;
	while(c<m){
		string s="1";
		for(int i=0;i<n-2;i++)
			if(rand()%2)s+="0";
			else s+="1";
		s+="1";
		if(M.count(s)>0)continue;
		M[s]=1;
		vector<int>A(9,-1);
		for(int b=2;b<=10;b++){
			for(int mul=2;mul<100;mul++){
				int x=0,p=1;
				for(int i=n-1;i>=0;i--){
					if(s[i]=='1')
						x=(x+p)%mul;
					p=(p*b)%mul;
				}
				if(x==0){
					A[b-2]=mul;
					break;
				}
			}
		}
		bool sw=1;
		for(int i=0;i<9;i++)if(A[i]==-1){sw=0;break;}
		if(sw){
			cout<<s<<" ";
			for(int i=0;i<8;i++)cout<<A[i]<<" ";
			cout<<A[8]<<endl;
			c++;
		}
	}
	return 0;
}
