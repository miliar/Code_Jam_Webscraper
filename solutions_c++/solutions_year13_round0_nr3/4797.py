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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>
#define ll long long
using namespace std;

bool pal(int n)
{
    int a;
    stringstream ss;
    ss << n;
    string s = ss.str();
    reverse(s.begin(),s.end());
    stringstream ss1(s);
    ss1 >> a;
    if(a == n)
        return true;
    else
        return false;

}

int main () {
   freopen("C-small-attempt0.in", "r", stdin);
freopen("output.txt", "w", stdout);
   int t,c=0,n,m,flag=0;
    cin >> t;
    for(int k=0;k<t;k++){
        c = 0;
        cin >> n>>m;
        cout<<"Case #"<<k+1<<": ";
        for(int i = n;i<=m;i++){
            if(pal(i)){
                int d  = sqrt(i);
                if(d*d == i && pal(d))
                    c++;
            }
        }
        cout<<c<<endl;
    }
  return 0;
}
