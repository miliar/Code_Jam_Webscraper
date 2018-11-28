#include <bits/stdc++.h>
using namespace std;
#define ll long long
int t,ans=0;
string str;
bool check(string s)
{
    bool ret=true;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='-')
        {
            ret=false;
            break;
        }
    }
    return ret;
}
string flip(string s,int n)
{
    string ret=s;
    //cout<<ret<<"       flip"<<endl;
    for(int i=0;i<=n;i++)
    {
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
        //cout<<i<<endl;
    }
    for(int i=0,j=n;i<=j;i++,j--)
    {
        ret[i]=s[j];
        ret[j]=s[i];
        //cout<<i<<endl;
    }
    return ret;
    //cout<<"end Flip"<<endl;
}
int main()
{
    FILE *ip,*out;
    ifstream inFile;
    ofstream outFile;
    inFile.open("B-small-attempt0.in");
    outFile.open("output_file.txt");
    inFile>>t;
    //cin>>t;
    for(int i=1;i<=t;i++)
    {
        ans=0;
        //cin>>str;
        inFile>>str;
        queue<string>q;
        map<string,int>mp;
        q.push(str);
        mp[str]=1;
        int flag=0;
        while(!q.empty())
        {
            str=q.front();
            q.pop();
            for(int k=0;k<str.size();k++)
            {
                string flp;
                flp=flip(str,k);
                //cout<<flp<<" "<<str<<endl;
                if(mp[flp]==0)
                {
                    mp[flp]=mp[str]+1;
                    q.push(flp);
                    if(check(flp))
                    {
                        flag=1;
                        ans=mp[str];
                        break;
                    }
                }
                if(flag)
                    break;
            }
            if(flag)
                break;
        }
        //cout<<ans<<endl;
        outFile<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
