//HARE KRISHNA
#include<bits/stdc++.h>
using namespace std;

#define pb push_back

#define sz1 44900
#define sz2 25000

#define ll long long
char sieve[(sz1>>4)+7];
int prime[sz2];
char flag[((sz1*sz1)>>4)+7];

vector<ll>anothervector[70000];
vector<ll>mainvec;
void bit_sieve(){
    int i,j,k,r;
    prime[0]=2;
    k=1;
    int lim=(int)sqrt(sz1)+1;
    for(i=3;i<sz1;i+=2){
        if(!(sieve[i>>4]&(1<<((i>>1)&7)))){
            prime[k++]=i;
            if(i<lim){
                r=i<<1;
                for(j=i*i;j<sz1;j+=r){
                    sieve[j>>4]|=(1<<((j>>1)&7));
                }
            }
        }
    }
    return;
}
vector<int>primeinrange;
void segmentsieve(int a,int b){
    int st,en,r,i,j,rr;
    for(i=a;i<=b;i++){
        flag[i>>4]=0;
    }
    primeinrange.clear();
    if(a<=2&&b>=2)primeinrange.pb(2);
    for(i=1;prime[i]&&prime[i]<=b;i++){
        r=prime[i];
        st=max(r+r+r,(a/r+1)*r);
        if(!(st&1))st+=r;
        en=(b/r)*r;
        rr=(r<<1);
        if(st>b)break;
        for(j=st;j<=en;j+=rr){
            flag[j>>4]|=(1<<((j>>1)&7));
        }
    }
    for(int i=max(a,3);i<=b;i++){
        if((i&1)&&(!(flag[i>>4]&(1<<((i>>1)&7))))){
            primeinrange.pb(i);
        }
    }
    return;



}

ll arrmul[11][18];


int main(){
    freopen("input4.in","r",stdin);
    freopen("out4.txt","w",stdout);
    bit_sieve();
    segmentsieve(1,100000000);
   //int sz=primeinrange.size();
   // cout<<sz<<endl;
    ll primesz=(ll)primeinrange.size();
    //cout<<primeinrange[primesz-1]<<endl;
    ll one,two,three;

    for(one = 2;one<=10;one++){
        arrmul[one][0]=1;
        for(two=1;two<=15;two++){
            arrmul[one][two]=arrmul[one][two-1]*one;
        }
    }

    ll n;
    int upto;
    int t,tcase;
    scanf("%d",&t);
    for(tcase=1;tcase<=t;tcase++){
        scanf("%lld %d",&n,&upto);

        ll i;
        ll j;
        ll k;
        int cnt=0;
        ll which;
        ll insideloop;
        for(i=2;i<(1L<<n);i++){
            if(cnt==upto)break;

            bool joggo=true;
            if((i&(1L))==0)joggo=false;
            else if((i&(1L<<(n-1)))==0)joggo=false;
//            else{
//                ll anovar;
//                for(anovar=n;anovar<64;anovar++){
//                    if(i&(1L<<anovar)){
//                        joggo=false;
//                        break;
//                    }
//                }
//            }
            if(joggo){
                bool flag=true;
                ll representt;
                ll sum;
                for(which=2;which<=10;which++){
                    sum=0;
                    for(j=0;j<n;j++){
                        if(i&(1L<<j)){
                            sum=sum+arrmul[which][j];
                        }
                    }
                    if(which==2)representt=sum;
                    ll primefactorize=sum;
                    ll sqrthat=(ll)sqrt(primefactorize)+1;
                    ll lastone;
                    for(insideloop=0;insideloop<primesz && primeinrange[insideloop]<=sqrthat;insideloop++){
                        if((primefactorize%primeinrange[insideloop])==0){
                            lastone=primeinrange[insideloop];
                            while((primefactorize%primeinrange[insideloop])==0){
                                primefactorize/=primeinrange[insideloop];
                            }
                        }
                    }
                    if(primefactorize==sum){
                        flag=false;
                        break;
                    }
                    else{
                        anothervector[i].pb(lastone);
                    }
                }
                if(flag){
                    mainvec.pb(sum);
                    mainvec.pb(representt);
                    cnt++;
                }
            }
        }
        printf("Case #%d:\n",tcase);
        int szmainvec=mainvec.size();
        for(i=0;i<szmainvec;i+=2){
            printf("%lld",mainvec[i]);
            ll whichoneh=mainvec[i+1];
            for(j=0;j<9;j++){
                printf(" %lld",anothervector[whichoneh][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
