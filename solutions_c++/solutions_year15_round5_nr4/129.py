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

int n;
vector<int> nums,freqs,res;
multiset<int> multint;

void borrar(int mask, int t)
{
    forn(i,res.size())
    if((mask>>i)%2==1)
    {
        t+= res[i];
    }
    multint.erase(multint.find(t));
    return;
}

void borrarTodasLasCombinaciones()
{
    for(int i=1;i<(1<<(res.size()-1));i++)
        borrar(i,res[res.size()-1]);
    return;
}

void solve()
{
    res.clear();
    multint.clear();
    int t = 0;
    forn(i,n)
    {
        forn(j,freqs[i])
        {
            t++;
            if(nums[i]!=0 || j != 0)
                multint.insert(nums[i]);
        }
    }
    if(t == 2)
    {
        res.push_back(nums[nums.size()-1]);
        return;
    }
    n=2;
    while((1<<n)<t)
        n++;
    res.push_back(*multint.begin());
    multint.erase(multint.begin());;
    res.push_back(*multint.begin());
    multint.erase(multint.begin());
    while(res.size()<n)
    {
        borrarTodasLasCombinaciones();
        res.push_back(*multint.begin());
        multint.erase(multint.begin());
    }
    return;
}

int main()
{
	freopen("D-small.in","r",stdin);
	freopen("D.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito = 1; casito <= casos; casito ++)
    {
        cin >> n;
        nums.resize(n);
        freqs.resize(n);
        forn(i,n)
            cin >> nums[i];
        forn(i,n)
            cin >> freqs[i];
        cout << "Case #"<< casito <<":";
        solve();
        forn(i,res.size())
            cout<<" " << res[i];
        cout<< endl;
    }
}
