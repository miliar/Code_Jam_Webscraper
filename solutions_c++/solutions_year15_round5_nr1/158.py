#include<algorithm>
#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<sstream>
#include<queue>
#include<vector>

using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

vector<long long> salaries, manager;
vector<pair<int,int> > minmaxsal;
vector<vector<int> > employees;
int n, d;
struct leqset {
    int maxl;
    vector<int> c;
    int pref(int n, int l)
    {
        return (n>>(maxl-l))|(1<<l);
    }
    void ini(int ml)
    {
        maxl=ml; c=vector<int>(1<<(maxl+1));
    }
    //inserta c copias de e, si c es negativo saca c copias
    void insertar(int e, int q=1)
    {
        forn(l,maxl+1)
            c[pref(e,l)]+=q;
    }
    int leq(int e)
    {
        int r=0,a=1;
        forn(i,maxl)
        {
            a<<=1;
            int b=(e>>maxl-i-1)&1;
            if (b) r+=c[a]; a|=b;
        }
        return r + c[a]; //sin el c[a] da los estrictamente menores
    }
    int size() { return c[1]; }
    int count(int e) { return c[e|(1<<maxl)]; }
};

leqset ls;

int getSol()
{
    ls.ini(20);
    int j=0,t=0;
    while(j < n && minmaxsal[j].first <= d)
    {
        ls.insertar(minmaxsal[j].second,1);
        j++;
    }
    int res = ls.leq(d);
    int i = 1;
    while(t<n)
    {
        while(t < n && minmaxsal[t].first<i)
        {
            ls.insertar(minmaxsal[t].second,-1);
            t++;
        }
        while(j < n && minmaxsal[j].first<=i+d)
        {
            ls.insertar(minmaxsal[j].second,1);
            j++;
        }
        res = max(res,ls.leq(i+d));
        i++;
    }
    return res;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito = 1; casito <= casos; casito ++)
    {
        long long s0,as,cs,rs,m0,am,cm,rm;
        cin >> n >> d >> s0 >> as >> cs >> rs >> m0 >> am >> cm >> rm;
        manager.resize(n);
        salaries.resize(n);
        manager.resize(n);
        minmaxsal.resize(n);
        salaries[0] = s0;
        minmaxsal[0] = make_pair(s0,s0);
        manager[0] = m0;
        for(int i=1;i<n;i++)
        {
            salaries[i] = (salaries[i-1]*as+cs)%rs;
            manager[i] = (manager[i-1]*am+cm)%rm;
            minmaxsal[i].first = min((int)salaries[i],minmaxsal[manager[i]%i].first);
            minmaxsal[i].second = max((int)salaries[i],minmaxsal[manager[i]%i].second);
        }
        sort(all(minmaxsal));
        cout << "Case #"<< casito <<": "<<getSol() << endl;
    }
}
