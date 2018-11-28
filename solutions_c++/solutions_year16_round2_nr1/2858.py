#include <bits/stdc++.h>

using namespace std;

int hsh[100];
multiset<int> st;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        memset(hsh,0,sizeof(hsh));
        st.clear();

        string s;
        cin>>s;
        int n=s.length();
        cout<<"Case #"<<tt<<": ";
        for(int i=0;i<n;i++)
        {
            char c=s[i];
            hsh[c-'A']++;
        }
        if(hsh[6])
        {
            int hh=hsh[6];
            for(int i=0;i<hh;i++)
            {
             st.insert(8);

             hsh['E'-'A']--;
             hsh['I'-'A']--;
             hsh['G'-'A']--;
             hsh['H'-'A']--;
             hsh['T'-'A']--;
            }
        }
        if(hsh[20])
        {
            int hh=hsh[20];
            for(int i=0;i<hh;i++)
            {
             st.insert(4);
             hsh['F'-'A']--;
             hsh['O'-'A']--;
             hsh['U'-'A']--;
             hsh['R'-'A']--;
            }
        }
        if(hsh[22])
        {
            int hh=hsh[22];
            for(int i=0;i<hh;i++)
            {
             st.insert(2);
             hsh['T'-'A']--;
             hsh['W'-'A']--;
             hsh['O'-'A']--;
            }
        }
        if(hsh[23])
        {
            int hh=hsh[23];
            for(int i=0;i<hh;i++)
            {
             st.insert(6);
             hsh['S'-'A']--;
             hsh['I'-'A']--;
             hsh['X'-'A']--;
            }
        }
        if(hsh[25])
        {
            int hh=hsh[25];
            for(int i=0;i<hh;i++)
            {
             st.insert(0);
             hsh['Z'-'A']--;
             hsh['E'-'A']--;
             hsh['R'-'A']--;
             hsh['O'-'A']--;
            }
        }
        if(hsh[14])
        {
            int hh=hsh[14];
            for(int i=0;i<hh;i++)
            {
             st.insert(1);
             hsh['O'-'A']--;
             hsh['N'-'A']--;
             hsh['E'-'A']--;
            }
        }
        if(hsh[7])
        {

            int hh=hsh[7];
            for(int i=0;i<hh;i++)
            {
             st.insert(3);
             char x='E';
             hsh['T'-'A']--;
             hsh['H'-'A']--;
             hsh['R'-'A']--;
             hsh[x-'A']-=1;
            // cout<<"geting simindies by "<<hsh[x-'A']<<endl;
             hsh[x-'A']-=1;
             //cout<<"geting simindies by "<<hsh[x-'A']<<endl;



            }
        }
        if(hsh[5])
        {
            int hh=hsh[5];
            for(int i=0;i<hh;i++)
            {
             st.insert(5);

             hsh['F'-'A']--;
             hsh['I'-'A']--;
             hsh['V'-'A']--;
             hsh['E'-'A']--;
            }
        }
        if(hsh[21])
        {
            int hh=hsh[21];
            for(int i=0;i<hh;i++)
            {
             st.insert(7);

             hsh['S'-'A']--;
             hsh['E'-'A']--;
             hsh['V'-'A']--;
             hsh['E'-'A']--;
             hsh['N'-'A']--;
            }
        }
        if(hsh[4])
        {
            int hh=hsh[4];
            for(int i=0;i<hh;i++)
            {
             st.insert(9);

             hsh['N'-'A']--;
             hsh['I'-'A']--;
             hsh['N'-'A']--;
             hsh['E'-'A']--;
            }
        }

        multiset<int> :: iterator it;
        for(it=st.begin();it!=st.end();it++)
            cout<<*it;

            cout<<endl;

    }
}
