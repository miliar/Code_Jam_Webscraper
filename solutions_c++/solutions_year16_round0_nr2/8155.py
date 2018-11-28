#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,p,j,res;
    scanf("%d",&t);
    string s;

    for(i=0;i<t;i++)
    {
        res=0;
        vector<char> a;
        a.clear();
        cin>>s;
        int l=s.length();
        j=0;
        while(s[j]=='-'&&j<l)
        {
            s[j]='+';
            res=1;
            j++;
        }
        a.push_back(s[0]);
        p=s[0];
        for(j=1;j<l;j++)
        {
            if(s[j]!=p)
            {
                a.push_back(s[j]);
                p=s[j];
            }
        }
        if(a.size()!=1)
        {
            res=res+a.size()-a.size()%2;
        }
        printf("Case #%d: %d\n",i+1,res);
    }
}
