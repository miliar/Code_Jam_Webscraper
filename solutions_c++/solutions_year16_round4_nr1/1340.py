#include <bits/stdc++.h>
using namespace std;
int test;
int n, r, p, s;
int rdb, pdb, sdb;
vector<char> z, sss;
vector<char> start(vector<char> z)
{
    if(z.size()==(1<<n)) return z;
    vector<char> x;
    for(int i=0; i<z.size(); i++)
    {
        if(z[i]=='P')
        {
            x.push_back('P');
            x.push_back('R');
        }
        else if(z[i]=='R')
        {
            x.push_back('R');
            x.push_back('S');
        }
        else
        {
            x.push_back('P');
            x.push_back('S');
        }
    }
    return start(x);
}
vector<char> rendez(vector<char> z, int k)
{
    if(k==z.size()) return z;
    for(int i=0; i<z.size(); i+=(2*k))
    {
        int x=i;
        int y=i+(k);
        int ki=1;
        for(int l=0; l<(k); l++)
        {
            if(z[x+l]<z[y+l]) break;
            else if(z[x+l]>z[y+l])
            {
                ki=2;
                break;
            }
        }
        if(ki==2)
        {
            for(int l=0; l<(k); l++)
            {
                swap(z[x+l], z[y+l]);
            }
        }
    }
    return rendez(z, 2*k);
}
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cout<<"Case #"<<tt<<": ";
        cin>>n;
        cin>>r>>p>>s;
        z.clear();
        z.push_back('P');
        sss=start(z);
        rdb=0;
        pdb=0;
        sdb=0;
        for(int i=0; i<sss.size(); i++)
        {
            if(sss[i]=='P') pdb++;
            else if(sss[i]=='R') rdb++;
            else sdb++;
        }
        if(p==pdb && r==rdb && s==sdb)
        {
            sss=rendez(sss, 1);
            for(int i=0; i<sss.size(); i++)
            {
                cout<<sss[i];
            }
            cout<<endl;
            continue;
        }

        z.clear();
        z.push_back('R');
        sss=start(z);
        rdb=0;
        pdb=0;
        sdb=0;
        for(int i=0; i<sss.size(); i++)
        {
            if(sss[i]=='P') pdb++;
            else if(sss[i]=='R') rdb++;
            else sdb++;
        }
        if(p==pdb && r==rdb && s==sdb)
        {
            sss=rendez(sss, 1);
            for(int i=0; i<sss.size(); i++) cout<<sss[i];
            cout<<endl;
            continue;
        }

        z.clear();
        z.push_back('S');
        sss=start(z);
        rdb=0;
        pdb=0;
        sdb=0;
        for(int i=0; i<sss.size(); i++)
        {
            if(sss[i]=='P') pdb++;
            else if(sss[i]=='R') rdb++;
            else sdb++;
        }
        if(p==pdb && r==rdb && s==sdb)
        {
            sss=rendez(sss, 1);
            for(int i=0; i<sss.size(); i++) cout<<sss[i];
            cout<<endl;
            continue;
        }

        cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
