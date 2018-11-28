


#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <fstream>
#include <iostream>
#include <iomanip>


using namespace std;

double c, f, x;


void solve(int CaseN)
{
    //cout << c << " " << f << " " << x << endl;
    
    double prev, curr;
    prev = x/2.0;
    
    double i = 0;
    double a = c/2.0;
    double b = x/(2.0+f);
    curr = a+b;
    
    while(curr < prev) {
        
        prev = curr;       
        
        i = i + f;
        a = a + (c/(2+i));
        b = x/(2+i+f);
        
        //cout <<  i << " " << a << " " << b << endl;
        
        curr = a + b;        
        
    }

    //cout << curr << " " << prev << endl;
    cout << "Case #" << CaseN << ": " << std::fixed << std::setprecision(7) << prev << endl;
    
}


void input()
{
    int n, p=0;
    cin >> n;
    
    while(n!=0) {
        
        p++;
        
        cin >> c;
        cin >> f;
        cin >> x;
        
        
        solve(p);
        
        //cout << c << " " << f << " " << x << endl;
        c=0;f=0;x=0;
        
        n--;
    }
    
    
}



int main()
{
    //std::cout << std::fixed << std::setprecision(7);
    
    input();
    return 0;
}