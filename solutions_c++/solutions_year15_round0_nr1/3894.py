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
    string word;
};

int main()
{
    ios_base::sync_with_stdio(false);
    Application app;
    app.Run();
} 

inline void Application::LoadData()
{
    cin >> size >> word;
}

int Application::Solve()
{
    int result = 0;
    int counter = word[0] - '0';
    
    for(int i = 1; i < word.size(); ++i)
    {   
        if(word[i] - '0' > 0)
        {
            if(counter < i)
            {
                result += i - counter;
                counter = i;
            }
        }
        
        counter += word[i] - '0';
    }
    
    return result;
    
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