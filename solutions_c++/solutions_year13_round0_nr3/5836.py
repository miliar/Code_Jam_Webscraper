#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

bool isPali(int num)
{
    int n = num;
    int rev = 0;
    int dig = 0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if (n==rev) return true;
    else return false;
}

int main ()
{ 
    ofstream answer;
    answer.open ("answer.txt");
    
    ifstream input( "input.txt" );
    if (!input) cout << "file not read";
    int cases;
    input >> cases;
    size_t count = 0;
    for (size_t i = 0; i < cases; ++i)
    {
        int a, b;
        input >> a >> b;
                
        while(a <= b)
        {
            int root = sqrt(a);
            if(pow(root,2) == a)
            {
                if(isPali(a) && isPali(root))
                {
                    count++;
                }
            }
            ++a;
        }
        
        answer << "Case #" << i+1 << ": " << count << endl;
        count = 0;
    }
    
    answer.close();
}