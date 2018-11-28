/* 
 * File:   main.cpp
 * Author: bkak
 *
 * Created on April 12, 2014, 2:43 PM
 */

#include <cstdlib>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <string>
#include <sstream>
#include <climits>
#include <cmath>
#include <math.h>
#include <vector>
#include <ctime>
using namespace std;

double docalc(double c, double f, double x){
    
    double count = 0;
    double speed = 2;
    double time = 0;
    
    while(count<x){
        if ( ((x-count)/speed) > ((x-(count-c))/(speed+f)) ){
            if (count>=c){
                //cout <<"1";
                count -= c;
                speed += f;
            }
        }
        if ( (count+c) <= x){
            //cout <<"2";
            count += c;
            time += (c/speed);
            //cout << "$" << time << "/";
        } else {
            //cout << "3";
            time += ((x-count)/speed);
            count = x;
        }
        
    }
    return time;
    
}


int main(){
    
   
    string tmp;
    int i=0;
    int j=0;
    double a,b,c;
    
    getline(cin,tmp);
    int size = atoi(tmp.c_str());
    
    double ans;
    
    while (i<size){
        cin >> a >> b >> c;
        
        ans = docalc(a,b,c);
        
        
        i++;
        
        cout << "Case #" << i << ": " << std::setprecision(50) << ans << "\n";
    }
    
     return 0;
}
