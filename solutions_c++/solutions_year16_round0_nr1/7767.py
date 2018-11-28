#include <bits/stdc++.h>
#include <string>
using namespace std;
typedef unsigned long long int ll;

#define MAXLEN 1001



int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d",&t);
    
	for(int i=0 ; i<t ; i++){
		printf("Case #%d: ",i+1);
		 ll n, k=0;
		 int cnt=0;
		 //string s="";
		 bool my[10]={0};
		 scanf("%llu",&n);
		
		 if(n==0) printf("INSOMNIA\n");
		 else{
//		 	s=itostr(n,s);
//		 	cout<<s;
		 while(cnt<10){
		 k+=n;
		 //cout<<"\n --"<<n<<"--\n";
		 	const int nz = snprintf(NULL, 0, "%llu",k);
			char buf[nz+1];
			int c = snprintf(buf, nz+1, "%llu", k);
			assert(buf[nz] == '\0');
    	 for(ll j=0;j<nz; j++) {
		  if(my[(int)buf[j]-'0']==0)	{
		  	my[(int)buf[j]-'0']=1;
		  	cnt++;
		  }
		 }
		 
		// s="";
		}
		printf("%llu\n",k); 
		}
	}
		// printf("\n");	
    return 0;
}
