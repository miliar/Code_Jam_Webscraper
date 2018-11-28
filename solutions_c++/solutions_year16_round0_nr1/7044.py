#include <bits/stdc++.h>
bool digits[10];
using namespace std;

int tryy(int x){
    if(x==0)return -1;

    int g=x;
    for(int i=0;i<10;i++){
        digits[i]=false;
    }
    bool z=false;
    while(!z){
        int c=x;
        while(c>0){
            int l=c%10;
            digits[l]=true;
            c/=10;
        }
        x+=g;
        z=true;
        for(int i=0;i<10;i++){
            if(digits[i]==0) z=false;
        }
    }
    int m=x-g;
    return m;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,k;
    cin>>t;
    int a[t];
    for(int i=0;i<t;i++){
        cin>>k;
        a[i]=tryy(k);
    }
    for(int i=0;i<t;i++){
        if(a[i]==-1) cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
        else cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
    }

}
