#include<iostream>
#include<cstring>
using namespace std;
int main(){
//freopen ("A-small-attempt0 (2).txt","r",stdin);
freopen ("output.txt","w",stdout);
    int a,b,c,t,i;
    cin>>t;
    for(int it=1;it<=t;it++){
            bool res=false;
            cout<<"Case #"<<it<<": ";
            int x,r,c;
            cin>>x>>r>>c;
            if(c<r){
                         a=r;
                         r=c;
                         c=a;
                         }
            if(x==1){
                    if((r*c)>=1)
                    res=true;
                    }
            else if(x==2){
                          if((r*c)>=2)
                     if((r*c)%2==0)
                     res=true;
                     }
            else if(x==3){
                 if(r>=2&&c>=3)
                 if((r*c)%3==0)
                     res=true;
                 }
                 else{
                      if((r*c)==16||(r*c)==12)
                      res=true;
                      }
            if(res)
            cout<<"GABRIEL"<<endl;
            else
            cout<<"RICHARD"<<endl;
            }
    }
