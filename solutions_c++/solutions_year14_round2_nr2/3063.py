#include <iostream>
#include <string>
#include <map>

using namespace std;

int process();

int main()
{
    int test;
    cin >> test;
    int i; // loop variable
    double result[test]; // results for each case
    for ( i = 0 ; i < test; i++)
    {
        result[i]=process();
    }
    
    //print results
    for (i = 0 ; i < test; i++)
    {
        cout << "Case #" << (i+1) << ": " << result[i] << "\n";
    }
    return 0;
}

int process ()
{
    long A,B,C;
    long count = 0;
    cin >> A >> B >> C;
    for ( long i = 0 ; i < A ; i++)
    {
        for (long j = 0 ; j < B ; j ++)
        {
            long ans = i & j;
            if (ans < C)
            {
                count ++ ;
            }
        }
    }
    return count;
}