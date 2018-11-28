#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 1000000
#define vll vector<ll>
string s;
deque<char>dq;
void init()
{
    while(!dq.empty())
        dq.pop_back();
}
int main()
{
    int t;

    FILE *f=freopen("output.txt","w",stdout);
    FILE *in=freopen("input.txt","r",stdin);
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>s;
        init();
        int len=s.size();
        char f,l;
        for(int i=0;i<len;i++)
        {
            if(i==0)
                dq.push_back(s[i]),f=s[i],l=s[i];
            else
            {
                if(s[i]>=f)
                    dq.push_front(s[i]),f=s[i];
                else
                    dq.push_back(s[i]),l=s[i];
            }
        }
        cout<< "Case #"<<tc<< ": ";
        for(int i=0;i<len;i++)
            cout<<dq[i];
        cout<<endl;
    }

    fclose(in);
    fclose(f);
    return 0;
}
