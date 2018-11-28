#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input6.in","r",stdin);
    freopen("output6.txt","w",stdout);
    long long int a,b,c,d,e,f,g,h,i,j,k,l;
    int arr[10];
    cin>>a;
    for(i=1;i<=a;i++)
    {
        cin>>b;
        if(b==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        memset(arr,0,sizeof(arr));
        f=e=0;
        while(e!=10)
        {
            f+=b;
            c=f;
            while(c>0)
            {
                d=c%10;
                if(arr[d]==0)
                {
                    arr[d]=1;
                    e++;
                }
                c=c/10;
            }
        }
        cout<<"Case #"<<i<<": "<<f<<"\n";
    }
    return 0;
}
