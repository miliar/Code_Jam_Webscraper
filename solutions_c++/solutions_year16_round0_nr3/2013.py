#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int T;

int n=16;
int J=50;

int bits[16];

long long divisors[11];

void genCoins(int i) {
    if(J==0) return;
    if(i==n-1) {
        bool nodivs=false;
        for(int j=2;j<=10;j++) {
            long long t=0;
            long long b=1;
            for(int p=0;p<n;p++) {
                t+=bits[p]*b;
                b*=j;
            }
            bool nodiv=true;
            for(int k=2;k<10000;k++) {
                if(t%k==0) {
                    divisors[j]=k;
                    nodiv =false;
                    break;
                }
            }
            if(nodiv) nodivs=true;
        }
        if(!nodivs) {
            for(int j=n-1;j>=0;j--) {
                cout<<bits[j];
            }
            for(int j=2;j<=10;j++) {
                cout<<" "<<divisors[j];
            }
            cout<<endl;
            J--;
        }
    } else {
        bits[i]=0;
        genCoins(i+1);
        bits[i]=1;
        genCoins(i+1);
    }
}

int main() {
    //freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    bits[0]=1;
    bits[n-1]=1;
    cout<<"Case #1:"<<endl;
    genCoins(1);
}
