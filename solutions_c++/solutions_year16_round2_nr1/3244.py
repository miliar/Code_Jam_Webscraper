#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    string S;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>S;
        int a[26]={0};

        for(int i=0;i<S.size();i++)
        {
            a[S[i]-'A']++;
        }

        vector<int> v;

        while(a['Z'-'A'])
        {
            v.push_back(0);
            a['Z'-'A']--;
            a['E'-'A']--;
            a['R'-'A']--;
            a['O'-'A']--;
        }

        while(a['X'-'A'])
        {
            v.push_back(6);
            a['S'-'A']--;
            a['I'-'A']--;
            a['X'-'A']--;
        }

        while(a['S'-'A'])
        {
            v.push_back(7);
            a['S'-'A']--;
            a['E'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            a['N'-'A']--;
        }

        while(a['W'-'A'])
        {
            v.push_back(2);
            a['T'-'A']--;
            a['W'-'A']--;
            a['O'-'A']--;
        }

        while(a['G'-'A'])
        {
            v.push_back(8);
            a['E'-'A']--;
            a['I'-'A']--;
            a['G'-'A']--;
            a['H'-'A']--;
            a['T'-'A']--;
        }

        while(a['U'-'A'])
        {
            v.push_back(4);
            a['F'-'A']--;
            a['O'-'A']--;
            a['U'-'A']--;
            a['R'-'A']--;
        }

        while(a['F'-'A'])
        {
            v.push_back(5);
            a['F'-'A']--;
            a['I'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
        }

        while(a['H'-'A'])
        {
            v.push_back(3);
            a['T'-'A']--;
            a['H'-'A']--;
            a['R'-'A']--;
            a['E'-'A']--;
            a['E'-'A']--;
        }

        while(a['O'-'A'])
        {
            v.push_back(1);
            a['O'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }

        while(a['N'-'A'])
        {
            v.push_back(9);
            a['N'-'A']--;
            a['I'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }

        sort(v.begin(),v.end());

        for(int i=0;i<v.size();i++)
            cout<<v[i];

        cout<<endl;
    }
}