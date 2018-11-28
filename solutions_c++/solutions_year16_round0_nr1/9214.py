#include <iostream>
#include <stdio.h>
#include <unistd.h>
using namespace std;
int T,n,f[100],cnt,x;


int main()
{   freopen("A-large.in","r",stdin);
    freopen("tt.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&n);
        if(n==0){cout<<"Case #"<<t<<": INSOMNIA"<<endl;continue;}

        for(int i=0;i<10;i++)f[i]=0;
        cnt=10;
        x=n;
        while(cnt){
            int y=x;
            while(y){
                if(!f[y%10])f[y%10]=1,cnt--;
                y/=10;
            }
            x+=n;
        }
        x-=n;
        cout<<"Case #"<<t<<": "<<x<<endl;
    }

    return 0;
}
