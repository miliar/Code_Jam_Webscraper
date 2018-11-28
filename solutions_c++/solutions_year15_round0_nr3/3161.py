#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

int mat[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int arr1[10001],arr2[10001];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,cs=0;cin>>t;
	while(t--){
		int l,x;cin>>l>>x;
		int n=l*x;
		string z,s;cin>>z;
		while(x--)s+=z;

		arr1[0]=s[0]-'i'+2;
		for(int i=1;i<n;++i){
			if(arr1[i-1]<0)arr1[i]=-mat[-arr1[i-1]][s[i]-'i'+2];
			else if(arr1[i-1]>0)arr1[i]=mat[arr1[i-1]][s[i]-'i'+2];
		}

		for(int i=0;i<n;++i){
			arr2[i]=s[i]-'i'+2;
			for(int j=i+1;j<n;++j){
				if(arr2[i]>0)arr2[i]=mat[arr2[i]][s[j]-'i'+2];
				else if(arr2[i]<0)arr2[i]=-mat[-arr2[i]][s[j]-'i'+2];
			}
		}

		bool check=0;

		for(int i=1;i<n && !check;++i){
			if(arr1[i-1]!=2)continue;
			int res=0,pos=i;
			for(int j=i+1;j<n;++j){
				if(pos==i)res=s[i]-'i'+2;
				else{
					if(res>0)res=mat[res][s[pos]-'i'+2];
					else res=-mat[-res][s[pos]-'i'+2];
				}
				++pos;
				if(res==3 && arr2[j]==4){check=1;break;}
			}
		}
		cout<<"Case #"<<++cs<<": ";
		if(check)cout<<"YES\n";
		else cout<<"NO\n";
	}
	return 0;
}
