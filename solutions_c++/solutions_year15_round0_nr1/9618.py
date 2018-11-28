#include <iostream>
#include <fstream>
#include <iomanip>
#include <set>
#include <map>
//#include <unordered_map>
//#include <unordered_set>
#include <vector>
#include <string>
#include <queue>
#include <stack>
//#include <array>
#include <algorithm>
#include <cmath>
//QMAKE_CXXFLAGS += -std=c++11
//#pragma comment(linker, "/STACK:1000000")
 
 
#define pb push_back
#define mp make_pair
 
using namespace std;



const long double EPS = 1e-5;
const long long MAXN = (int) 1 + 5e5;
const int INF = (int) 128;




int main()
{
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    
    
    int n, k;
    string temp; temp.reserve(1001);
    
    cin >> k;
    
    for (int j = 1; j <= k; ++j)
    {
        temp.clear();
        
        cin >> n >> temp;
        
        int p = temp[0] - 48, ans = 0;
        
        for (int i = 1; i <= n; ++i)
        {
            ans += max(i - p, 0);
            p += max(i - p, 0) + temp[i] - 48;
        }
        
        cout << "Case #" << j << ": " << ans << endl;
    }
    
    
    
    return 0;
}

































