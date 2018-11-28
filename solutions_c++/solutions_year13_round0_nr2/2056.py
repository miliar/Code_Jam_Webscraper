#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cmath>
#include <sstream>
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int y10=0;y10<m;y10++)
#define repv(i,n,m) for(int y11=n;y11>0;y11++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define stringstream ss

#define NMAX 110
typedef long long int ll;

using namespace std;

int main(){ int z,o,j,i,n,m,k; int s[NMAX][NMAX],sol; bool flag=true; bool flag1=true;  bool all;
cin>>z;
for (o=0;o<z;o++){ 
	cin>>n>>m; all=true;
	for(i=0;i<n;i++)for(j=0;j<m;j++){cin>>s[i][j];}
	for(i=0;i<n;i++)for(j=0;j<m;j++){ flag=flag1=true;
			for(k=0;k<n;k++){ if(s[i][j]<s[k][j]) flag=false;}
			for(k=0;k<m;k++){ if(s[i][j]<s[i][k]) flag1=false;}
			if(!flag&&!flag1) all=false;
			}
	cout<<"Case #"<<o+1<<": ";
	if (all)cout<<"YES";else cout<<"NO"; cout<<"\n";
}
return 0;}

		
