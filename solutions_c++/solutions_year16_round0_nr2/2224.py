#include<bits/stdc++.h>
using namespace std;
string flip(string str)
{
    int i,n=str.size();
    for(i=0;i<n;i++)
    if(str[i]=='-')
        str[i]='+';
    else
        str[i]='-';
    return str;
}
int main()
{
    ifstream cin("a.txt");
    ofstream cout("b.txt");
    int t,n,i,ans=0,var=0;
    string str;
    cin>>t;
    while(t--)
    {
        var++;
        cout<<"Case #"<<var<<": ";
        ans=0;
        cin>>str;
        while(1)
        {
            if(str[str.size()-1]=='-')
            {
                if(str[0]=='-')
                {
                    str=flip(str);
                    ans++;
                }
                else
                {
                    int j=str.size()-1;
                    while(1)
                    {
                        if(str[j]=='+')
                            break;
                        j--;
                    }
                    string temp=str.substr(0,j+1);
                    str=str.substr(j+1,str.size()-j);
                    temp=flip(temp);
                    ans++;
                    str=temp+str;
                    str=flip(str);
                    ans++;
                }
            }
            str=str.substr(0,str.size()-1);
            if(str.size()==0)
                break;
        }
        cout<<ans<<'\n';
    }
}
