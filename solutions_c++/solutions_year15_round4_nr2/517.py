#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int t;
int n;
double v,x;

double eps=0.0000001;

bool appeq(double x, double y) {
    return -eps <= x-y && x-y <= eps;
}

double r[200];
double c[200];

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    cout.precision(15);
    cin>>t;
    for(int cases=0;cases<t;cases++) {
        cin>>n>>v>>x;
        for(int i=0;i<n;i++) {
            cin>>r[i]>>c[i];
        }
        if(n==2 && c[1]<c[0]) {
            double t=r[0];
            r[0]=r[1];
            r[1]=t;
            t=c[0];
            c[0]=c[1];
            c[1]=t;
        }
        bool imp=false;
        double ans=0;
        if(n==1) {
            if (appeq(x,c[0])) {
                    ans=v/r[0];
                } else {
                    imp=true;
                }
        } else if (n==2) {
            if(appeq(x,c[0])) {
                if(appeq(x,c[1])) {
                    ans=v/(r[0]+r[1]);
                } else {
                    ans=v/r[0];
                }
            } else {
                if(appeq(x,c[1])) {
                    ans=v/r[1];
                } else {
                    if(c[0]<x&&c[1]>x) {
                        double b= (x*v-v*c[0])/(r[1]*(c[1]-c[0]));
                        double a= (v-b*r[1])/r[0];
                        ans=max(a,b);
                    } else {
                        imp=true;
                    }
                }
            }
        }
        if(imp) {
            cout<<"Case #"<<cases+1<<": "<<"IMPOSSIBLE"<<endl;
        } else {
            cout<<"Case #"<<cases+1<<": "<<ans<<endl;
        }
    }
}
