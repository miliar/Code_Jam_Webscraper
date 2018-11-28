//
//  main.cpp
//  GoogleCodejam1C
//
//  Created by Sapphire-MAC on 5/11/14.
//  Copyright (c) 2014 sapphire. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

long long gcd(long long n, long long m) {
	long long gcd, remainder;
    
	while (n != 0)
	{
		remainder = m % n;
		m = n;
		n = remainder;
	}
    
	gcd = m;
    
	return gcd;
}

int main(int argc, const char * argv[])
{
    ifstream ifstream;
    ofstream ofstream;
    ifstream.open("/Users/sapphire/Documents/GoogleCodejam/GoogleCodejam1C/GoogleCodejam1C/input.txt");
    ofstream.open("/Users/sapphire/Documents/GoogleCodejam/GoogleCodejam1C/GoogleCodejam1C/output.txt");
    
    int count;
    
    ifstream >> count;
    string delimiter = "/";
    
    for(int i = 0; i < count; ++i) {
        ofstream << "Case #" << (i + 1) << ": ";
        int j = 0;
        
        string row;
        ifstream >> row;
        
        istringstream iss(row);
        
        string token;
        
        string s0, s1;
        
        while(getline(iss, token, '/')) {
            if(j == 0) {
                s0 = token;
            }
            else {
                s1 = token;
            }
            ++j;
        }
        
        long long n0, n1;
        
        istringstream(s0) >> n0;
        istringstream(s1) >> n1;
        
        long long newNumber1, newNumber2;
        newNumber1 = n0 / gcd(n0, n1);
        newNumber2 = n1 / gcd(n0, n1);
        
        n0 = newNumber1;
        n1 = newNumber2;
        
        bool flag = false;
        
        long long a = 2;
        
        for(int k = 0; k < 40; ++k) {
            if(n1 == a) {
                flag = true;
                a *= 2;
            }
            else {
                a *= 2;
            }
        }
        
        cout << flag << " " << a << endl;
        
        a /= 2;
        
        if(flag) {
            for(int k = 0; k < 40; ++k) {
                if(n1 == a) {
                    cout << k << endl;
                    if(n0 == 1) {
                        ofstream << (40 - k) << endl;
                        break;
                    }
                    
                    if(n0 % 2 == 1) {
                        n0 = (n0 - 1) / 2;
                        n1 /= 2;
                    }
                    else {
                        n0 /= 2;
                        n1 /= 2;
                    }
                }
                a /= 2;
                
                if(k == 39) {
                    ofstream << "impossible" << endl;
                }
            }
        }
        else {
            ofstream << "impossible" << endl;
        }
    }
    
    return 0;
}

