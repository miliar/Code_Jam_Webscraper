#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <cmath>
using namespace std;
typedef long long ll;
const int MAX_HEIGHT = 100;
void printSuc(int i)
{
    cout<<"Case #"<<i+1<<": YES\n";
}
void printFail(int i)
{
    cout<<"Case #"<<i+1<<": NO\n";
}
int main()
{
	FILE* fin=freopen("B-large.in","rt",stdin);
	FILE* fout=freopen("B-large.out","wt",stdout);
    int t;
    std::cin>>t;
    vector<ll> v;
    for(int zz=0;zz<t;zz++)
    {
        int n,m;
        cin>>n>>m;
        vector<vector<int> > v;
        for(int i=0;i<n;i++)
        {
            vector<int> tmp;
            for(int j=0;j<m;j++)
            {
                int t;
                cin>>t;
                tmp.push_back(t);
            }
            v.push_back(tmp);
        }
//        for(int i=MAX_HEIGHT-1;i>=0;i--)
//        {
//            for(int j=0;j<n;j++)
//            {
//                for(int k=0;k<m;k++)
//                {
//                    if (i==v[j][k])
//                }
//            }
//        }
        bool fail=false;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if (v[i][j] != MAX_HEIGHT)
                {
                    int l=v[i][j];
                    int cnt1=0;
                    for(int k=0;k<n;k++)
                    {
                        if (l >= v[k][j])
                        {
                            cnt1++;
                        }
                    }
                    int cnt2=0;
                    for(int k=0;k<m;k++)
                    {
                        if (l >= v[i][k])
                        {
                            cnt2++;
                        }
                    }
                    if (cnt2!=m && cnt1 != n)
                    {
                        fail=true;
                        break;
                    }
                }
            }
            if (fail)
                break;
        }
        if (fail)
            printFail(zz);
        else
            printSuc(zz);

    }
//    fclose(fout);
//    fclose(fin);
    return 1;
}