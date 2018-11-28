#include<bits/stdc++.h>
using namespace std;
long long a,s,d[10],f,g,h,j,k,l,i,n,m;
string x;
main(){
    freopen("out.txt","w",stdout);
    cin>>n;
    for(i=1;i<=n;i++){
        cin>>x;
        cout<<"Case #"<<i<<": ";
        for(a=1;a<x.size();a++){
            if(x[a]!=x[a-1]) k++;
        }
        l=1;
        if(k%2==0 && x[0]=='-') l=0;
        if(k%2==1 && x[0]=='+') l=0;
        cout<<k-l+1<<endl;
        k=0;
    }
}
