# include <string> 
# include <vector> 
# include <iostream> 
# include <sstream> 
# include <cstdio> 
# include <cstdlib> 
# include <cmath> 
# include <cctype> 
# include <cstring> 
# include <map> 
# include <queue> 
# include <deque> 
# include <set> 
# include <algorithm> 
# include <utility> 
# include <functional> 
# include <stack> 
# include <bitset> 
# include <complex> 
# include <cassert> 
# include <ctime> 
# include <list> 
# include <valarray> 
#include <unordered_set>

using namespace std;

typedef long long ll;

int test(int n)
{
    if(n == 0)
        return -1;
        
    unordered_set<int> set;
    
    ll N = n;
    
    int i = 1;
    
    while(true)
    {
        ll current = i * N;
        
        while(current != 0)
        {
            set.insert(current%10);
            current /= 10;
        }
        
        if(set.size() == 10)
            return i * N;
        
        i++;
    }
    return -1;
}
int main()
{
	int t;
    cin >> t;
    
    int index = 1;
    while(--t>=0)
    {
        int n;
        cin >> n;
        
        int res = test(n);
        cout << "Case #" << index++ << ": ";
        
        if(res == -1)
            cout << "INSOMNIA" << endl;
        else cout << res << endl;
    }
	return 0;
}

