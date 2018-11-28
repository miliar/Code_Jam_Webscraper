//
//  main.cpp
//  b
//
//  Created by Zhou Sun on 6/14/14.
//  Copyright (c) 2014 Zhou Sun. All rights reserved.
//

#include <iostream>
using namespace std;
int ts,n,p,q;
int h[200],g[200];
int f[200],t[200];
int s[200];
long long a[200][200][3000];
int main(int argc, const char * argv[])
{
    cin>>ts;
    for (int tt=1; tt<=ts; tt++) {
        cin>>p>>q>>n;
        int sum=0;
        for (int i=0; i<n; i++) {
            cin>>h[i]>>g[i];
            t[i]=(h[i]-1)/q;
            sum+=t[i]+1;
            s[i+1]=s[i]+t[i]+1;
            int r=(h[i]-1)%q+1;
            f[i]=(r-1)/p+1;
        }
        long long mx=0;
        memset(a, 0, sizeof(a));
        for (int i=0; i<=n; i++) {
            for (int j=0; j<=i; j++) {
                for (int k=0; k<=sum; k++) {
                    if (a[i][j][k]>mx) {
                        mx=a[i][j][k];
                    }
                    a[i+1][j][k]=max(a[i+1][j][k],a[i][j][k]);
                    if(f[i]+k<=s[i+1]-j)a[i+1][j+1][k+f[i]]=a[i][j][k]+g[i];
                    
                }
            }
        }
        cout<<"Case #"<<tt<<": "<<mx<<endl;
    }
    return 0;
}

