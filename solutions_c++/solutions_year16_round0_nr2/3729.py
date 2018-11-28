#include <bits/stdc++.h>

#define REP(i,x) for(uint32 i = 0 ; i < (x) ; i++)

//#define DEBUG_MODE
#ifdef DEBUG_MODE
#define print(x) cout << #x << " = " << x << endl
#define debug(x) x
#else
#define print(x)
#define debug(x)
#endif

#define hash_map      unordered_map
#define hash_multimap unordered_multimap
#define hash_set      unordered_set
#define hash_multiset unordered_multiset

using namespace std;

typedef short int int16;
typedef unsigned short int uint16;
typedef int int32;
typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;

typedef pair <int, int> PII;
typedef pair <uint32, uint32> PUU;
typedef pair <uint32, int> PUI;
typedef pair <int, uint32> PIU;
typedef pair <int64, int64> PLL;
typedef pair <int64, int> PLI;
typedef pair <int, int64> PIL;
typedef pair <int, int16> PIS;
typedef pair <int16, int> PSI;

constexpr int UNDEF = -1;

class Application
{
public:
    inline void Run();
private:
    // Methods
    inline void LoadData();
    inline void Solve();
    inline void Clear();
    // Fields
    string content;
    int TS;
};

int main()
{
    ios_base::sync_with_stdio(false);
    Application app;
    app.Run();
}

inline void Application::LoadData()
{
    cin >> content;
}

inline void Application::Solve()
{
    char last_sign = '+';
    int minus_group_no = 0;
    
    for(auto it : content)
    {
        if(it == '-' && last_sign != it)
            ++minus_group_no;
        
        last_sign = it;
    }  
    
    int result = minus_group_no * 2;
    
    if(content.front() == '-')
        -- result;
    
    cout << "Case #" << TS << ": " << result << "\n"; 
}

inline void Application::Clear()
{
    
}

inline void Application::Run()
{
    uint32 test_number;
    cin >> test_number;
    
    for(TS = 1; TS <= test_number; ++TS)
    {
        LoadData();
        Solve();
        Clear();
    }
}
