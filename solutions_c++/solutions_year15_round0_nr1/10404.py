#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MAX numeric_limits<int>::max()
#define MIN numeric_limits<int>::min()
#define MOD 1000000007
int shyness[1003];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    cin>>tc;
    int d,i,j;
    int len,maxi;
    string num;
    int tot,req;
    for(d=1;d<=tc;d++)
    {
        cin>>maxi>>num;
        tot=num[0]-'0';
        len=num.length();
        req=0;
        for(i=1;i<len;i++)
        {
            if(num[i]=='0')
                continue;
            if(tot>=i)
            {
                tot+=num[i]-'0';
            }
            else
            {
                req+=i-tot;
                tot+=num[i]-'0';
                tot+=req;
            }
        }
        cout<<"Case #"<<d<<": "<<req<<"\n";
    }
    return 0;
}
