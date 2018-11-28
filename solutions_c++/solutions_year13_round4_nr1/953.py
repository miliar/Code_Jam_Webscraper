#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxx=1001000;
int n,m;
int a[2222],c[2222];
int ga[2222],gc[2222],gg;
long long big,small;

long long f(int d) {
    long long t=n+n-d+1;
    t=t*d/2;
    return t;
}

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>n>>m;
        big=0;
        for(int i=0;i<m;i++) {
            int x,y,z;
            cin>>x>>y>>z;
            big+=f(y-x)*z;
            a[2*i]=x; c[2*i]=z;
            a[2*i+1]=y; c[2*i+1]=-z;
        }
        cout<<"Case #"<<T<<": ";
        //cerr<<"BIG "<<big<<endl;
        int mm=2*m;
        for(int i=0;i<mm;i++) for(int j=i+1;j<mm;j++) if (a[i]>a[j]) {
            int t=a[i]; a[i]=a[j]; a[j]=t;
            t=c[i]; c[i]=c[j]; c[j]=t;
        }
        
        small=0;
        long long r=0;
        gg=0;
        for(int i=0;i<mm;) {
            int p=a[i],cc=c[i];
            //cerr<<"i,a[i],c[i] "<<i<<' '<<p<<' '<<cc<<endl;
            i++;
            while((i<mm)&&(a[i]==p)) {
                cc+=c[i]; i++;
            }
            //cerr<<"i,p,cc "<<i<<' '<<p<<' '<<cc<<endl;
            if (cc>0) {
                ga[gg]=p;
                gc[gg]=cc;
                gg++;
                r+=cc;
            } else if (cc<0) {
                long long rr=r+cc;
                while(r>rr) {
                    long long t=r-gc[gg-1];
                    if (t>=rr) {
                        small+=f(p-ga[gg-1])*gc[gg-1];
                        gg--;
                        r=t;
                    } else {
                        long long w=r-rr;
                        small+=f(p-ga[gg-1])*w;
                        gc[gg-1]-=w;
                        r=rr;
                    }
                }
            }
        }
        //cerr<<"SMALL "<<small<<endl;
        cout<<(big-small)<<endl;
    }
    return 0;
}