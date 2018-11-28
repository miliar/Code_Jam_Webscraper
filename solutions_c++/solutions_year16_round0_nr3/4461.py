#include <bits/stdc++.h>
#include<iostream>
using namespace std;
typedef long long int lli;
typedef vector<lli> vi;
typedef vector<vector<lli> > vvi;
#define read() freopen("C-small-attempt1.in", "r", stdin)
#define write() freopen("output2.txt", "w", stdout)
//static int prime[10000000];
void solve(vi &ps, lli prime[]){
    for(lli i=1; i<=10000000; i++) prime[i]=0;
    for(lli i=4; i<=10000000; i+=2)
        prime[i]=2;
    for(lli i=3; i<=sqrt(10000000); i+=2){
        if(prime[i]==0){
            for(lli j=i*i ; j<=10000000; j+=(2*i)){
                prime[j]=i;
            }
        }
    }
    for(lli i=2; i<10000000; i++){
        if(prime[i]==0)ps.push_back(i);
    }
}
lli checkp(vi ps, lli x, lli prime[]){

    lli n=ps.size();
    if(x<=10000000)return prime[x];
    else {
        for(lli i=2; i<=sqrt(x) && i<n; i++){
            if(x%ps[i]==0){
                x/=ps[i];
                return ps[i];
            }
        }
        if(sqrt(x)> n){
            for(int i=ps[n-1]; i<= sqrt(x); i+=2)
            {
                if(x%i==0){
                    x/=i;
                    return i;
                }
            }
        }
        return 0;
    }
}

int main()
{
    read(); write();
    lli* prime=new lli [10000001];
    vi ps, ans(11);
    solve(ps ,prime);
    lli t,x,N, n, h,l, k,p,j,J,num=0, fin=0, flag=0;
    cin>>t; x=t;
    while(t--){
        cin>>N>>J; num=0;
        h= (1<<N)-1; l=(1<<(N-1))+1;
        cout<<"Case #"<<x-t<<": "<<endl;
        for(lli i=l; i<=h && num<J; i+=2){
            n = i;
            if(checkp(ps,i,prime)!=0){
                ans[2]=checkp(ps,i,prime);
               // cout<<"i :" <<i <<endl;
                for(j=3; j<=10; j++){
                        n=i;
                        p=1; k=0;ans[j]=0;
                    for(k; k<N; k++){
                        if((n&1)==1){
                            ans[j]+=p;
                        }p*=j;
                        n=(n>>1);
                    }
                        //cout<<"ans: "<<j <<": "<<ans[j]<<endl;
                        lli aa=checkp(ps,ans[j],prime);
                        if(aa==0){
                            flag=1;
                            break;
                        }
                    ans[j]=aa;
                }
                    if(flag==1){
                        flag=0;
                        continue;
                    }
                    if(j==11){
                        num++;
                        lli number=0;p=1;
                        n=i;
                        for(lli j=0; j<N; j++){
                            if((n&1)==1){
                                    number+=p;
                                }n=(n>>1);
                                p*=10;
                        }cout<<number<<" ";
                        for(j=2; j<=10; j++){
                            cout<<ans[j]<<" ";
                        }cout<<endl;
                    }
            }

            //cout<<"--------"<<endl;
        }
    }
}
