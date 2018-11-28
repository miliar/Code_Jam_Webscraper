//
//  main.cpp
//  Mushroom Monster
//
//  Created by Shreyas Sinha on 18/04/15.
//  Copyright (c) 2015 Shreyas Sinha. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    int t,n,A[1005],max;
    long long sum,sum2;
    ofstream outfile;
    ifstream infile;
    infile.open("A-large.in");
    outfile.open("output.in");
    infile>>t;
    for (int k=1; k<=t; k++) {
        infile>>n;
        
        for (int i=0; i<n; i++) {
            infile>>A[i];
        }
        max=0;
        sum=0;
        for (int i=1; i<n; i++) {
            if (A[i]-A[i-1]<0) {
                sum+=(-(A[i]-A[i-1]));
                if (A[i-1]-A[i]>max) {
                    max=A[i-1]-A[i];
                }
            }
        }
        sum2=0;
        
        
        for (int i=0; i<n-1; i++) {
        
            if (A[i]<=max) {
                sum2+=A[i];
                
            }
            else{
                sum2+=max;
                
            }
            
        }
        outfile<<"Case #"<<k<<": "<<sum<<" "<<sum2<<"\n";
        
    }
    outfile.close();
    infile.close();
    return 0;
}
