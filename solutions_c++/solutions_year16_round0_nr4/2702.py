/*input-c,s,k. condition: s=k*/
#include <iostream>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<t<<": ";
        if(s == k)
        {
            for(int i=1;i<=k;i++)
                cout<<i<<" ";
        }
        cout<<endl;
    }
}