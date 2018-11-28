#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("output.out");

    int t;in>>t;
    for(int i=1;i<t+1;i++)
    {
        string s;
        in>>s;
        int l=s.size();
        char arrl[l],arrr[l];
        arrr[0]=s[0];
        int rl=1,ll=0;
        for(int j=1;j<l;j++)
        {
            if(s[j]>=arrr[rl-1])
            {
                arrr[rl]=s[j];
                rl++;
            }
            else
            {
                arrl[ll]=s[j];
                ll++;
            }
        }
        out<<"Case #"<<i<<": ";
        for(int j=rl-1;j>=0;j--)
        {
            out<<arrr[j];
        }
        for(int j=0;j<ll;j++)
        {
            out<<arrl[j];
        }
        out<<"\n";

    }
}
