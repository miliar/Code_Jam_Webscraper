#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int t,i,j,tc,n,cnt1,cnt2;
double ken[10001],naomi[10001],cken[10001],cnaomi[10001];

int main()
{
	freopen("D:\\input.txt","r",stdin);
	freopen("D:\\output.txt","w",stdout);
	cin>>tc;
	for(t=1;t<=tc;t++){
		cnt1=0; cnt2=0;
		cin>>n;
		for(i=0;i<n;i++) cin>>naomi[i];
		for(i=0;i<n;i++) cin>>ken[i];
		
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		
		for(i=0;i<n;i++) cnaomi[i]=ken[i];
		for(i=0;i<n;i++) cken[i]=naomi[i];
		
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(cnaomi[j]>cken[i]){
					cnaomi[j]=-1;
					cnt2++;
					break;
				}
			}
		}
		
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(naomi[j]>ken[i]){
					naomi[j]=-1;
					cnt1++;
					break;
				}
			}
		}
	
		cout<<"Case #"<<t<<": "<<cnt1<<" "<<n-cnt2<<endl;
	}
	return 0;
}

