#include <bits/stdc++.h>
#define max 1000000

using namespace std;
int ans[10]={0};
void cal(long long  n){
    while(n){
        int p=n%10;
        ans[p]++;
        n/=10;
        
    }
    
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
	freopen("output_2.out","w",stdout);
	long long t,n,l;
	cin>>t;
	int j;
	for(j=1;j<=t;j++){
	    cin>>n;
	    
	    memset(ans,0,sizeof ans);
	    cout<<"Case #"<<j<<": ";
	    if(n==0)
	        cout<<"INSOMNIA\n";
	   else{
	       for(long long i=1; ;i++){
	           
	           cal(n*i);
	           l=n*i;
	           int k;
	           for(k=0;k<10;k++)
	            {
	                if(!ans[k])
	                    break;
	            }
	           if(k==10)
	            break;
	       }
	       cout<<l<<endl;
	   }
	    
	}
	
	
	return 0;
}
