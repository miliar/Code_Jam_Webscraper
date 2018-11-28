#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1 ; i<=t ; i++)
    {
        string s;
        cin>>s;
        int num_changes = 1;
        for(int i=1 ; i<s.length() ; i++)
        {
            if(s[i]!=s[i-1])
                num_changes++;
        }
        int ans;
        if(s[s.length()-1]=='-')
            ans = num_changes;
        else
            ans = num_changes-1;

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
