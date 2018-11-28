#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	long long n;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i);
		}else{
			if(n==1){
				printf("Case #%d: 10\n",i);	
			}else{
				int a[15];
				memset(a,0,sizeof(a));
				int cont=0;
				long long r=1,v;
				while(cont!=10){
					cont=0;
					v=n*r;
					r++;
					long long h=v;
					while(h!=0){
						int e=h%10;
						a[e]=1;
						h/=10;
					}
					for(int j=0;j<10;j++){
						if(a[j]==1){
							cont++;
						}
					}
				}
				printf("Case #%d: %lld\n",i,v);
			}
		}
		
	}
	return 0;
}