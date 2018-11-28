#include<cstdio>
#include<iostream>
using namespace std;
int a[1000],b[100000],n,t;
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    n=0;
    for (long long i=1,j=i*i;j<100000000000000LL;i=i+1,j=i*i){
        long long k=j;
        int flag=1;
        t=0;
        while (k!=0){
	        a[t++]=k%10;
	        k/=10;
        }
        for (int o=0;o<t;o++)
        	if (a[o]!=a[t-o-1])
        		flag=0;
        k=i;
        t=0;
        while (k!=0){
	        a[t++]=k%10;
	        k/=10;
        }
        for (int o=0;o<t;o++)
        	if (a[o]!=a[t-o-1])
        		flag=0;
        if (flag==1){
	        b[n++]=j;
//	        cout<<i<<' '<<j<<endl;
		}
    }
    int test;
    cin>>test;
    for (int Test=1;Test<=test;Test++){
		long long x, y;
		cin>>x>>y;
		int ans=0;
		for (int i=0;i<n;i++)
			if (x<=b[i] && b[i]<=y)
				ans++;
		cout<<"Case #"<<Test<<": "<<ans<<endl;
	}
    return 0;
}
