/*
1 ≤ T ≤ 100.
Small dataset

0 ≤ Smax ≤ 6.

Large dataset

0 ≤ Smax ≤ 1000.

Input 
    
Output 
 
4
4 11111
1 09
5 110011
0 1

Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0

num = 0;
if 0 :
    true
    num += input;
else 
    if( num >= i )
        num += input;
    
*/

#include<iostream>
#include<stdlib.h>

using namespace std;
int main()
{
    unsigned int test = 0;
    cin >> test;
    for( unsigned int j = 0; j < test; j++ )
    {
        unsigned int tot = 0, needPeople = 0, num = 0;
        cin >> tot;

        char ch;
        scanf( "%c", &ch );

        for( unsigned int i = 0; i <= tot; i++ )
        {
            int input = 0;
            char ch;
            scanf( "%c", &ch );
            input = atoi( &ch );
            
            //cout << "input" << input << endl;
            if( i == 0 )
                num += input;
            else
            {
                if( num >= i )
                    num += input;
                else
                {
                    needPeople += ( i - num );
                    num += ( i - num );
                    num += input;
                }
            }
        }
        cout << "Case #" << j+1 << ": " << needPeople << endl;
    }
}
