#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        char s[200];
        cin>>s;
        int n=strlen(s);
        char curr='+';
        int count_ans=0;
        for(int j=n-1;j>=0;j--)
        {
            if(s[j]!=curr)
            {
                count_ans++;
                curr=s[j];
            }
        }
        cout<<"Case #"<<i+1<<": "<<count_ans<<endl;
    }
    return 0;
}
