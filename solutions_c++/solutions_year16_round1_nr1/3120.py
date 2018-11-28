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
#define arsize 1000000001
#define INF 0x3f3f3f3f
#define NINF INT_MIN
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define size 1000000
using namespace std;
ofstream fout ("/Users/priya/Desktop/A-large.out");
ifstream fin ("/Users/priya/Desktop/A-large.in");
// int a, b;
// fin >> a >> b;
// fout << a+b << endl;
//  freopen("in", "r", stdin);
//  freopen("out", "w", stdout);
int main()
{
    int t; fin>>t; for(int j=0;j<t;j++)
    {
        string s; fin>>s;
        string ans;
        for(int i=0;i<s.length();i++)
        {
            if(ans.empty())
            {
                ans=s[i];
            }
            else if(s[i]>=*ans.begin())
            {
                ans=s[i]+ans;
            }
            else{
                ans=ans+s[i];
            }
        }
        fout<<"Case #"<<j+1<<":"<<" "<<ans<<endl;
    }
    return 0;
}