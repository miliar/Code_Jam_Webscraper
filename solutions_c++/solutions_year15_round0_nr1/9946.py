#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        int n;
        string a;
        cin>>n;
        cin>>a;
        int sa[n+2];
        for(int j=0; j<n+1; j++)
        {
            sa[j]=a[j]-'0';
        }
        int p=0;
        int b=0;
        for(int y=0; y<=n; y++)
        {
            if(sa[y]!=0)
            {
                if(p>=y)
                {
                    p+=sa[y];
                }
                else
                {
                    b=b+(y-p);
                    p=p+b+sa[y];
                }
            }

        }
        cout<<"Case #"<<i+1<<": "<<b<<endl;
    }
    return 0;
}
