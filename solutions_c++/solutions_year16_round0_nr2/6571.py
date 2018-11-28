#include<stdio.h>
#include<iostream>
#include<set>
using namespace std;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    for(int i=1 ; i<=t ; i++)
    {
        string s;
        cin>>s;
        int cnt=0, p=0, l=s.size();

        for(int x=0 ; x<l ; x++)
        {
            if(x==0 || s[x]!=s[x-1])
            {
                if(s[x]=='-')
                {
                    cnt+=p+1;
                }
                else
                {
                    p=1;
                }
            }

        }

        cout<<"Case #"<<i<<": "<<cnt<<endl;

    }
}
