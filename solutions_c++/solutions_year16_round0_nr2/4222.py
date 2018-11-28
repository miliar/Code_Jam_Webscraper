#include <bits/stdc++.h>
using namespace std;
#define ll long long

char a[1000];
vector<char>v;
stack<char>s;
int main()
{
    int t,c;
    FILE *f=freopen("output.txt","w",stdout);
    FILE *in=freopen("input.txt","r",stdin);
    scanf("%d",&t);
    getchar();
    for(ll tc=1; tc<=t; tc++)
    {
        gets(a);
        int len=strlen(a);
        v.clear();
        while(!s.empty())
            s.pop();
        s.push('#');
        int p=0,m=0,c=0;
        for(int i=len-1; i>=0; i--)
        {
            s.push(a[i]);
            if(a[i]=='+')
                p++;
            else
                m++;
        }
        if(!p && m)
            cout<< "Case #"<<tc<< ": 1\n";
        else if(p && !m)
            cout<< "Case #"<<tc<< ": 0\n";
        else
        {
            char prev;
            while(m>0)
            {
                if(v.size()>0)
                {
                    while(s.top()==prev && s.top()!='#')
                    {
                        v.push_back(s.top());
                        s.pop();
                    }
                    for(int i=0; i<v.size(); i++)
                    {
                        if(v[i]=='+')
                            s.push('-'),m++;
                        else
                            s.push('+'),m--;
                    }
                    v.clear();
                    c++;
                }
                else
                {
                    if(s.top()!='#')
                    {
                        v.push_back(s.top());
                        prev=s.top();
                        s.pop();
                    }
                    //cout<<v[0]<<endl;

                }

            }
            cout<< "Case #"<<tc<< ": "<<c<<endl;
        }

    }
    fclose(in);
    fclose(f);
    return 0;
}
