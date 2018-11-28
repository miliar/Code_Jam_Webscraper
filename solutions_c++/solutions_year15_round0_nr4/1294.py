#include<cstdio>
#include<iostream> 
#include<cstring>
#include<string>
#define pr puts("RICHARD")
#define pg puts("GABRIEL")
using namespace std;

int test,n,i,x,r,c,t;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>test;
    for (t=1;t<=test;t++){
        cout<<"Case #"<<t<<": ";
        cin>>x>>r>>c;
        if (x==1){
           pg;
           continue;
        }
        if (x==2){
           if ((r*c)&1) pr;
           else pg;
           continue;
        }
        if (x==3){
           if (((r*c)%3)|r==1|c==1) pr;
           else pg;
           continue;
        }
        if (((r*c)%4)|(r<4&&c<4)|r==1|c==1|r==2|c==2) pr;
        else pg;
    }
}
