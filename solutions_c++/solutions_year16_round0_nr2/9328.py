#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    cin>>test;
    for(int x=1;x<=test;x++)
    {
        string str;
        cin>>str;
        int n=str.size();
        str+="+";
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(str[i]!=str[i+1])
                ans++;
        }
        cout<<"Case #"<<x<<": "<<ans<<endl;
    }
    fclose(stdout);
}
