#include <iostream>
using namespace std;

string rev(string s,int n)
{
    //cout<<s<<" "<<n<<endl;
    string s1=s;
    for(int i=n;i>=0;i--)
    {
        if(s[i]=='-')
        {
            s1[n-i]='+';
        }
        else
        s1[n-i]='-';
    }
    //cout<<s1<<endl;
    return s1;
}

int main()
{
    int t,k=1;
    cin>>t;
    while(t--)
    {
        string s;
        int count=0,i;
        cin>>s;
        for(i=1;i<s.size();)
        {
            if(s[i-1]!=s[i])
            {
                s=rev(s,i-1);
                i=1;
                count++;
                continue;
            }
            i++;
        }
        if(s[s.size()-1]=='-')
            count++;
        cout<<"Case #"<<k++<<": "<<count<<endl;
    }
    return 0;
}

