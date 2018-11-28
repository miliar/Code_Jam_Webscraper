//
//  main.cpp
//  Code Jam 2
//
//  Created by Rishab Mehra on 12/04/14.
//  Copyright (c) 2014 Rishab Mehra. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

long double check(ifstream &fin);

int main() {
    int x;
   
    ifstream fin("Test1.txt",ios::in);
    fin>>x;
    long double arr[100];
    for(int i=0;i<x;i++)
        arr[i]=check(fin);
    
    for (int i=0; i<x; i++) {
        cout<<"Case #"<<i+1<<": "<<setprecision(10)<<arr[i]<<endl;
    }
    return 0;
}


long double check(ifstream &fin)
{
    long double c,f,x;
    fin>>setprecision(10)>>c>>f>>x;
    long double tTime=0;
    //int farms=0;
    long double speed=2;
    int check=0;
    
    while (check==0) {
        check=1;
    if (x/speed>=(c/speed+x/(speed+f))) {
        tTime+=c/speed;
        speed+=f;
        check=0;
     }
        
        if(check==1)
            tTime+=x/speed;
    }
    
   // cout<<setprecision(10)<<tTime;
    
    return tTime;
}

