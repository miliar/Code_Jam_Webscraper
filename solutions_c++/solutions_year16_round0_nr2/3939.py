#include<bits/stdc++.h>
#include<algorithm>
#define ll long long int
using namespace std;
int main()
{
    ll counter,t,i,j;
    string str;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        cin>>str;
        counter=0;
        for(i=1;i<str.length();i++)
        {
            if(str[i]!=str[i-1])
                counter++;
        }
        if(str[i-1]=='-')
            counter++;
        cout<<"Case #"<<j<<": "<<counter<<endl;
    }
    return 0;
}
