#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
bool cmp(int a, int b){
    return a>b;
}
int d[110000], e[11010]; 
int f,a,c,n;
int m;
int fn(int i){
    sort(d,d+n, cmp);
    f+=i;
    a=f+d[0]-1;
    if(a<m)m=a;
    int nb=n, k=d[0];
    if(d[0]<=1)return 0;
    for(int q=1; q<=(k==9?2:1);q++){

// for(int o=0;o<n;o++)cout<<d[o]<<" ";cout<<i<<" "<<a<<endl;
        
        i=0;
        int h;
        if(k==9&&q==1){h=6;   
            for(int o=0;o<n;o++)e[o]=d[o];
        }
        else h=ceil(k/2.0);
        while(d[++i]==k&&i<n){
            d[i]=h;
            d[n++]=k-h;
        }
        d[0]=h;
        d[n++]=k-h;
        int bf=f;
        fn(i);
        f=bf;
        if(k==9){h=6;   
            for(int o=0;o<n;o++)d[o]=e[o];
        }
    n=nb;
    }
    // for(int q=1; q<k;q++){
    // }
}
int main() {
    freopen("in", "r", stdin);
     freopen("out.out", "w", stdout);
    int t; cin>>t;
    for(int j=1;j<=t;j++){
        cin>>n;
        a=0; c=0;
        for(int i=0;i<n;i++){
            cin>>d[i];
        }
        sort(d,d+n, cmp);
        m=d[0]; f=1;
        // cout<<m<<" "<<f<<" "<<a<<" "<<c<<" "<<f<<endl;
            fn(0);
        cout<<"Case #"<<j<<": "<<m<<endl;
    }
    return 0;
}
