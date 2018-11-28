#include<iostream>
#include<stdio.h>

using namespace std;


int main()
{
    freopen("a_large.in","r",stdin);
    freopen("b.in","w",stdout);
    int T,cnt=0;
    cin>>T;

    while(T--)
    {
        int n,sum=0,count=0;
        string s;
        cin>>n>>s;

        for(int i=1;i<=n;i++)
        {
            sum += s[i-1]-'0';
            if(sum>=i)
                continue;
            else{
                count++;
                sum++;
            }

        }

        cout<<"Case #"<<++cnt<<": "<<count<<endl;
    }


    return 0;
}
