#include <bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while (t--){
        unsigned long long int n;
        cin>>n;
        int i=1,j,f=0;
        if (n==0)
            f=-1;
        long long int a[10];
        unsigned long long int k1,k2;
        for (j=0;j<10;j++)
            a[j]=0;
        while (f==0){
            k2=k1=i*n;
            i++;
            while (k1>0){
                int d=k1%10;
                a[d]++;
                k1=k1/10;
            }
            for (j=0;j<10;j++){
                if (a[j]==0)
                    break;
            }
            if (j==10){
                f=1;
                break;
            }
        }
        if (f==-1)
            cout<<"Case #"<<cas++<<": "<<"INSOMNIA"<<endl;
        else
            cout<<"Case #"<<cas++<<": "<<k2<<endl;
    }
    return 0;
}
