#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#define FOR(i,j,k) for(int i=j;i<=k;i++)
using namespace std;
int main (int argc, char *argv[])
{
	std::ios::sync_with_stdio(false);
	int noc;cin>>noc;
	FOR(cs,1,noc){
		string s;
		cin>>s;
		int n=s.size();
		int ans=0;
		for(int i=n-1;i>=0;i--){
			if (s[i]=='+')	continue;
			else{
				if (s[0]=='-'){
					ans++;
				}else{
					ans+=2;
					FOR(j,0,i){
						if (s[j]=='+')	s[j]='-';
						else break;
					}
				}
				string temp;
				FOR(j,0,i)	temp+=s[j];
				FOR(j,0,i){
					s[i-j]=temp[j]=='+'?'-':'+';
				}

			}
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}
