#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cs=1;
    cin>>t;
    string ss;
    while(t--)
    {
        cin>>ss;
        int cnt = 1;
        for(int i = 1; i < ss.size() ; i++)
        {
            if(ss[i] != ss[i-1]) cnt++;
        }
        if(ss[ss.size()-1] == '+') cnt--;
        printf("Case #%d: %d\n", cs++, cnt);
    }
    return 0;
}
