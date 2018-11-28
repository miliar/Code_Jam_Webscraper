#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<cmath>
#include<cassert>
 
using namespace std;
 
#define mod 1000000007
#define X first
#define Y second
#define pb push_back
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define all(c) c.begin(),c.end()
#define MAXN 100010
#define INF 1000000000
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> pii;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("op.txt","w",stdout);
	int t,cno=1;
	cin>>t;
	while(t--){
		int Smax,sum=0,ans=0;
		string S;
		cin>>Smax>>S;
		for(int i=0;i<=Smax;i++){
			if(sum<i && S[i]!='0'){
				ans=ans+i-sum;
				sum=i+S[i]-'0';
			}
			else sum=sum+S[i]-'0';
		}
		cout<<"Case #"<<cno++<<": "<<ans<<"\n";
	}
	return 0;
	
}
