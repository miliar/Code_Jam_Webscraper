#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<string>
#include<vector>
#include<cstring>

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

vector<string> vec;
int m,n;
vector<int> shard;
int res;
int mapa[1024];

int calc2(vector<string> vecs)
{
    int res = 1;
    for(int i=0;i<vecs.size();i++)
    forn(t,vecs[i].size()+1)
    {
        if(t==0)
            continue;
        bool b = true;
        forn(j,i)
        {
            if(vecs[j].size()>=t && vecs[i].substr(0,t) == vecs[j].substr(0,t))
            {
                b = false;
            }
        }
        if(b==true)
            res++;
    }
    return res;
}

int calc()
{
    int res = 0;
    forn(i,n)
    {
        vector<string> vecs;
        forn(j,m)
        if(shard[j]==i)
            vecs.push_back(vec[j]);
        if(vecs.empty())
            return 0;
        res += calc2(vecs);
    }
    return res;
}

void go(int pos)
{
    if(pos == m)
    {
        forn(i,n)
        {
            bool b = false;
            forn(j,m)
            if(shard[j]==i)
                b = true;
            if(b==false)
                return;
        }
        int t = calc();
        mapa[t]++;
        return;
    }
    shard.push_back(0);
    forn(i,n)
    {
        shard[pos] = i;
        go(pos+1);
    }
    shard.pop_back();
    return;
}
int main()
{
	freopen("D-small.in","r",stdin);
	freopen("D.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito=1;casito<=casos;casito++)
    {
        cin >> m >> n;
        memset(mapa,0,sizeof(mapa));
        vec.resize(m);
        forn(i,m)
        {
            cin >> vec[i];
        }
        go(0);
        int res = 1000;
        while(mapa[res] == 0)
            res--;
        cout << "Case #"<< casito <<": "<< res <<" "<< mapa[res] << endl;
    }
}
