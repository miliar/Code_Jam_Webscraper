#include<bits/stdc++.h>
using namespace std;
const int nmax=100000000;

int f[nmax],p[nmax],nprime,n,T,J,uoc[11];

long long value(int k, int cs){
    long long res=1,p=cs;
    for (int i=0;i<n-2;i++){
        res+=p*(k&1);
        k>>=1;
        p*=cs;
    }
    return res+p;
}

long long timuoc(long long x){
    if (x<nmax) return f[x]==x?0:f[x];
    for (int i=0;i<nprime && p[i]*p[i]<=x;i++)
        if (x%p[i]==0) return p[i];
    return 0;
}

void solve(int v){
    for (int k=2;k<=10;k++){
        long long x=value(v,k);
        uoc[k]=timuoc(x);
        if (uoc[k]==0) return;
        //printf("Uoc cua %lld la %d\n",x,uoc[k]);
    }
    cout<<1;
    for (int i=n-3;i>=0;i--) cout<<((v>>i)&1);
    cout<<1;
    for (int i=2;i<11;i++) cout<<" "<<uoc[i];
    cout<<endl;
    J--;
}

main(){
    //freopen("out.txt","w",stdout);
    for (int i=2;i<nmax;i++){
        if (f[i]==0) f[i]=p[nprime++]=i;
        for (int j=0;j<nprime && p[j]*i<nmax && p[j]<=f[i];j++) f[p[j]*i]=p[j];
    }
    cin>>T;
    for (int t=1;t<=T;t++){
        cin>>n>>J;
        cout<<"Case #"<<t<<":\n";
        for (int i=0;1;i++){
            solve(i);
            if (J==0) break;
        }
    }
}
