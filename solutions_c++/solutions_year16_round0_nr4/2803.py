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

using namespace std;
typedef unsigned long long ull;


void work(ull K, ull C, ull S)
{
    if(K == 1)
    {
        cout << " 1" << endl;
        return;
    }
    if(C == 1)
    {
        for(int i = 1; i <= K; i++)
        {
            cout << " " << i;
        }
        cout << endl;
        return;
    }
    cout << " " << 1;
    
    for(ull k = 2; k <= K; k++ )
    {
        ull current_location = k;
        
        for(ull c = 2; c <= C; c++)
        {
            current_location = (current_location - 1) * K + k; 
        }
        cout << " " << current_location;
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    
    int index = 1;
    while(--t>=0)
    {
        ull K, C, S;
        cin >> K >> C >> S;
        
        cout << "Case #" << index++ << ":";
        work(K,C,S);
    }
	return 0;
}

