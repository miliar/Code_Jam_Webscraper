#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string.h>

using namespace std;

int main(){

    freopen("gcj1_input.txt","r",stdin);
    freopen("gcj1_output.txt","w",stdout);

    int t,j;
    cin>>t;
    for(j=1;j<=t;j++){
        long long n,i,a[15],x=2,cnt=0,found=0,temp,val;
        cin>>n;
        val=n;
        memset(a,0,sizeof(a));
        while(1){
            temp=n;
            while(temp>0){
                if(a[temp%10]==0){
                    cnt++;
                    a[temp%10]++;
                }
                temp/=10;
            }
            if(cnt==10){
                found=1;break;
            }
            if(val*x==n)break;
            n=val*x;
            x++;
        }
        cout<<"Case #"<<j<<": ";
        if(found)cout<<n<<"\n";
        else cout<<"INSOMNIA\n";
    }
    return 0;







}
