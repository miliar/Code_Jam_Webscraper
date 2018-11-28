#include <bits/stdc++.h>

using namespace std;

typedef long long int64;

const int INF = 1000000001;
const int UNDEF = -1;

class Application
{
public:
    inline void Run();    
private:
    // Methods
    inline void LoadData();
    inline int Solve();
    // Fields
    
    int size;
    vector <int> a;
    int max_value;
};

int main()
{
    ios_base::sync_with_stdio(false);
    Application app;
    app.Run();
}

inline void Application::LoadData()
{
    cin >> size;
    a.resize(size);
    max_value = UNDEF;
   
    
    for(int i = 0; i < size; ++i)
    {
        cin >> a[i];
        max_value = max(max_value, a[i]);
    }
}

int Application::Solve()
{
    int best_result = INF;
    sort(a.begin(), a.end());
    
    for(int i = max_value; i >= 1; --i)
    { 
        int temp_result = 0;
        
        for(int j = size - 1; j >= 0; --j)
        {
            if(a[j] > i)
            {
                temp_result += ((a[j] / i) - 1);
                
                if(a[j] % i != 0)
                    ++temp_result;
            }
            else
                break;

        }
        
        temp_result += i;
        
        if(temp_result < best_result)
            best_result = temp_result;
    }
    
    
    return best_result;
}

inline void Application::Run()
{ 
    int test_number;
    cin >> test_number;
    for(int i = 0; i < test_number; ++i)
    {
        LoadData();
        cout << "Case #" << i + 1 << ": ";
        cout << Solve();
        cout << "\n";
    }
}