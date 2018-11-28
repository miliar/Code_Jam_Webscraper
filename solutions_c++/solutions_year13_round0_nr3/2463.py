#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
bool pal(long long i)
{
    vector<long long> v;
    while (i>0)
    {
        v.push_back(i%10);
        i/=10;
    }
    for (i=0;i<v.size()/2;++i)
    {
        if (v[i]!=v[v.size()-i-1])
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    ifstream cin ("C-large-1.in");
    ofstream cout("output.txt");
    long long n, a, b, i;
    cin>>n;
    vector<pair<long long, long long> > in;
    vector<long long> v;
    for (i=0;i<n;++i)
    {
        cin>>a>>b;
        in.push_back(make_pair(a, b));
        v.push_back(a-1);
        v.push_back(b);
    }
    sort(v.begin(), v.end());
    long long max_el=v[2*n-1], j=0, r=0;
    map<long long, long long> m;
    for (i=0;true;++i)
    {
        while (v[j]<i*i && j<2*n)
        {
            m[v[j]]=r;
            ++j;
        }
        if (j==2*n)
        {
            break;
        }
        if (!pal(i) || !pal(i*i))
        {
            continue;
        }
        //cout<<i<<" "<<i*i<<endl;
        ++r;
        while (v[j]==i*i && j<2*n)
        {
            m[v[j]]=r;
            ++j;
        }
    }
    for (i=0;i<n;++i)
    {
        cout<<"Case #"<<i+1<<": "<<m[in[i].second]-m[in[i].first-1]<<endl;
    }
    return 0;
}
