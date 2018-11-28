#include <bits/stdc++.h>
using namespace std;
long long n,j;
int a[100];
long long q[50][11],w[11],d[11];
long long prime(long long w){
    for (long long i=2;i*i<=w;i++)
        if(w%i==0)return i;
    return -1;
}
bool check(){
    for (int i=2;i<=10;i++){
        d[i]=prime(w[i]);
        if(d[i]==-1)return false;
    }
    return true;
}
bool back(long long k){
    long long i,l;
    if(k==n){
        if(check()){
            j--;
            for (i=0;i<n;i++)
                cout<<a[i];
            cout<<" ";
            for (i=2;i<=10;i++)
                cout<<d[i]<<" ";
            cout<<endl;
            if(j==0)return true;
        }
    }
    else{
        if(k==0||k==n-1){
            a[k]=1;
            for (l=2;l<=10;l++){
                w[l]+=(q[n-k-1][l]);
            }
            if(back(k+1))return true;
            for (l=2;l<=10;l++){
                w[l]-=(q[n-k-1][l]);
            }
        }
        else{
            for (i=0;i<2;i++){
                a[k]=i;
                for (l=2;l<=10;l++){
                    w[l]+=i*(q[n-k-1][l]);
                }
                if(back(k+1))return true;
                for (l=2;l<=10;l++){
                    w[l]-=i*(q[n-k-1][l]);
                }
            }
        }
    }
    return false;
}
int main(){
    long long i,cas,sum,l;
    long long k=1000000000011011;
    cin>>cas;
    cin>>n>>j;
    cout<<"Case #1:\n";
    for (i=0;i<n;i++)
        for (l=2;l<=10;l++)
            i==0 ? q[i][l]=1 : q[i][l]=q[i-1][l]*l;
    back(0);
}
