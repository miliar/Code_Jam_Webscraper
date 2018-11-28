#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
    setbuf(stdout,0);
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        int n;
        cin>>n;
        int i,j;
        vector<int> a(n);
        int mo=0;
        for(i=0; i<n; i++)
        {
            cin>>a[i];
            if(a[i]>mo)mo=a[i];
        }
        int s=-1;
        vector<int> b=a;
        for(i=1;i<=mo;i++)
        {
            //cout<<"1";
            a=b;
            int tes=i;
            for(j=0;j<n;j++)
            {
                //cout<<"2";
                while(a[j]>i)a[j]-=i,tes++;
            }
            //cout<<tes<<endl;
            if(tes<s||s==-1)s=tes;
        }
        cout<<"Case #"<<tci<<": "<<s<<endl;
    }
    return 0;
}
