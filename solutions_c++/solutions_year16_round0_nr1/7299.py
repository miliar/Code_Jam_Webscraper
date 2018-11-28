#include<bits/stdc++.h>
#define MX 100000
#define pb push_back
#define mp make_pair
#define fs first
#define sec second
#define sc scanf
#define pr printf
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("outputLarge.in","w",stdout);
	long long int n,t,i,j,k,m,T;
	cin>>T;
	for(t=1;t<=T;++t){
		cin>>n;
		if(n==0)
			cout<<"Case #"<<t<<": INSOMNIA\n";
		else{
		int a[10];
		memset(a,0,sizeof(a));
		int flag=0;
		k=n;
        for(i=1;i<=1000000;++i){
        	m=n;
        	while(m!=0){
                j=m%10;
                a[j]=1;
                m/=10;
        	}
        	flag=0;
           for(int x=0;x<10;++x){
           	if(a[x]==0)
           		{
           			flag=1;
           	        break;
           		}
           }
           if(flag==0)
            break;
           n+=k;
        }
        if(flag==0)
        	cout<<"Case #"<<t<<": "<<n<<"\n";
        else
        	cout<<"Case #"<<t<<": INSOMNIA\n";
    }
	}
	return 0;
}