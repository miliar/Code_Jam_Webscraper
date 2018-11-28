#include <iostream> 
#include <vector> 
#include <queue> 
#include <string> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <iomanip> 
#include <sstream> 
#include <algorithm> 
#include <map> 
#include <set> 
#include <fstream>
using namespace std;

typedef long long LL;

string name;
int n;

bool isVowel(char ch)
{
    return (ch == 'a') || (ch == 'e') || (ch == 'i') || (ch == 'o') || (ch == 'u');     
}

void solve()
{
    LL ans = 0;
    
    int len = name.size();
    
    int balance = 0;
    
    int rightSt = -1;
    for (int i = 0; i < len; i++)
    {
        char ch = name[i];
        if (!isVowel(ch))
        {
            balance++;
            if (balance >= n) rightSt = i - n + 1;
        }   
        else
        {
            balance = 0;
        }
        
        ans += rightSt + 1;
    }
    
    cout << ans << endl;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> name >> n;
        
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}
