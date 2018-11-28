#include <bits/stdc++.h>

using namespace std;


int main()
{
    freopen("prot.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long i,j,k,l,m,n,p,q,rel=0;
    cin>>n;
    string s,s1;
    while(n--)
    {
        rel++;
        cin>>s;
        l=s.length();
        s1="";
        m=0;
        while(s.length()>0)
        {
            s1="";
            i=s.length()-1;
            while(s[i]!='-' && i>=0)
                i--;
            for(j=0;j<=i;j++)
                s1+=s[j];
            if(i>=0)
            {
                p=s1.length();
                if(s1[0]=='-')
                {

                    k=0;
                    while(s1[k]!='+' && k<p)
                        k++;
                    s="";
                    for(j=p-1;j>=k;j--)
                    {
                        if(s1[j]=='+')
                            s += '-';
                        else
                            s += '+';
                    }
                    m++;
                }
                else
                {
                    k=0;
                    s="";
                    while(s1[k]!='-' && k<p)
                        k++;
                    while(s1[k]!='+' && k<p)
                        k++;
                    for(j=p-1;j>=k;j--)
                    {
                        if(s1[j]=='+')
                            s += '-';
                        else
                            s += '+';
                    }
                    m += 2;
                }
            }
            else
            {
                break;
            }
        }
        cout<<"Case #"<<rel<<": "<<m<<endl;
    }
    return 0;
}
