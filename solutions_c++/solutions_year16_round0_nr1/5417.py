#include <bits/stdc++.h>
using namespace std;
int N,K,gut,i,k,maxi,counter,T;
long long zahl,num;
bool arr[100];
int main()
{
    freopen("output.out","w",stdout);
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>zahl;
        counter=1;
        for(int j=0;j<10;j++)
        arr[j]=0;
        while(true)
        {
        if(zahl==0)
        break;
        num=zahl*counter;
        long long  temp=num;
        while(temp)
        {
            arr[temp%10]=1;
            temp/=10;
        }
        bool ok=1;
        for(int j=0;j<10;j++)
        if(!arr[j]){
        ok=false;}
        if(ok)
        break;
        counter++;
        }
    cout<<"Case #"<<i<<": ";
    if(zahl!=0)
    cout<<num;
    else cout<<"INSOMNIA";
    cout<<"\n";
    }





    return 0;
}
