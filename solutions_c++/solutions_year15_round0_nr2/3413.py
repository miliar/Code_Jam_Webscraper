#include<stdio.h>
#include<algorithm>
#define ll long long
using namespace std;

bool func(ll i, ll j){
	return i>j;
}

ll getans(ll arr[],ll n){
	///printf("f");
	/*for(ll lv=0;lv<n;lv++){
		printf("%lld ",arr[lv]);
	}
	printf("\n");*/
	if(arr[0]==1){
		return 1;
	}
	if(arr[0]==2){
		return 2;
	}
	if(arr[0]==3){
		return 3;
	}
	if(arr[0]==4){
		return 3;
	}
	ll arr1[n+1],arr2[n];
	ll arr2size=0;
	for(ll lv=0;lv<n;lv++){
		arr1[lv]=arr[lv];
		if(arr[lv]!=1){
			arr2[arr2size++]=arr[lv]-1;
		}
	}
	arr1[n]=arr1[0]-(arr1[0]/2);
	arr1[0]=arr1[0]/2;
	sort(arr1, arr1+n+1, func);
	return 1+min(getans(arr2,arr2size),getans(arr1,n+1));
}

int main(){
	ll tt;
	scanf("%lld",&tt);
	ll arr[1002];
	for(ll i=1;i<=tt;i++){
		ll n;
		scanf("%lld",&n);
		for(ll lv=0;lv<n;lv++){
			scanf("%lld",&arr[lv]);
		}
		printf("Case #%lld: ",i);
		sort(arr, arr+n, func);
		ll ans=1e7;
		for(ll lv=1;lv<=1000;lv++)
		{	
			ll t=0;
			for(ll lv2=0;lv2<n;lv2++)
			{
				if(arr[lv2]>lv)
				{
					if(arr[lv2]%lv==0)
						t+=(arr[lv2]/lv-1);
					else
						t+=(arr[lv2]/lv);
				}
			}
			ans=min(ans,lv+t);
		}
		printf("%lld\n",ans);
	}	
	return 0;
}
