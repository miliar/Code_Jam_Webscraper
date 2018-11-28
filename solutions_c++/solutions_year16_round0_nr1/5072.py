#include<bits/stdc++.h>
using namespace std;
#define MAXN 200005
#define mod 1000000007
#define ll long long
#define ull unsigned long long
ull gcd(ull a,ull b){
	ull r;
	while(1){
		r=a%b;
		if(r==0) return b;
		a=b;
		b=r;
	}
	return r;
}

int  main(){
    ll n,t,k,f,test = 1;
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	cin>>t;
    bool flag[10];
    while(t--){
        cin>>n;
        cout<<"Case #"<<test<<": ";
        if(n == 0) cout<<"INSOMNIA"<<endl;
        else{
            f = 10;
            for(int i=0;i<10;i++) flag[i] = true;
            ll m = 1;
            k = n;
            while(f){
                k = m*n;
                ll temp = k;

                while(temp){
                    if(flag[temp%10]){
                        flag[temp%10] = false;
                        f--;
                    } 
                    temp/=10;
                }
                
                m++;
            }
            cout<<k<<endl;
        }
        
        test++;
    }
    
    return 0;
}
