#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    #define int long long
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in",ios::in);
    fout.open("Outputs2.in",ios::out);
    int t,i,n,Case=1,m,p,j,l,lastminus;
    bool isplus,isminus;
    string s;
    fin>>t;
    while(Case<=t)
    {
        fin>>s;
        l=s.length()-1;
        m=0;
        while(m>=0)
        {
            int c=0;
            for(i=0;i<=l;i++)
                if(s[i]=='+')
                c++;
            if(c==s.length())
                break;
            for(j=l;j>=0;j--)
            {
                if(s[j]=='-')
                    break;
            }
            lastminus=j;
            if(s[0]=='-')
            {
                reverse(&s[0],&s[lastminus+1]);
                for(i=0;i<=lastminus;i++)
                {
                    if(s[i]=='+')
                        s[i]='-';
                    else
                        s[i]='+';
                }
            }
            else
            {
               for(j=lastminus;j>=0;j--)
               {
                   if(s[j]=='+')
                    break;
               }
               reverse(&s[0],&s[j+1]);
                for(i=0;i<=j;i++)
                {
                    if(s[i]=='+')
                        s[i]='-';
                    else
                        s[i]='+';
                }
            }
            //cout<<s<<endl;
            m++;
        }

        fout<<"Case #"<<Case<<": "<<m<<endl;

            Case++;
    }
}
