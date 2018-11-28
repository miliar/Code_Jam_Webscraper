#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

long long cs,k,c,s;

int main()
{
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>cs;
    for(int j=1;j<=cs;j++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<j<<": 1";
        for(int i=1;i<k;i++)
        {
            cout<<" "<<(long long)pow(k,c-1)*i+1;
        }
        cout<<endl;
    }
    return 0;
}
