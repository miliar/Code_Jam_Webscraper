#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

    freopen("A-large.in","r",stdin);
    freopen("CJ16-01.out","w",stdout);
    long long n,j;
    int t,a[10],rem,cnt,k,flag,c,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        flag=0;
        c=1;
        for(k=0;k<10;k++)
            a[k]=0;

        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        j=n;
        while(1)
        {
            cnt=0;
            while(j>0)
            {
                rem=j%10;
                j=j/10;
                a[rem]=1;
            }
            for(j=0;j<10;j++)
            {
                if(a[j]==1)
                {
                    cnt++;
                    if(cnt==10)
                    {
                        flag=1;
                        break;
                    }
                }
            }
            if(flag==1)
                break;

            c++;
            j=c*n;

        }
        if(i==t)
        cout<<"Case #"<<i<<": "<<c*n;
        else
        cout<<"Case #"<<i<<": "<<c*n<<endl;


    }
    return 0;
}

