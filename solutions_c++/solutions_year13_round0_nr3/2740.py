//
//  main.cpp
//  QualifsFairAndSqare
//
//  Created by MrAaaah on 12/04/13.
//  Copyright (c) 2013 MrAaaah. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

bool isPalindrome(int x) {
    int reverse = 0, temp;
    
    temp = x;
    
    while(temp != 0)
    {
        reverse = reverse * 10;
        reverse = reverse + temp % 10;
        temp = temp / 10;
    }
    
    return x == reverse;
}

int main(int argc, const char * argv[])
{
    int cases, a, b, sqrtA, sqrtB, cpt;
	cin >> cases;

	for (int c = 1; c <= cases; ++c)
	{
        cpt = 0;
		cin >> a; cin >> b;
        
        sqrtA = ceil(sqrt(a)); sqrtB = floor(sqrt(b));
        
        for (int n = sqrtA; n <= sqrtB; ++n) {
            if (isPalindrome(n)) {
                if (isPalindrome(n*n)) {
                    cpt++;
                }
            }
        }
        
		cout << "Case #" << c << ": " << cpt << endl;
	}
	
    return 0;
}

