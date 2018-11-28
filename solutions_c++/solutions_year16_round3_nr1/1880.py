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
int arr[MAXN];
int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		int a,sum=0;
		scanf("%d",&a);
		for(int i=1;i<=a;i++)
			scanf("%d",arr+i),sum+=arr[i];
		printf("Case #%d: ",test);
		while(sum>=1){
			int mx=0,pos=-1;
			int pos1=-1,mx1=0;
			for(int i=1;i<=a;i++)
				if(umax(mx,arr[i]))
					pos=i;
			for(int i=1;i<=a;i++)
				if(i!=pos and umax(mx1,arr[i]))
					pos1=i;		
			if(mx){
				if(sum-2!=1 and mx==mx1){
					arr[pos]--;
					sum-=2;
					arr[pos1]--;
					cout<<char(pos+64)<<char(pos1+64)<<" ";
				}
				else{
					arr[pos]--;
					sum--;
					cout<<char(pos+64)<<" ";
				}
			}
		}	
		cout<<endl;
	}
	return 0;
}
//LooK aT mY COde ONlinE +_+

