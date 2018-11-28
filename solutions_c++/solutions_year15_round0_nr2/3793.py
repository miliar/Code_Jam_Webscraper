//
//  main.cpp
//  Pancakes
//
//  Created by hawy on 4/11/15.
//  Copyright (c) 2015 meltaweel. All rights reserved.
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



int ReadNumbers( const string & s, vector <int> & v ) {
    istringstream is( s );
    int n;
    while( is >> n ) {
        v.push_back( n );
    }
    
    //std::sort (v.begin(), v.end());
    //std::reverse(v.begin(),v.end());
    
    return (int)v.size();
}

int findMinTime(int tTime, vector<int> &v){
    int sum=0;
    for(std::vector<int>::size_type i = 0; i != v.size(); i++) {
        sum +=(int) ( (v[i]-1) / tTime) ;
    }
    
    return tTime+sum;
}

int N;
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
    
    cin>>N;
    
    

    string pans_string;
    int i,j,D,minTime,temp_time;
    vector<int> pans;
    
    for (i=1; i<N+1; i++) {
        cin>>D;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        getline(cin,pans_string);
        j = ReadNumbers(pans_string, pans);
      
        
        minTime = *max_element(pans.begin(),pans.end());

        temp_time = 2;
        
        while(temp_time < minTime){
                        
            minTime = min(minTime, findMinTime(temp_time,pans ) );
            
            temp_time++;
        }
        
        
        
        printf("Case #%d: %d", i,minTime);
        cout<<endl;
        pans.clear();
    }
    
    return 0;
}


