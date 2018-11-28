//
//  main.cpp
//  realthinsf
//
//  Created by Abhishek Anand on 13/04/14.
//  Copyright (c) 2014 AbhishekAnand. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(int argc, const char * argv[])

{
    int n;
    cin >> n;
    for(int f = 0; f <n; f++){
        int x;
        cin >> x;
        vector<double> a(x);
        vector<double> b(x);
        vector<double> c(x);
        vector <double> d(x);
        for(int i  = 0 ; i < x; i++){
            
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        for(int i  = 0 ; i < x; i++){
            
            cin >> b[i];
        }
        sort(b.begin(), b.end());
        for(int i  =0 ; i < x; i++){
            c.at(i)=a.at(i);
            d.at(i)=b.at(i);
        }
        int y = x;
        int war=0;
        
        while(a.empty()==false){
            
            if (a.at(y-1)> b.at(y-1) ){
                
                a.erase(a.begin()+(y-1));
                b.erase(b.begin());
                war++;
                y--;
            }else{
                for(int i = 0; i < y ; i++){
                    if(b.at(i)> a.at(y-1)){
                        
                        b.erase(b.begin() + i);
                        a.erase(a.begin() + (y-1));
                        y--;
                        
                        break;
                        
                    }
                }
            }
            
        }
        
        int dece=0;
        int z = x;
        while(c.empty()==false){
            
            if( d.at(z-1)> c.at(z-1)){
                d.erase(d.begin() + (z-1));
                c.erase(c.begin());
                z--;
                
            }else{
                
                for(int i = 0 ; i < z; i++){
                    if(c.at(i)> d.at(z-1)){
                        
                        c.erase(c.begin() + i);
                        d.erase(d.begin() + (z-1));
                        z--;
                        dece++;
                        break;
                        
                    }
                    
                }
            }
        }
        
        
        cout << "Case  #" << f + 1 << ": " << dece  << " " << war << "\n";
    }
    return 0;
}

