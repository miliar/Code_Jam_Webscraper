#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<string> answer;

void getStrings( string s, long long int digitsLeft )
{
   if( digitsLeft == 0 )
      answer.push_back( "1" + s + "1" );
   else
   {
      getStrings( s + "0", digitsLeft - 1 );
      getStrings( s + "1", digitsLeft - 1 );
   }
}

long long int isNotPrime(long long int n)
{
    long long int i, f = 0;
    for(i = 2; i <= sqrt(n); i++)
    {
        if(n % i == 0)
        {
            f = 1;
            break;
        }
    }
    if(f == 0)
        return 0;
    else
        return i;
}


long long int baseN(string str, long long int n)
{
    long long int x, j = 0, sum = 0;
    
    for (std::string::reverse_iterator rit=str.rbegin(); rit!=str.rend(); ++rit) {
        x = (long long int) pow(n, j);
        if((*rit) == '1')
            sum += x;
        j++;
    }
    return sum;
}
 
int main() {
    long long int f, i, j, divisor, count = 0, n, t;
    cin >> t;
    cin >> n >> j;
    getStrings( "", n - 2);
    cout << "Case #1:\n";
    for (std::vector<string>::iterator it = answer.begin() ; it != answer.end(); ++it)
    {
        f = 0;
        vector<long long int> vec;
        for(i = 2; i <= 10; i++)
        {
            divisor = isNotPrime(baseN(*it, i));
            if(!(divisor ? 1 : 0))
            {
                f = 1;
                break;
            }
            vec.push_back(divisor);
        }
        
        if(f == 0)
        {
            if(vec.size() == 9 && count < j)
            {
                count++;
                cout << (*it) << " ";
                for (std::vector<long long int>::iterator iti = vec.begin() ; iti != vec.end(); ++iti)
                {
                    cout << *iti << " ";
                }
                cout << endl;
            }
        }
    }
}