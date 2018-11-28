#include <bits/stdc++.h>
using namespace std;
#define syncs ios_base::sync_with_stdio(0)
#define ot(x) cout<<x<<"\n";
#define ent cout<<"\n";
#define f(i,n) for(int i=0;i<n;i++)
#define wh(n) while(n--)
int t,a[10];

int main(){
    syncs;
    cin>>t;
    f(i,t){
        unsigned long long n,last=0;
        cin>>n;
        int m=1;
        while(a[0]!=1||a[1]!=1||a[2]!=1||a[3]!=1||a[4]!=1||a[5]!=1||a[6]!=1||a[7]!=1||a[8]!=1||a[9]!=1){
            if(n==0) break;
            unsigned long long r=m*n;
            string no;
            stringstream convert;
            convert<<r;
            no=convert.str();
            f(j,no.length()){
                a[no[j]-48]=1;
            }
            m++;
            last=r;
        }
        if(n==0){
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }else{
            cout<<"Case #"<<i+1<<": "<<last<<endl;
        }
        f(k,10){
            a[k]=0;
        }
    }
    return 0;
}
