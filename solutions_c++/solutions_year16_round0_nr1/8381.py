#include<bits/stdc++.h>
using namespace std;
long long a,s,d[10],f,g,h,j,k,l,i,n,m;
main(){
    freopen("out.txt","w",stdout);
    cin>>n;
    for(i=1;i<=n;i++){
        cin>>a;
        cout<<"Case #"<<i<<": ";
        if(a==0) {cout<<"INSOMNIA"<<endl;continue;}
        for(j=1;j<=1000;j++){
            s=a*j;
            while(s>0){
                d[s%10]++;
                if(d[s%10]==1) l++;
                s/=10;
            }
            if(l==10) {cout<<a*j<<endl;break;}

        }
        l=0;
        for(a=0;a<10;a++)d[a]=0;
    }
}
