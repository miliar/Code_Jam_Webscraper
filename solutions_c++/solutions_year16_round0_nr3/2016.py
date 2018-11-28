#include <cstdio>
#include <algorithm>
#include <iostream>
#include <deque>
#include <cstring>
using namespace std;

int T,N,J;
int prm[]={2,3,5,7,11,13,17,19,23,29,31,37},pn=12;
int powmod[11][33][12];
int ans[5555],an;

int to_base_mod(int x,int b,int m) {
    int s=0;
    for (int i=N-3;i>=0;i--) {
        if (x&(1<<i)) {
            s+=powmod[b][i][m];
            s%=prm[m];
        }
    }
    return s;
}


int main () {
    cin>>T>>N>>J;

    cout<<"Case #1:"<<endl;

    for (int i=2;i<=10;i++) for (int j=0;j<pn;j++){
        int s=1;
        for (int k=1;k<N;k++) {s*=i;s%=prm[j];powmod[i][k][j]=s;}
        powmod[i][0][j]=1;
    }

    for (int p=0;an<J;) {
        for (;;p++) {
            bool flag=1;
            for (int b=2;b<=10;b++) {
                bool isprime=1;
                for (int j=0;j<pn;j++)
                    if ((1+powmod[b][N-1][j]+(b%prm[j])*to_base_mod(p,b,j))%prm[j]==0) {
                        isprime=0;break;
                    }
                if (isprime) {
                    flag=0;break;
                }
            }
            if (flag) {
                ans[an++]=p;
                ++p;break;
            }
        }
    }
    for (int i=0;i<J;i++) {
        cout<<1;
        for (int j=N-3;j>=0;j--) cout<<(bool)(ans[i]&(1<<j));
        cout<<"1 ";
        for (int b=2;b<=10;b++) {
             for (int j=0;j<pn;j++)
                    if ((1+powmod[b][N-1][j]+(b%prm[j])*to_base_mod(ans[i],b,j))%prm[j]==0) {
                        cout<<prm[j];
                        if (b!=10) cout<<' ';
                        break;
                    }
        }
        cout<<endl;
    }
}
