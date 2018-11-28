//
//  main.cpp
//  cjq
//
//  Created by No_love_no_problem on 10.04.16.
//  Copyright © 2016 Anna Vlasova. All rights reserved.
//
#include <fstream>
#include <iostream>
#include <array>

void equal(std::string &a,std::string &b)
{
    int x=a.length();
    int y=b.length();
    if(x>y)
    {
        while(x>b.length())
        {
            b='0'+b;
        }
    }
    else
    {
        while(y>a.length())
        {
            a='0'+a;
        }
    }
}

void plutz(std::string &a, std::string b)
{
    equal(a, b);
    
    int l=a.length();
    int e=0;
    for(int i=l-1; i>-1; i--)
    {
        e=a[i]-48+b[i]-48+e;
        a[i]=e%10+48;
        e=e/10;
    }
    if(e!=0)
    {
        char q=e+48;
        a=q+a;
    }
}

int main() {
    std::ifstream in;
    in.open("/Users/no_love_no_problem/Desktop/A-large.in");
    std::ofstream out;
    out.open("/Users/no_love_no_problem/Desktop/A-large.out");
    
    int k;
    std::string n;
    in >> k;
    
    for (int i = 0; i < k; i++){
        
        out << "Case #" << i+1 << ": ";
        
        in >> n;
        if (n == "0") {
            out << "INSOMNIA\n";
            continue;
        }
        
        std::array<bool, 10> digits({0, 0, 0, 0, 0, 0, 0, 0, 0, 0});
        
        bool q = 0;
        std::string sum("0");
        
        while (!q) {
        
            plutz(sum, n);
            
            for(auto x : sum){
                digits[x-'0'] = 1;
            }
            
            q = 1;
            for (int j = 0; j < 10; j++) {
                q = q && digits[j];
            }
        }
        out << sum << "\n";
    }
    
    in.close();
    out.close();
    return 0;
}
