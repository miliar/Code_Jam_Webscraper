# include <bits/stdc++.h>
using namespace std;

long long mask;
long long done = (1<<10)-1;
long long prop;

long long solve(long long a){
    //cout<<a<<endl;
    long long aux = a;
    while(aux>=10){
        mask |= ( 1<<(aux%10) );
        aux/=10;
    }
    mask |= ( 1<<(aux%10) );

    if(mask == done) return a;

    return solve(a+prop);
}

int main(){
    freopen("sheepsCodeJam.in","r",stdin);
    freopen("sheepsCodeJam.out","w",stdout);

    long long t,i;

    cin>>t;

    for(long long f=1 ; f<=t ; f++){

        cin>>i;
        mask = 0;
        prop = i;

        if(i==0){
            printf("Case #%lld: INSOMNIA\n",f);
        }else{
            printf("Case #%lld: %lld\n",f,solve(i));
        }

    }
}










