#include<bits/stdc++.h>
using namespace std;
 
#define rep(i,n) for(i=0;i<n;i++)
#define ll long long
#define elif else if
#define ff first
#define ss second
#define pii pair<ll int,ll int>
#define mp make_pair
#define pb push_back
#define CLEAR(array, value) memset(ptr, value, sizeof(array));
#define si(a)     scanf("%d", &a)
#define sl(a)     scanf("%lld", &a)
#define pi(a)     printf("%d", a)
#define pl(a)     printf("%lld", a)
#define pn        printf("\n")
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("outputAsmall.in","w",stdout);
	char a[]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
   vector<pair <int, char> >v;
	int n,m,g;
	cin>>n;
	for(int i=1;i<=n;i++)
	{ int t=0;
	
		cin>>m;
		for(int j=1;j<=m;j++){
		int x;
		cin>>x;
		t=t+x;
		v.push_back(make_pair(x,a[j-1]));
	}
	cout<<"Case #"<<i<<": ";
		sort(v.rbegin(),v.rend());
		g=v[0].first;
		for(int j2=0;j2<g;j2++){
			if(v[0].first>v[1].first)
			{
				cout<<v[0].second<<" ";
				v[0].first=v[0].first-1;
				
			}else{
				int c=1;
				for(int k=0;k<m;k++){
					if(v[k].first==v[k+1].first){
						c++;
					}else{
						break;
					}
				}
				if(c%2==0){
					int z=c-1;
					for(int k1=0;k1<c/2;k1++){
						cout<<v[z].second<<v[z-1].second<<" ";
						v[z].first=v[z].first-1;
						v[z-1].first=v[z-1].first-1;
						z=z-2;
					}
					
				}else{
					int z1=c-1;
					cout<<v[z1].second<<" ";
					v[z1].first=v[z1].first-1;
					z1=z1-1;
					for(int k2=0;k2<c/2;k2++){
						cout<<v[z1].second<<v[z1-1].second<<" ";
					    v[z1].first=v[z1].first-1;
						v[z1-1].first=v[z1-1].first-1;
					}
					
				}
				
			}
			
		}
		
	cout<<endl;
	v.clear();
	}
	

	return 0;
}
