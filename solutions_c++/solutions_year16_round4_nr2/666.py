#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iomanip>

using namespace std;

int T;

int k,n;
double p[210];
double cp[2][210];
int a=0;
bool add[20];
int addc=0;
double ans;

void addp(double p) {
    int b=1-a;
    cp[b][0]=cp[a][0]*(1-p);
    for(int i=1;i<n;i++) {
        cp[b][i]=cp[a][i-1]*p+cp[a][i]*(1-p);
    }
    a=b;
}

void brute(int x) {
    if(x<n) {
        add[x]=false;
        brute(x+1);
        add[x]=true;
        addc++;
        brute(x+1);
        addc--;
    } else {
        if(addc==k) {
            memset(cp,0,sizeof(cp));
            cp[a][0]=1;
            for(int i=0;i<n;i++) {
                if(add[i]) {
                    addp(p[i]);
                }
            }
            if(cp[a][k/2]>ans) ans=cp[a][k/2];
        }
    }
}

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);


    cin>>T;
    for(int C=0;C<T;C++) {
        cin>>n>>k;
        for(int i=0;i<n;i++) {
            cin>>p[i];
        }
        sort(p,p+n);
        ans=0;
        brute(0);
        cout<<"Case #"<<C+1<<": "<<setprecision(20)<<ans<<endl;

    }
}
