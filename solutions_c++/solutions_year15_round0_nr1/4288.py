#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
long long t;
int main()
{
    ifstream cin;
    cin.open("A-large.in");
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int o=1; o<=t; o++)
    {
        int n;
        string s;
        int curst=0,ans=0;
        cin>>n;
        cin>>s;
        for(int i=0; i<=n; i++)
        {
            if(curst<i&&s[i]>'0') {ans+=i-curst; curst=i;}
            curst+=s[i]-'0';
        }
        printf("Case #%d: %d\n",o,ans);
    }
    cin.close();
    return 0;
}
