/* coder: Anh Tuan Nguyen */
#include <bits/stdc++.h>
using namespace std;

int main()
{
#ifdef gsdt
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
#endif // gsdt

    int t;
    cin>>t;
    string s;
    for(int i=1; i<=t; i++)
    {
        cin>>s;
        char cur=s[0];
        int cnt=0;
        for(int j=0; j<s.length(); j++)
        {
            if(cur!=s[j])
            {
                cnt++;
                cur=s[j];
            }
        }
        if(cur=='-') cnt++;
        printf("CASE #%d: %d\n",i,cnt);
    }

    return 0;
}

