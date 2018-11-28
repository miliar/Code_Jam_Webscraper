#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    int t,n;
    fin >> t;
    map<string,int>m;
    m["ZERO"]=0;
    m["ONE"]=1;
    m["TWO"]=2;
    m["THREE"]=3;
    m["FOUR"]=4;
    m["FIVE"]=5;
    m["SIX"]=6;
    m["SEVEN"]=7;
    m["EIGHT"]=8;
    m["NINE"]=9;

    for(int tc=1;tc<=t;tc++)
    {
        fout << "Case #"<<tc<<": ";
        string s;
        fin >> s;
        int a[26];
        vector<int>v;
        for(int i=0;i<26;i++)
            a[i]=0;
        for(int i=0;i<s.size();i++)
        {
            a[s[i]-'A']++;
        }
        int temp=a['X'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(6);
            a['X'-'A']--;
            a['S'-'A']--;
            a['I'-'A']--;
        }
        temp=a['W'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(2);
            a['T'-'A']--;
            a['W'-'A']--;
            a['O'-'A']--;
        }
        temp=a['Z'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(0);
            a['Z'-'A']--;
            a['E'-'A']--;
            a['R'-'A']--;
            a['O'-'A']--;
        }
        temp=a['U'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(4);
            a['F'-'A']--;
            a['O'-'A']--;
            a['U'-'A']--;
            a['R'-'A']--;
        }
        temp=a['F'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(5);
            a['F'-'A']--;
            a['I'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
        }
        temp=a['R'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(3);
            a['T'-'A']--;
            a['H'-'A']--;
            a['R'-'A']--;
            a['E'-'A']--;
            a['E'-'A']--;
        }
        temp=a['G'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(8);
            a['E'-'A']--;
            a['I'-'A']--;
            a['G'-'A']--;
            a['H'-'A']--;
            a['T'-'A']--;
        }
        temp=a['V'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(7);
            a['S'-'A']--;
            a['E'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            a['N'-'A']--;
        }
        temp=a['O'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(1);
            a['O'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }
        temp=a['I'-'A'];
        for(int i=0;i<temp;i++)
        {
            v.push_back(9);
            a['N'-'A']--;
            a['I'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }
        sort(v.begin(),v.end());
        for(int i=0;i<v.size();i++)
            fout << v[i];
        fout << endl;
    }
    return 0;
}
