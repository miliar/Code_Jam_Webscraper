#include<iostream>
using namespace std;
#include<algorithm>
const int maxn=1000+10;
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int t; cin>>t;
	int k=1;
	while(t--){
		int n; cin>>n;
		int a[maxn];
		int ma=0;
		for(int i=0;i<n;i++) { cin>>a[i]; ma=max(ma,a[i]); }
		int mi=ma;
		for(int i=1;i<=ma;i++){
			int tmp_mi=i;
			for(int j=0;j<n;j++){
				if(a[j]>i){
					tmp_mi+=(a[j]+i-1)/i-1;
				}
			}
			mi=min(mi,tmp_mi);
		}
		cout<<"Case #"<<k++<<": "<<mi<<endl;
	}
	return 0;
}
