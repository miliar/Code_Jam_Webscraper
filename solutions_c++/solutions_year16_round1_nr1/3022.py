#include<iostream>
#include<fstream>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
using namespace std;
long long t,used[1001],dp[1001];
string s;
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    ifstream cin;
    cin.open("A-large.in");
    ofstream cout;
    cout.open("A-large.out");
    cin>>t;
    for(int o=1; o<=t; o++)
    {
        cin>>s;
        cout<<"Case #"<<o<<": ";
        for(int i=0; i<s.size(); i++)
        {
            dp[i]=0;
            used[i]=0;
        }
        char maxC = s[0];
        int maxInd = 0;
        dp[0]=-1;
        for(int i=1; i<s.size(); i++)
        {
            dp[i]=maxInd;
            if(s[i]>=maxC)
            {
                maxC = s[i];
                maxInd = i;
            }
        }
        int ind = maxInd;
        while(ind>=0)
        {
            used[ind]=1;
            cout<<s[ind];
            ind=dp[ind];
        }
        for(int i=0; i<s.size(); i++)
            if(used[i]==0)
                cout<<s[i];
        cout<<endl;
    }
    cin.close();
    cout.close();
    return 0;
}
