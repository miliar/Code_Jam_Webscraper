#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <cstring>
#include <climits>
#include <iostream>
#include <cassert>
#define mod 1000000007
#define eps 1e-4
#define arsize 1000000000
#define INF 0x3f3f3f3f
#define NINF INT_MIN
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define size 1000001
#define fi(i,n) for(int i=0; i<(int)(n); ++i)
#define fii(i,u,n) for(int i=(int)(u); i<(int)(n); ++i)
#define fl(i,n) for(long int i=0; i<(long int)(n); ++i)
#define fli(i,u,n) for(long int i=(long int)(u); i<(long int)(n); ++i)
#define each(it,o) for(aut(it,0.begin()); it!=o.end(); ++it)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define mset(m,v) memset(m,v,sizeof(m))
#define edge pair<int,int>
typedef long int li;
typedef long long int lli;
using namespace std;
/*ofstream fout ("test.out");
 ifstream fin ("test.in");
 int a, b;
 fin >> a >> b;
 fout << a+b << endl;*/
int main()
{
    ifstream fin("/Users/priya/Desktop/B-large.in");
    ofstream fout("/Users/priya/Desktop/B-large.out");
    long int t; fin>>t;
    for(long int i=1;i<=t;++i)
    {
        string s; fin>>s; bool onlyplus=1,onlyminus=1;
        for(int j=0;j<s.length();++j)
        {
            if(s[j]=='+') onlyminus=0;
            if(s[j]=='-') onlyplus=0;
        }
        if(onlyminus) fout<<"Case #"<<i<<":"<<" "<<"1"<<endl;
        else if(onlyplus) fout<<"Case #"<<i<<":"<<" "<<"0"<<endl;
        else
        {
            long int count1=0, count2=0;
            if(s[0]=='+')
            {
            for(int i=1;i<s.length();++i)
                if((s[i]=='-')&&(s[i-1]=='+'))
                    count2++;
            }
            else if(s[0]=='-')
            {
                count1++;
                for(int i=1;i<s.length();++i)
                    if((s[i]=='-')&&(s[i-1]=='+'))
                        count2++;
            }
            fout<<"Case #"<<i<<":"<<" "<<2*count2+count1<<endl;
        }
    }
    return 0;
}