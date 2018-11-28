#include <bits/stdc++.h>
using namespace std;
string s;
int test;
int db[26];
int ans[10];
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cin>>s;
        for(int i=0; i<10; i++) ans[i]=0;
        for(int i=0; i<26; i++) db[i]=0;
        for(int i=0; i<s.size(); i++)
        {
            db[s[i]-'A']++;
        }
        while(db['Z'-'A']>0)
        {
            db['Z'-'A']--;
            db['E'-'A']--;
            db['R'-'A']--;
            db['O'-'A']--;
            ans[0]++;
        }
        while(db['W'-'A']>0)
        {
            db['T'-'A']--;
            db['W'-'A']--;
            db['O'-'A']--;
            ans[2]++;
        }
        while(db['U'-'A']>0)
        {
            db['F'-'A']--;
            db['O'-'A']--;
            db['U'-'A']--;
            db['R'-'A']--;
            ans[4]++;
        }
        while(db['X'-'A']>0)
        {
            db['S'-'A']--;
            db['I'-'A']--;
            db['X'-'A']--;
            ans[6]++;
        }
        while(db['G'-'A']>0)
        {
            db['E'-'A']--;
            db['I'-'A']--;
            db['G'-'A']--;
            db['H'-'A']--;
            db['T'-'A']--;
            ans[8]++;
        }
        while(db['O'-'A']>0)
        {
            db['O'-'A']--;
            db['N'-'A']--;
            db['E'-'A']--;
            ans[1]++;
        }
        while(db['T'-'A']>0)
        {
            db['T'-'A']--;
            db['H'-'A']--;
            db['R'-'A']--;
            db['E'-'A']--;
            db['E'-'A']--;
            ans[3]++;
        }
        while(db['F'-'A']>0)
        {
            db['F'-'A']--;
            db['I'-'A']--;
            db['V'-'A']--;
            db['E'-'A']--;
            ans[5]++;
        }
        while(db['S'-'A']>0)
        {
            db['S'-'A']--;
            db['E'-'A']--;
            db['V'-'A']--;
            db['E'-'A']--;
            db['N'-'A']--;
            ans[7]++;
        }
        while(db['N'-'A']>0)
        {
            db['N'-'A']--;
            db['I'-'A']--;
            db['N'-'A']--;
            db['E'-'A']--;
            ans[9]++;
        }
        cout<<"Case #"<<tt<<": ";
        for(int i=0; i<10; i++)
        {
            for(int j=0; j<ans[i]; j++)
            {
                cout<<i;
            }
        }
        cout<<endl;
    }
    return 0;
}
