#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
using namespace std;

long long huiwen[70]= {1,
                       2,
                       3,
                       11,
                       22,
                       101,
                       111,
                       121,
                       202,
                       212,
                       1001,
                       1111,
                       2002,
                       10001,
                       10101,
                       10201,
                       11011,
                       11111,
                       11211,
                       20002,
                       20102,
                       100001,
                       101101,
                       110011,
                       111111,
                       200002,
                       1000001,
                       1001001,
                       1002001,
                       1010101,
                       1011101,
                       1012101,
                       1100011,
                       1101011,
                       1102011,
                       1110111,
                       1111111,
                       2000002,
                       2001002,
                       10000001,
                       10011001,
                       10100101,
                       10111101,
                       11000011,
                       11011011,
                       11100111,
                       11111111,
                       20000002,
                       100000001,
                       100010001,
                       100020001,
                       100101001,
                       100111001,
                       100121001,
                       101000101,
                       101010101,
                       101020101,
                       101101101,
                       101111101,
                       110000011,
                       110010011,
                       110020011,
                       110101011,
                       110111011,
                       111000111,
                       111010111,
                       111101111,
                       111111111,
                       200000002,
                       200010002,
                      };

int hui(long long l,long long r) {
    int i=0;
    while(huiwen[i]*huiwen[i]<l)i++;
    if(huiwen[i]*huiwen[i]>r)return 0;
    int num=0;
    for(; i<70; i++) {
        //cout<<huiwen[i]<<endl;
        if(huiwen[i]*huiwen[i]>r)return num;
        num++;
    }
}
int main() {
    //freopen("as.in","r",stdin);
    //freopen("c.txt","w",stdout);
    long long t;
    long long l,r;
    cin>>t;
    for(long long cnt=1; cnt<=t; cnt++) {
        cin>>l>>r;
        cout<<"Case #"<<cnt<<": "<<hui(l,r)<<endl;
    }
}


