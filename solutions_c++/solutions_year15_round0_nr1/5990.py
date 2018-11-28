#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int s;
    long int sum,count;
    char str[1002];
    int c;
    for(int T=0;T<t;T++)
    {
        cin>>s;
        cin>>str;
        sum=0;
        count=0;
        for(int i=0;i<=s;i++)
        {
            c=str[i]-'0';
            if(i>sum)
            {
                count+=i-sum;
                sum+=i-sum;
            }
            sum+=c;
        }
        cout<<"Case #"<<T+1<<": "<<count<<"\n";
    }
    return 0;
}
