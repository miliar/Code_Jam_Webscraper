#include <bits/stdc++.h>
using namespace std;

ifstream be("Oversizedin.txt");
ofstream ki("Oversizedout.txt");

int t;
vector<int> megoldas;

void process()
{
    string s1;
    be>>s1;
    int k;
    be>>k;
    vector<int> s;
    int db=0;
    for(int i=0;i<s1.length();i++)
    {
        if(s1[i]=='+') s.push_back(1);
        else s.push_back(0);
    }
    for(int i=0;i<=s.size()-k;i++)
    {
        if(s[i]==1) continue;
        db+=1;
        for(int j=i;j<=i+k-1;j++) s[j]=(s[j]+1)%2;
    }
    for(int i=s.size()-k+1;i<s.size();i++)
    {
        if(s[i]==0)
        {
            megoldas.push_back(-INT_MAX);
            return;
        }
    }
    megoldas.push_back(db);
}

int main()
{
    ios_base::sync_with_stdio(false);
    be>>t;
    for(int i=1;i<=t;i++)
    {
        process();
    }
    int akt=1;
    for(auto s:megoldas)
    {
        ki<<"Case #"<<akt<<": ";
        if(s!=-INT_MAX) ki<<s<<endl;
        else ki<<"IMPOSSIBLE"<<endl;
        akt+=1;
    }
    return 0;
}
