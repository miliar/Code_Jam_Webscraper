#include <bits/stdc++.h>

#define REP(i,x) for(uint32 i = 0 ; i < (x) ; i++)

#define DEBUG_MODE
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


int64 PowModulo(int64 a, uint32 n, int64 modulo)
{
      int64 result = 1;
      while(n)
      {
              if(n % 2)
              {
                      result *= a;
                      result %= modulo;
              }
              n /= 2;
              a *= a;
              a %= modulo;
      }
      return result;
}

bool MillerRabin(uint64 p)
{
      if(p < 2)
              return false;
      uint64 tests[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41};
      int i = 0;
        for(; i < 13; ++i)
              if(p == tests[i])
                      return true;
      uint64 kk = p - 1;
      while( kk % 2 == 0 )
              kk /= 2;

      for(i = 0; i < 13; ++i)
      {
              uint64 k = kk;
              uint64 d = tests[i];
              uint64 x = PowModulo(d, k, p);
              if( x == 1 || x == (p - 1) )
                      continue;
              while(k < p - 1)
              {
                      x = (x * x) % p;
                      if(x == (p - 1))
                              break;
                      else if(x == 1)
                              return false;
                      k *= 2;
              }
              if(x != p - 1)
                      return false;
      }
      return true;
}



class Application
{
public:
    inline void Run();
private:
    // Methods
    inline void LoadData();
    inline void Solve();
    inline void Clear();
    inline bool IsJamNumber();
    
    
    void GenerateAllNumber();
    void PrintResult(int pos);
    void PrintDivisors(int pos);
    
    
    // Fields
    vector <bool> number;
    vector < vector <bool > > result;
    vector < vector <int> > true_result;
    int64 TN;
    
    int64 n = 16;
    int64 j = 32;
    int64 pos;
};

int main()
{
    ios_base::sync_with_stdio(false);
    Application app;
    app.Run();
}

void Application::PrintResult(int pos)
{
    for(auto it : result[pos])
        cout << it;
    
    cout << " ";
}

void Application::PrintDivisors(int pos)
{
    for(auto it : true_result[pos])
    {
        cout << it << " ";
    }
    
    cout << "\n";
}


inline bool Application::IsJamNumber()
{
    for(int64 base = 2; base <= 10; ++base)
    {
        int64 no = 0;
        int64 act_pow = 1;
        
        for(int64 i = number.size() - 1; i >= 0; --i)
        {
            if(number[i])
                no += act_pow;
            act_pow *= base;
        }
        
        if(MillerRabin(no))
        {       
            return false;
        }
    
    }
    

    true_result.push_back(vector <int>());
    for(int64 base = 2; base <= 10; ++base)
    {
        int64 no = 0;
        int64 act_pow = 1;
        
        for(int64 i = number.size() - 1; i >= 0; --i)
        {
            if(number[i])
                no += act_pow;
            act_pow *= base;
        }
        
        int no_sqrt = sqrt(no) + 1;
      
        bool OK = false;
        for(int i = 2; i < no_sqrt; ++i)
        {
            if(no % i == 0)
            {
                true_result.back().push_back(i);
                OK = true;
                break;
            }
        }
        
        if(!OK)
        {
            true_result.pop_back();
            return false;
        }
    }
    
    return true;
}

void Application::GenerateAllNumber()
{
    if(pos == n - 1)
    {
        number[pos] = true;
        if(IsJamNumber())
            result.push_back(number);
    }
    else
    {   

        number[pos] = true;
        
        ++ pos;
        GenerateAllNumber();
     
        if(result.size() == j)
            return;
                
        -- pos;
        number[pos] = false;
         
        ++pos;

        GenerateAllNumber();
    
        if(result.size() == j)
            return;

        --pos;
    }
}

inline void Application::LoadData()
{
    cin >> n >> j;
    
    number.resize(n);
    number[0] = true;
    pos = 1;
    
    GenerateAllNumber();
}

inline void Application::Solve()
{
    cout << "Case #1:\n";

    
    REP(i, result.size())
    {
        PrintResult(i);
        PrintDivisors(i);
    }
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
