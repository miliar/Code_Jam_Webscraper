#include<bits/stdc++.h>
using namespace std;
int main(){
	FILE *fin1 = freopen("input.txt", "r", stdin);
	FILE *fin2= freopen("output.txt", "w", stdout);
long long int  x,i,j,ii,k,t,n,f,ans,xx;
		scanf("%lld",&t);
	//t=1000010;
	for(ii=1;ii<=t;ii++){
		long long int v[10]={0};
		scanf("%lld",&n);
	
		xx=1;
		for(k=1;k<=100;k++){
			f=0;
			x=n*xx;
			ans=x;
			
			while(x!=0){
				v[x%10]=1;
				x=x/10;
			}
			
			xx++;
			for(i=0;i<10;i++)
				{
					if(v[i]==0)
						{
							f=1;
							break;
						}
					
				}
			if(f==0)
				break;
		}
		if(f==1)
		cout<<"Case #"<<ii<<": INSOMNIA"<<endl;
		else
		cout<<"Case #"<<ii<<": "<<ans<<endl;
		

	}

	return 0;
}