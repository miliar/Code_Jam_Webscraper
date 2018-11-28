#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
struct T{
	int a,b;
};
bool fn(T a, T b){
	if(a.a<b.a)return true;
	if(a.a>b.a)return false;
	if(a.b<b.b)return true;
	return false;
}
int main(){
	int t,te,n,m,i,j,k,a,b,flag;
	cin>>t;
	for(te=0;te<t;te++){
		cin>>n>>m;
		flag=0;
		T arr[m];
		int vis[n+1];
		for(i=0;i<=n;i++)vis[i]=0;
		for(i=0;i<m;i++){
			scanf("%d%d",&arr[i].a,&arr[i].b);
			if(arr[i].b==n)flag=1;
			vis[arr[i].b]=1;
		}
		sort(arr,arr+m,fn);
		for(i=0;i<m;){
			j=i;
			a=arr[i].a;
			b=a+1;
			while(j<m&&arr[j].a==a&&arr[j].b==b&&b<=n){
				j++;
				b++;
			}
			if(b>n&&vis[a]==0){
				cout<<"2 "<<a<<"\n";
				break;
			}		
			while(j<m&&arr[j].a==a)j++;	
			i=j;
		}
		if(i==m){
			if(flag==1)cout<<"1\n";
			else cout<<"2 "<<n<<"\n";
		}
	}
	return 0;
}
