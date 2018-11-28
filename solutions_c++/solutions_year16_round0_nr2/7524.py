#include<bits/stdc++.h>

using namespace std;

bool check(bool arr[],int x)
{
    for(int i=0; i<x; i++)
    {
        if(!arr[i])
            return true;
    }
    return false;
}

int main()
{
    freopen("codejam.txt","w",stdout);
    int tc,k=1;
    cin>>tc;
    while(tc--)
    {
        string s;
        cin>>s;
        bool arr[101];
         cout<<"Case #"<<k<<": ";
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='-')
                arr[i]=0;
            else
                arr[i]=1;
        }
        int ans=0;
        while(check(arr,s.size()))
        {
            bool check=0;
            for(int i=s.size()-1; i>=0; i--)
            {
                if(arr[i]==0)
                    check=1;
                if(check)
                    arr[i]=!arr[i];
            }
            ans++;
        }
        cout<<ans<<endl;
        k++;
    }
     fclose(stdout);
    return 0;
}
