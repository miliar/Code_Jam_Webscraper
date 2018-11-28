#include<bits/stdc++.h>
using namespace std;
#define pb push_back
int n,i,j,z;
map<char,int>mp;
string s;
vector<int>v;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>n;
    while(n--)
    {
        cin>>s;
        for(i=0;s[i];i++)
            mp[s[i]]++;

            if(mp['Z'])
            {
                for(j=0;j<mp['Z'];j++)
                    v.pb(0);

                mp['E']-=mp['Z'];
                mp['R']-=mp['Z'];
                mp['O']-=mp['Z'];
                mp['Z']=0;

            }
            if(mp['W'])
            {
                for(j=0;j<mp['W'];j++)
                    v.pb(2);
                mp['T']-=mp['W'];
                mp['O']-=mp['W'];
                mp['W']=0;

            }
            if(mp['U'])
            {
                for(j=0;j<mp['U'];j++)
                    v.pb(4);
                mp['F']-=mp['U'];
                mp['O']-=mp['U'];
                mp['R']-=mp['U'];
                mp['U']=0;

            }
            if(mp['F'])
            {
                for(j=0;j<mp['F'];j++)
                    v.pb(5);
                mp['I']-=mp['F'];
                mp['V']-=mp['F'];
                mp['E']-=mp['F'];
                mp['F']=0;

            }
            if(mp['X'])
            {
                for(j=0;j<mp['X'];j++)
                    v.pb(6);
                mp['I']-=mp['X'];
                mp['S']-=mp['X'];
                mp['X']=0;

            }
            if(mp['G'])
            {
                for(j=0;j<mp['G'];j++)
                    v.pb(8);
                mp['I']-=mp['G'];
                mp['E']-=mp['G'];
                mp['H']-=mp['G'];
                mp['T']-=mp['G'];
                mp['G']=0;

            }
            if(mp['O'])
            {
                for(j=0;j<mp['O'];j++)
                    v.pb(1);
                mp['N']-=mp['O'];
                mp['E']-=mp['O'];
                mp['O']=0;

            }
            if(mp['V'])
            {
                for(j=0;j<mp['V'];j++)
                    v.pb(7);
                mp['S']-=mp['V'];
                mp['E']-=mp['V'];
                mp['E']-=mp['V'];
                mp['N']-=mp['V'];
                mp['V']=0;

            }
            if(mp['R'])
            {
                for(j=0;j<mp['R'];j++)
                    v.pb(3);
                mp['T']-=mp['R'];
                mp['H']-=mp['R'];
                mp['E']-=2*mp['R'];
                mp['R']=0;

            }
            if(mp['T'])
            {
                for(j=0;j<mp['T'];j++)
                    v.pb(10);

            }
            if(mp['I'])
            {
                for(j=0;j<mp['I'];j++)
                    v.pb(9);

            }

        sort(v.begin(),v.end());
        int l=v.size();
        printf("Case #%d: ",++z);
        for(i=0;i<l;i++)
            cout<<v[i];
        puts("");
        mp.clear();
        v.clear();

    }
}
