#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int t,n,used[10];
int main()
{
    ifstream cin;
    cin.open("B-large.in");
    freopen("B-large.out","w",stdout);
    cin>>t;
    for(int o=1; o<=t; o++)
    {
        string s;
        cin>>s;
        char c[2] = {'-','+'};
        int cInd=1;
        int ans=0;
        for(int i=s.size()-1; i>=0; i--)
        {
            if(s[i]!=c[cInd])
            {
                ans++;
                cInd^=1;
            }
        }
        printf("Case #%d: %d\n",o,ans);
    }
    cin.close();
    return 0;
}
