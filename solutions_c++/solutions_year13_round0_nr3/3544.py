/*
 *  easyFairAndSquare.cpp
 *  Google_Jam
 *
 *  Created by Hugo Manet on 13/04/13.
 *  Copyright 2013 __MyCompanyName__. All rights reserved.
 *
 */

using namespace std;

//*
#include <iostream>
/*/
#include <fstream>

ifstream fcin("/Users/hugo/Downloads/C-small-attempt0.in.txt");
ofstream fcout("/Users/hugo/Downloads/C-small-attempt0.out.txt");

#define cin fcin
#define cout fcout
//*/

#define in(n) ((A <= n && n <= B)? 1:0)

int main()
{
    int     N;
    cin>>   N;
    
    for (int i = 1; i <= N; i++)
    {
        int     A,  B;
        cin>>   A>> B;
        
        cout << "Case #" << i << ": " << in(1) + in(4) + in(9) + in(121) + in(484) << '\n';
    }
}
