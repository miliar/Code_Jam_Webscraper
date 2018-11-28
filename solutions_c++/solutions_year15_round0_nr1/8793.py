#include <bits/stdc++.h>

using namespace std;

int main()
{
    int num;
    cin>>num;
    for (int i = 1 ; i <=num ; i++)
    {
        int n;
        string s;
        cin>>n>>s;
        int sum=0;
        int comp=0;
        for (int j = 0 ; j <=n ; j++)
        {
            if (j>sum)
            {
                 comp++;
                 sum++;
            }
            sum+=(s[j]-'0');
        }
        cout<<"Case #"<<i<<": "<<comp<<endl;
    }
    return 0;
}
