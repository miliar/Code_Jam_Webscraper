#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#define forn(i, n) for(int i=0; i<n; i++)
#define for1(i, n) for(int i=1; i<=n; i++)
#define N 200
using namespace std;
int main(){
	int t, c, d, v, sum=0, ans=0, den[N], a[N];
	cin>>t;
	forn(i, t){
		cin>>c>>d>>v; sum=ans=0;
		forn(j, d)cin>>den[j]; den[d]=0; den[d+1]=v+1; d+=2;
		sort(den, den+d);
		for1(j, d-1){
			//sum+=den[j];
			//cout<<sum<<"-"<<den[j]<<" ";
			if(sum>=v)break;
			if(sum<den[j]-1){
				while(sum<den[j]-1 && sum<v)ans++, sum=sum*2+1;
			}
			sum=sum+den[j];
		}
		//cout<<endl;
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
		
	return 0;
}
