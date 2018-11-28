#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;

    for(int tc=1; tc<=t; tc++)
    {
        string s;

        cin>>s;
        int len=s.size();

        map<char,int>mp;

        for(int i=0; i<len; i++)
        {
            mp[s[i]]++;
        }

        vector<int>v;

            while(mp['S'] && mp['I'] && mp['X'])
            {
                v.push_back(6);
                mp['S']--;
                mp['I']--;
                mp['X']--;
            }

            while(mp['E'] && mp['I'] && mp['G'] && mp['H'] && mp['T'])
            {
                v.push_back(8);
                mp['E']--;
                mp['I']--;
                mp['G']--;
                mp['H']--;
                mp['T']--;
            }

            while(mp['F'] && mp['O'] && mp['U'] && mp['R'])
            {
                v.push_back(4);
                mp['F']--;
                mp['O']--;
                mp['U']--;
                mp['R']--;
            }
            while(mp['F'] && mp['I'] && mp['V'] && mp['E'])
            {
                v.push_back(5);
                mp['F']--;
                mp['I']--;
                mp['V']--;
                mp['E']--;
            }

            while(mp['T'] && mp['H'] && mp['R'] && mp['E']>=2)
            {
                v.push_back(3);
                mp['T']--;
                mp['H']--;
                mp['R']--;
                mp['E']--;
                mp['E']--;
            }

            while(mp['S'] && mp['E']>=2 && mp['V'] && mp['N'])
            {
                v.push_back(7);
                mp['S']--;
                mp['E']--;
                mp['V']--;
                mp['E']--;
                mp['N']--;
            }

            while(mp['N']>=2 && mp['I'] && mp['E'])
            {
                v.push_back(9);
                mp['N']--;
                mp['I']--;
                mp['N']--;
                mp['E']--;
            }

            while(mp['Z'] && mp['E'] && mp['R'] && mp['O'])
            {
                v.push_back(0);
                mp['Z']--;
                mp['E']--;
                mp['R']--;
                mp['O']--;
            }

            while(mp['O'] && mp['N'] && mp['E'])
            {
                v.push_back(1);
                mp['O']--;
                mp['N']--;
                mp['E']--;
            }
            while(mp['T'] && mp['W'] && mp['O'])
            {
                v.push_back(2);
                mp['T']--;
                mp['W']--;
                mp['O']--;
            }




        sort(v.begin(),v.end());
        int l=v.size();
        cout<<"Case #"<<tc<<": ";
        for(int i=0; i<l; i++)
        {
            cout<<v[i];
        }
        cout<<endl;
        mp.clear();
        v.clear();
    }

    return 0;
}


