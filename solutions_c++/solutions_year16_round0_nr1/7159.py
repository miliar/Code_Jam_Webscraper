#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
    int T =0;
    string N;
    ifstream inF(argv[1]);

    inF >> T;
    
    for(int i = 0; i < T; i++)
    {
        inF>> N;
        int mult = 0;
        int prod = 0;
        int carry = 0;
        int count = 0;
        int size  = N.size();
        string lastMult;
        bool exist[10] = {0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0};
        
        if(size == 1 && N[0]=='0')
        {
            cout << "Case #" << i+1 <<": INSOMNIA" << endl;
            continue;
        }
        
        while(count != 10)
        {
            carry = 0;
            ++mult;
            lastMult.clear();
            for(int j = size-1; j >= 0; --j )
            {
                prod = (N[j] - '0')*mult + carry;
                carry = prod/10;
                prod  = prod%10;
                if(0 == exist[prod])
                {
                    exist[prod] = 1;
                    ++count;
                }
                lastMult+= (char)(prod+'0');
            }
            
            while(carry != 0)
            {
                prod = carry%10;
                carry = carry/10;
                if(0 == exist[prod])
                {
                    exist[prod] = 1;
                    ++count;
                }
                lastMult+= (char)(prod+'0');
            }
        }
        reverse(lastMult.begin(), lastMult.end());
        cout << "Case #" << i+1 <<": " << lastMult<< endl;
    }
   return 0;
}

