/* 
 * File:   main.cpp
 * Author: pegasus
 *
 * Created on April 13, 2013, 3:21 AM
 */

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <map>
#include <cmath>
using namespace std;

/*
 * 
 */

bool has_a_sqaure (int y)
{

        float x= sqrt(y);
    
    if (x==floor(x))
    {
        return true;
    }
        return false;
}


string int_to_string (int x)
{
    stringstream ss;
    ss<<x;
    return ss.str();
}



bool isPlainDrom (int x)
{
string str_eq =int_to_string(x);

string rev (str_eq.rbegin() ,str_eq.rend());

return (str_eq ==rev);

}


int main(int argc, char** argv) {

    freopen("input.txt","r",stdin);
    freopen("out.in","w",stdout);
    
    int test_cases;
    
    cin>>test_cases ;
    
    for (int t=1 ; t <=test_cases ;t++)
    {
        int counter =0 ;
        
        int start ,end;
        
        cin>>start >>end;
        
        for (int i=start ; i<=end ;i++)
        {
            
            if (isPlainDrom(i))
            {
                if (has_a_sqaure(i))
                {
                    int sqr_i = (int)sqrt(i);
                    if (isPlainDrom(sqr_i))
                    {
                        counter++;
                    }
                
                }
                
            }
        }
        
        cout<<"Case #"<<t<<": "<<counter<<endl;
    }
    
    return 0;
}

