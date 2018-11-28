#include<iostream>
#include<cstdio>
#include<string.h>
using namespace  std;
int main()
{
	int t,k=0;
        freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
	scanf("%d",&t);
	while(t--){
		int smax,need=0;
		scanf("%d",&smax);
		char s[1005];
		scanf("%s",s);
		fflush(stdin);

		int arr[smax];
		for(int i=0;i<=smax;i++){
			arr[i]=s[i]-48;
		}
		int standing=s[0]-48;
	
		for(int i=1;i<=smax;i++){
			arr[i]=arr[i]+arr[i-1];
		//	cout<<arr[i]<<" " ;
		}
		for(int i=0;i<=smax;i++){
			if(i>=arr[i]+need)
			need++;
		}
	/*	for(int i=1;i<=smax;i++)
		{
			if(standing<i){
				cout<<i<<" "<<s[i]<<" ";
				need=need+i-standing;
				standing= standing + need ;
			}
			else
			 	standing=standing + s[i] - 48;		 	
		}	
	*/
		k++;
		printf("Case #%d: %d\n",k,need);
		
	}	
	return 0;
}
