#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int T;

long long n;
bool digits[10];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    cin>>T;
    for(int C=0;C<T;C++) {
        cin>>n;
        if(n>0) {
        int dc=0;
        memset(digits,0,sizeof(digits));
        long long t=0;
        while(dc<10) {
            t+=n;
            long long ct=t;
            while(ct>0) {
                long long d=ct%10;
                if(!digits[d]) {
                    digits[d]=true;
                    dc++;
                }
                ct/=10;
            }
        }
        cout<<"Case #"<<C+1<<": "<<t<<endl;
        } else {
        cout<<"Case #"<<C+1<<": "<<"INSOMNIA"<<endl;
        }
    }
}
