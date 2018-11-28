#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int x[111],y[111];
int a[111][111];
int main() {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("b.txt","w",stdout);
    int t,m,n;
    bool mark;
    cin>>t;

    for(int cnt=1; cnt<=t; cnt++) {
        mark=1;
        cin>>n>>m;
        for(int i=0; i<111; i++) {
            x[i]=y[i]=0;
        }
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                cin>>a[i][j];
                if(a[i][j]>x[i])x[i]=a[i][j];
                if(a[i][j]>y[j])y[j]=a[i][j];
            }
        }
         for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(a[i][j]<x[i]&&a[i][j]<y[j])mark=0;
            }
         }
        cout<<"Case #"<<cnt<<": ";

        if(mark)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }

}
