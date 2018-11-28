#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        int n;
        cin>>n;
        getchar();
        int a[n+1];
        char c;
        int i;
        for(i=0;i<n+1;i++)
        {
            cin>>c;
            a[i]=c-'0';
        }
        int te=a[0];
        int s=0;
        for(i=1;i<n+1;i++)
        {
            if(i>te)
            {
                s+=i-te;
                te=i;
            }
            te+=a[i];
        }
        cout<<"Case #"<<tci<<": "<<s<<endl;
    }
    return 0;
}
