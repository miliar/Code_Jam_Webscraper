
#include <cstdio> 
#include <iostream>
#include <string>

using namespace std;

bool check(bool * dig)
{
    bool all = true;
   for (int i = 0; i < 10; i++)
   {
        all = all & dig[i];
    }
    return all;
}
int main()
{
    int T;
    cin >> T;
    int count = 1;
  
    
    while(T--)
    {
        int N;
        cin >> N;
        if (N==0) 
        {
            cout << "Case #" << count++ << ": INSOMNIA" << endl;
        }
        else
        {
            bool dig[10] = {false};
            int c = 1;
            while(true)
            {
                int res = N * c;
                while(res)
                {
                    int d = res % 10;
                    dig[d] = true;
                    res /= 10;       
                }
                if (check(dig))
                {
                    cout << "Case #" << count << ": " << N*c << endl;
                    break;
                } 
                else
                {
                    c++;
                }
           }
            count++;
        }
            
    }
    
}
   
