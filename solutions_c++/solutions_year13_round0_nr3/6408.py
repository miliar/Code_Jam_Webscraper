#include <iostream>
#include <sstream>
#include <string>

using namespace std;

bool ispalindrom(unsigned long long x)
{
    stringstream ss;
    string a ,b;
    ss << x;
    ss >> a;
    b = string( a.rbegin(), a.rend());
    if(a==b)
        return true;
        else return false;
}        


int main()
{
    int n;
    cin >> n;
    unsigned long long a, b;
    int count;
    for(int i = 0; i<n;i++)
    {
        count = 0;
        cin >> a >> b;
        for(int k = 1 ; k<=b; k++)
        {
            if(ispalindrom(k))
                if(ispalindrom(k*k) && k*k >=a && k*k <= b)
                    count ++;
        }
        
        cout << "Case #" << i+1 << ": " << count << "\n";
     }
return 0;
}                    
                
                
                
                
                
                
            
