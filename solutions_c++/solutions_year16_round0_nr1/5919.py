#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;
int arr[10],faltan,res[1000000],pot,temp,voy,t,casos,n;
int main()
{
    for (long long i=1;i<=1000000;i++){
        if (i==1000000)
            int lalala=0;
        faltan=10;
        voy=1;
        for (int j=0;j<=9;j++)
            arr[j]=0;
        while (faltan){
            temp=i*voy;
            while (temp){
                if (arr[temp%10]==0){
                    faltan--;
                    arr[temp%10]=1;
                }
                temp/=10;
            }
            if (faltan) voy++;
        }
        res[i]=voy*i;
    }
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    for (casos=1;casos<=t;casos++){
        cin>>n;
        if (n==0)
            cout<<"Case #"<<casos<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<casos<<": "<<res[n]<<endl;
    }
    return 0;
}
