#include<bits/stdc++.h>
using namespace std;
typedef	long long ll;
typedef unsigned long long ULL;
#define all(v) ((v).begin()),((v).end())
#define sz(v) ((int)((v).size()))
#define PI(n) ((double)acos(n))
#define pw2(n) (1LL<<(n))
int dx8[8] = { 1, -1, 0, 0, 1, 1, -1, -1 };
int dy8[8] = { 0, 0, 1, -1, 1, -1, 1, -1 };
void file()
{
    #ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    //freopen(fo, "w", stdout);
    #else
    // online submission
    #endif
}
void fast()
{
std::ios_base::sync_with_stdio(0);
cin.tie(NULL); cout.tie(NULL);
}
inline bool find(long long n,int  vis[]){
	while(n!=0){
		if(n==0) break;
		vis[n%10]=1;
		n/=10;
	}
	for(int i=0;i<10;i++)
		if(vis[i]==0)
    	return 0;
	return 1;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long n;
		int vis[11];
		for(int ii=0;ii<10;ii++)
		  vis[ii]=0;
		cin>>n;
		printf("Case #%d: ",i);
		if(n==0) {
			printf("INSOMNIA");
			if(i!=t) cout<<endl;
			continue;
		}
		int j=1;
		while(1){
			if(find(n*j,vis)) break;
			 j++;
		}
		printf("%lld",j*n);
		if(i!=t) printf("\n");
	}
	
	
	
	
	
	
	
	
	
}
