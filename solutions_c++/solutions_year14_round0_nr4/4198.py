//
//  main.cpp
//  DemoTest
//
//  Created by mezheng on 10/14/13.
//
//

#include <iostream>
#include <algorithm>
#include <vector>
#include<iomanip>
#include<queue>
#include <math.h>
using namespace std;


int main(int argc, const char * argv[])
{
    int n, t;
    vector<double> naomi(1000);
    vector<double> ken(1000);
    cin>>t;
    for (int i=1; i<=t; i++) {
        cin>>n;
        for (int j=0; j<n; j++) {
            cin>>naomi[j];
        }
        for (int j=0; j<n; j++) {
            cin>>ken[j];
        }
        cout<<"Case #" << i << ": ";
        
        sort(naomi.begin(), naomi.begin()+n);
        sort(ken.begin(), ken.begin()+n);
        
        int dr=0, wr=0;
        int ki=0;
        for (int i=0; i<n; i++) {
            if (naomi[i] > ken[ki]) {
                dr++;
                ki++;
            }
        }
        int ni=n;
        ki=n-1;
        while (ni--) {
            if (ken[ki] > naomi[ni]) {
                ki--;
            } else {
                wr++;
            }
        }
        
        cout<<dr<<" "<<wr<<endl;
    }
    return 0;
}

