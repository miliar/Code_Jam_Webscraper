#include <iostream>

using namespace std;

int main()
{
    int t,s,d;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int c=0,l=0,x=0;
        cin>>s;
        char a[s];
        cin>>a;
        for(int i=0;i<=s;i++)
        {
            d=a[i]-'0';
            if(i<=c && d!=0)
            {
                c+=d;
            }
            if(i>c && d!=0)
            {
                l=i-c;
                c=c+l+d;
                x=x+l;
            }
        }
        cout<<"Case #"<<j<<": "<<x<<"\n";
    }
    return 0;
}
