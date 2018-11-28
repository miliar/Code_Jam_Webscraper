#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	int p,n,i,arr[1000],t,k,ans,f=0,j,l;
	long int var;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		ans=0;
		int flag[1000]={0};
		cin>>p>>n;
		for(i=0;i<n;i++)
			cin>>arr[i];
		sort(arr,arr+n);
		int c=0;
			var=p;f=0;
			for(i=0;i<n;)
			{
				if(var>arr[i]){
					var+=arr[i];flag[i]=1;
					i++;
				}
				else{ l=0;
					while(var<=arr[i] ){l++;
						if(i==n-1){
							ans++;i++;f=1;break;}
						else{
							ans++;
							var+=var-1;
							if(l>=n-i){
							ans=ans-l+n-i;
							f=1;break;}
							}	
						}
					}
				if(f) break;
			}
				cout<<"Case #"<<k<<": "<<ans<<endl;
		}
		return 0;
	}
