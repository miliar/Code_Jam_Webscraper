#include<bits/stdc++.h>
using namespace std;
int m[10004];
int main(){
    int t,n,Acount,Bcount,minrate;
    cin>>t;
    for(int x=1;x<=t;x++){
        cin>>n;
        for(int i=0;i<n;i++)cin>>m[i];
        //applying scheme 1 and calculate rate for scheme 2
        Acount=0,minrate=0;
        for(int i=0;i<n-1;i++){
            if(m[i]>m[i+1]){
                Acount+=(m[i]-m[i+1]);
                if(minrate<(m[i]-m[i+1]))minrate=(m[i]-m[i+1]);
            }
        }
        //apply scheme 2
        Bcount=0;
        for(int i=0;i<n-1;i++){
            if(minrate<m[i]){
                Bcount+=minrate;
            }
            else{
                Bcount+=m[i];
            }
        }
        cout<<"Case #"<<x<<": "<<Acount<<' '<<Bcount<<endl;
    }
}
