#include<bits/stdc++.h>
using namespace std;

string invert(string a, int i)
{
        for(int j=0;j<=i;j++)
        {
                if(a[j]=='+')
                        a[j]='-';
                else
                        a[j]='+';
        }
        return a;
}

int main()
{
        int t;
        cin>>t;
        int i=0;
        while(t--)
        {
                cout<<"Case #"<<i+1<<": ";
                int count=0;
                string s;
                cin>>s;
                int l=s.length();
                for(int j=0;j<l;j++)
                {
                        if(s[l-j-1]=='-')
                        {
                                s=invert(s,l-j-1);
                                count++;
                        }
                }
                cout<<count<<endl;
        i++;
        }
        return 0;
}
