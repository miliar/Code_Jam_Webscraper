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

main()
{
    ios_base::sync_with_stdio(false);
    int t, num = 0;
    ifstream cin("B-large.in");
    ofstream cout("B-large.out");
    cin>>t;
    while(t--){
        num++;
        double C, F, X;
        cin>>C>>F>>X;
        cout<<"Case #"<<num<<": ";
        double ans = X/2.00000, MS = 2.00000;
        double cur = 0.000000;
        for(int i=1;i<=X;i++){
            cur += C/MS;
            MS += F;
            ans = min(ans, (X/MS) + cur);
        }
        cout<<fixed<<setprecision(7)<<ans<<endl;
    }
}
