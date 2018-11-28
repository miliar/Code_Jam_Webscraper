#include <bits/stdc++.h>
using namespace std;
int t;
string x;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cin >> x;
        int v=0;
        for(int j=1;j<x.size();j++)
        {
            if(x[j]!=x[j-1])
            {
                for(int k=0;k<j;k++)
                {
                    if(x[k]=='-')
                        x[k]='+';
                    else x[k]='-';
                }
                v++;
            }
        }
        if(x[0]=='-')v++;
        cout << "Case #" << i << ": " << v << "\n";
    }
    return 0;
}
