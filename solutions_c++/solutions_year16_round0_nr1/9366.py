//
//  QA.cpp
//  2016 Qualification Round Problem A
//
//  Created by meltaweel.
//  Copyright (c) 2016 meltaweel. All rights reserved.
//

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define toDigit(c) (c-'0')

int T,i;




bool add_each_digit(int x,std::set<int>& found)
{
    if(x >= 10)
         add_each_digit(x / 10, found);
    
    int digit = x % 10;
    
    found.insert(digit);
    
    if(found.size() == 10)
        return false;
    
    return true;
    
    
}

int remove_zeros(int &x){
    int c=0;
    while(x%10 ==0){
        x=x/10;
        c++;
    }
    return c;
}

int main(int argc, char *args[]) {
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        freopen("small.in","rt",stdin);
        freopen("small.out","wt",stdout);
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        freopen("large.in","rt",stdin);
        freopen("large.out","wt",stdout);
    }
    else {
        freopen("test.in", "r", stdin);
        
    }
    
    cin>>T;
    
    
    int N;
    for (i=1; i<T+1; i++) {
        
        cin>>N;
        
        if(N==0)
            printf("Case #%d: INSOMNIA",i);
        else{
            
            int m= remove_zeros(N);
            
            
            int NN=0;
            std::set<int> found;
            int j =1;
            int mm =1;
            if(m>0){
                mm=pow(10,m);
                found.insert(0);
            }
            while(true){
                
                NN=N*j;
                
                if(!add_each_digit(NN, found)){
                    if(m>0)
                        NN*=mm;
                    printf("Case #%d: %d",i,NN);
                    break;

                }else
                    j++;
                
                
               
                
                
                
            }
            
        }
        
        
        cout<<endl;
        
    }
    
    
    return 0;
}


