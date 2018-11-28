#include <bits/stdc++.h>
#define ull unsigned long long
using namespace std;


int main()
{
    ios::sync_with_stdio(0);
    ifstream in;
    in.open("B-large.in");
    ofstream out;
    out.open("output.out");

    int t;in>>t;
    for(int i=1;i<t+1;i++)
    {
        string s;in>>s;
        int l=s.size();
        int last=-1;
        int arr[101]={0};
        ull ans=0;
        for(int j=0;j<l;j++)
        {
            if(s[j]=='+')
            {
                arr[j]=1;
            }
            else
            {
                last=j;
            }
        }
        for(int j=0;j<last;j++)
        {
            if(arr[j]!=arr[j+1])
            {
                ans++;
            }
        }
        if(last==-1)
        {
            out<<"Case #"<<i<<": 0\n";
        }
        else
        {
            out<<"Case #"<<i<<": "<<ans+1<<"\n";
        }

    }
}
