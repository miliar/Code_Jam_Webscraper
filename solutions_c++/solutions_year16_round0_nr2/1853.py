#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t=1, i, j, l, ans[105], n;
    string s;
    cin>>t;
    for(l=1; l<=t; l++)
    {
        cin>>s;
        ans[l]=0;
        n=s.size();
        while(1)
        {
            for(i=n-1; i>=0; i--)
            {
                if(s[i]=='-')
                {
                    ans[l]++;
                    for(j=i; j>=0; j--)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                    break;
                }
            }
            if(i==-1)
                break;
        }
    }
    for(l=1; l<=t; l++)
        cout<<"Case #"<<l<<": "<<ans[l]<<endl;
    return 0;
}
