//
//  main.cpp
//  prac
//
//  Created by Deshmukh  on 17/03/14.
//  Copyright (c) 2014 Deshmukh . All rights reserved.
//

#include <iostream>
#include<string>
#include<ctime>
#include<fstream>
#include<limits>

int main(int argc, const char * argv[])
{   using namespace std;
    ofstream output;
    ifstream input;
    int t,t1=1,i;
    double c,f,x,x1,rate;
    input.open("/Users/deshmukh/Desktop/c/Udit/codejam/input/sample");
    output.open("/Users/deshmukh/Desktop/c/Udit/codejam/output/output1.txt");
    input>>t;
    while(t1<=t){
        input.precision(5);
        input>>fixed>>c>>f>>x;
        //cin>>x1;
        //cout<<x1<<endl;
        //cout.precision(7);
        //cout<<fixed<<c<<" "<<f<<" "<<x<<endl;
        double time_for_farm[100000]{},time[100000]{};
        rate=2;
        time_for_farm[0]=0;
        time_for_farm[1]=c/rate;
        time[0]=x/rate;
        rate=rate+f;
        time[1]=time_for_farm[1]+x/rate;
        i=0;
        while(time[i+1]<time[i]){
            time_for_farm[i+2]=time_for_farm[i+1]+c/rate;
            rate+=f;
            time[i+2]=time_for_farm[i+2]+x/rate;
            i++;
        }
        output.precision(7);
        output<<"Case #"<<t1<<": "<<fixed<<time[i]<<"\n";
        
        
        t1++;
        
    }
    
    
    
    
    
   
    return 0;
}

