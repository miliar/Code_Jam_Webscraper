#include<bits/stdc++.h>
#define MAXN 100009
#define INF 1000000007
#define imx 2147483647
#define LLINF 1000000000000000007
#define mp(x,y) make_pair(x,y)
#define wr cout<<"Continue Debugging!!!"<<endl;
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
#define ppb() pop_back()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
using namespace std;
typedef long long ll;
typedef pair<int,int>PII;
template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
int arr[28],ans[23];
int pp[]={0,6,8,2,3,4,5,9,7,1};
//int pp[]={0,1,2,3,4,5,6,7,8,9};
string cnt[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<int>adj[24];
int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	for(int i=0;i<10;i++)
		for(int j=0;j<cnt[i].size();j++)
			adj[i].pb(1);
	adj[3][3]=adj[3][4]=adj[7][1]=adj[7][3]=adj[9][0]=adj[9][2]=2;		
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		fill(arr,arr+27,0);
		fill(ans,ans+22,0);
		string s;
		cin>>s;
		for(int i=0;i<s.size();i++)
			arr[s[i]-'A'+1]++;
		for(int i=0;i<10;i++){
			int mn=INF,d=1;
			int pos=pp[i];
			for(int j=0;j<cnt[pos].size();j++){
				if(arr[cnt[pos][j]-'A'+1]==0){
					d=0;
					break;
				}
				umin(mn,arr[cnt[pos][j]-'A'+1]/adj[pos][j]);
			}	
			if(mn<INF and d){	
				for(int j=0;j<cnt[pos].size();j++)
					arr[cnt[pos][j]-'A'+1]-=mn;
				ans[pos]=mn;	
			}
		}
		//for(int i=1;i<=26;i++)
		//	assert(arr[i]==0);
		printf("Case #%d: ",test);
		for(int i=0;i<10;i++)
			for(int j=1;j<=ans[i];j++)
				cout<<i;
		cout<<endl;		
	}
	return 0;
}
//LooK aT mY COde ONlinE +_+

