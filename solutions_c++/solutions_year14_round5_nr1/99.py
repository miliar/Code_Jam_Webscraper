//
//  main.cpp
//  a
//
//  Created by Zhou Sun on 6/14/14.
//  Copyright (c) 2014 Zhou Sun. All rights reserved.
//

#include <iostream>
using namespace std;
int ts;
long long n,p,q,r,s;
long long f[2000000];
long long ls[2000000];
long long rs[2000000];

int main(int argc, const char * argv[])
{
    cin>>ts;
    for (int tt=1; tt<=ts; tt++) {
        cin>>n>>p>>q>>r>>s;
        for (int i=0; i<n; i++) {
            f[i]=(i*p+q)%r+s;
        }
        ls[0]=0;
        for (int i=0; i<n; i++) {
            ls[i+1]=ls[i];
            ls[i+1]+=f[i];
        }
        memset(rs, 0, sizeof(rs));
        for (int i=n-1; i>=0; i--) {
            rs[i]=rs[i+1]+f[i];
        }
        long long sum= ls[n];
        int j=n;
        long double mi=sum;
        for (int i=0; i<=n && mi>ls[i]; i++) {
            while (rs[j]<ls[i]) {
                long long cur=ls[i];
                cur = max(cur, rs[j]);
                cur = max(cur, sum-ls[i]-rs[j]);
                if(cur<mi)mi=cur;
                j--;
            }
            int jj=j;
            while (rs[jj]<ls[i+1]) {
                long long cur=ls[i];
                cur = max(cur, rs[jj]);
                cur = max(cur, sum-ls[i]-rs[jj]);
                if(cur<mi)mi=cur;
                jj--;
            }
            j++;
        }
        cout<<"Case #"<<tt<<": ";
        printf("%.10Lf\n",1-mi/sum);
    }
    return 0;
}

