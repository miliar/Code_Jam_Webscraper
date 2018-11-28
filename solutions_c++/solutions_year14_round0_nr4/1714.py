#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <iomanip>
#include <queue>
#include <deque>
#include <algorithm>
#include <cstring>

using namespace std;

typedef pair<int, int> pie;
#define L first
#define R second
#define MP make_pair
#define PB push_back
double a[10000], b[10000];
set<double> s;
main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("D-large.in");
    ofstream cout("D-large.out");
    int t, num = 0;
    cin>>t;
    while(t--){
        int n, ans = 0;
        cin>>n;
        for(int i=1;i<=n;i++)
            cin>>a[i];
        for(int i=1;i<=n;i++){
            cin>>b[i];
            s.insert(b[i]);
        }
        sort(a+1, a+n+1);
        sort(b+1, b+n+1);
        int ret = 0;
        for(int i=1;i<=n;i++){
            if(s.lower_bound(a[i]) == s.end())
                ret++;
            else
                s.erase(s.lower_bound(a[i]));
        }
        s.clear();
        int lo = 1, l = 1;
        for(int i=1;i<=n;i++){
            if(a[lo] > b[l])
                ans++, lo++, l++;
            else
                lo++;
        }

        num++;
        cout<<"Case #"<<num<<": "<<ans<<" "<<ret<<endl;
    }
}
