#include <iostream>
#include<bits/stdc++.h>
#define LIM 72

using namespace std;

int main()
{
    freopen("inputl.txt","r",stdin);
    freopen("outputl.txt","w",stdout);
    int n,rem,ar[10],j,k,flag,t,m,num;
    cin>>t;
    for(m=1;m<=t;m++)
    {
        cin>>num;
        if(num==0)
        {
            cout<<"Case #"<<m<<": INSOMNIA"<<endl;
            continue;
        }
        for(k=0;k<10;k++)
            ar[k]=0;
        for(j=1;j<=LIM;j++){
            n = num*j;
            while(n!=0){
                rem=n%10;
                ar[rem]=1;
                n/=10;
            }
            flag=0;
            for(k=0;k<10;k++){
                if(ar[k]==0){
                    flag=1;
                    break;
                }
            }
            if(flag==0)
             {
                 cout<<"Case #"<<m<<": "<<num*j<<endl;
                 break;
             }
        }
    }
    return 0;
}
