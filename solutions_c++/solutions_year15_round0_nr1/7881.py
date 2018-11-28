#include<iostream>
#include<string>
using namespace std;
int main()
{
    long long int t,i,n,s[10000],sum = 0,ans = 0,c,coun = 0,an[10000];
    string st;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cin>>st;
        for(i =0;i <= n;++i)
            s[i] = st[i] - 48;
        sum = s[0];
        for(i = 1;i <= n;++i)
        {
            if(s[i] == 0)
                continue;
            if(sum >= i)
            {
                sum = sum+s[i];
            }
            else
            {
                c = i-sum;
                ans = ans+c;
                sum = sum + s[i] + c;
            }
        }
        an[coun] = ans;
        ++coun;
        ans = 0;
        sum = 0;
    }
    for(i =0;i<coun;++i)
        cout<<"Case #"<<i+1<<": "<<an[i]<<endl;
    return 0;
}
