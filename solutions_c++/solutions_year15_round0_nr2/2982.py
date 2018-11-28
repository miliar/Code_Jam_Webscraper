#include <iostream>
#include"cmath"
#include <algorithm>
#include <fstream>
using namespace std;
int a[20000];
int ans,n,m,tt,i1;
int main()
{
    //ifstream cin("2.in");
    //ofstream cout("2.out");
    cin>>n;
    for (i1=0;i1<n;i1++)
    {
        cin>>m;
        for (int j=0;j<m;j++)
            cin>>a[j];
        sort(a,a+m);
        ans=a[m-1];
        for (int i=1;i<a[m-1];i++)
        if(i<ans)
        {
            tt=0;
            for (int j=0;j<m;j++)
            {
                tt+=(a[j]/i);
                if(a[j]%i!=0)
                    tt++;
                    tt--;
            }
            tt+=i;
            if(tt<ans) ans=tt;
        }
        else break;
        cout<<"Case #"<<i1+1<<": "<<ans<<endl;
    }
    return 0;
}
