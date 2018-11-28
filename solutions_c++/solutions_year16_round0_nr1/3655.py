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
    int64 number;
    int64 original_number;
    int TN = 0;
};

int main()
{
    ios_base::sync_with_stdio(false);
    Application app;
    app.Run();
}

inline void Application::LoadData()
{
    cin >> original_number;
  
}

inline void Application::Solve()
{
    if(original_number == 0)
    {
         cout << "Case #" << TN << ": INSOMNIA\n"; 
         return;
    }
    
    vector <bool> occured(10, false);
    int64 occured_no = 0;
    number = original_number;
    
    
    while(occured_no < 10)
    {
        int64 temp = number;
        
        while(temp > 0)
        {
            int64 digit = temp % 10;
            temp /= 10;
            if(!occured[digit])
            {
                ++occured_no;
                occured[digit] = true;
            }
        }
        
        number += original_number;
    }
   
    
    cout << "Case #" << TN << ": " << number - original_number<< "\n"; 
}   

inline void Application::Clear()
{
    
}

inline void Application::Run()
{
    uint32 test_number;
    cin >> test_number;
    
    for(TN = 1; TN <= test_number; ++TN)
    {
        LoadData();
        Solve();
        Clear();
    }
}
