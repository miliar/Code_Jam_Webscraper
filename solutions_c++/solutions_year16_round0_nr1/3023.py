#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int dig[15];

void f()
{
    int n,i,j,x;
    memset(dig,0,sizeof dig);
    cin>>n;
    for(i=1;i<=1000;i++){
        x=n*i;
        while(x){
            dig[x%10]=1;
            x/=10;
        }
        for(j=0;j<=9;j++)
            if(dig[j]==0)
                break;
        if(j==10){
            cout<<n*i<<endl;
            return;
        }
    }
    cout<<"INSOMNIA"<<endl;
}
int main(){
    int t,x=0;
    freopen("sheep.in","r",stdin);
    freopen("sheep.out","w",stdout);
    cin>>t;
    while(t--){
        cout<<"Case #"<<++x<<": ";
        f();
    }
    return 0;
}
