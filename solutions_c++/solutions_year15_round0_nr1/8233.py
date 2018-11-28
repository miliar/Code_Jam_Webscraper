#include <iostream>

using namespace std;

int main()
{
    short t;
    cin>>t;
    for(short i=1;i<=t;i++)
    {
        short s, count=0,ans=0;
        cin>>s;
        char c;
        for(short j=0;j<=s;j++)
        {
            cin>>c;
            if( j > count && c!='0')
            {
                ans += (j-count);
                count += (j-count);
            }
            count += (c-'0');
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
