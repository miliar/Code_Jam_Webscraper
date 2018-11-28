//
//  main.cpp
//  codejam
//
//  Created by Stephen Zhu on 4/11/14.
//  Copyright (c) 2014 Stephen Zhu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <list>

using namespace std;

#define tr(i, end) \
for (int i = 0; i < end; ++i)




int main()
{
    
    ifstream ins("D-large.in");
    FILE * out;
    out = fopen("D-large.out", "w");
    
    int T;
    ins >> T;
    tr(i, T){
        fprintf(out, "Case #%i: ", i+1);
        int N;
        ins >> N;
        
        int dpoints(0), warpoints(0);
        
        //play deceitful war
        list<double> naomi;
        list<double> ken;
        
        tr(j, N){
            double temp;
            ins >> temp;
            naomi.push_back(temp);
        }
        
        tr(j, N){
            double temp;
            ins >> temp;
            ken.push_back(temp);
        }
        
        naomi.sort();
        ken.sort();
        
        list<double> naomi2 = naomi;
        list<double> ken2 = ken;
        
        tr(j, N){
            if (naomi.front() < ken.front()){
                ken.pop_back();
            }
            else {
                ken.pop_front();
                dpoints++;
            }
            naomi.pop_front();
        }
        
        
        tr(j,N){
            if(ken2.front() < naomi2.front()){
                naomi2.pop_back();
            }
            else {
                naomi2.pop_front();
                warpoints++;
            }
            ken2.pop_front();
        }
        
        fprintf(out, "%i %i\n", dpoints, N-warpoints);
        
    }
        
    return 0;
}



