//
//  main.cpp
//  test
//
//  Created by Shreyas Sinha on 09/04/16.
//  Copyright © 2016 Shreyas Sinha. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <algorithm>
#include <utility>


using namespace std;

typedef long long ll;
int t,n,a[27];
vector< pair<int, int> > v;
int main() {
    ifstream infile;
    ofstream outfile;
    ll sum=0;
    infile.open("A-large.in");
    outfile.open("output.in");
    
    infile>>t;
    for (int ic=1; ic<=t; ic++) {
            outfile<<"Case #"<<ic<<": ";
        infile>>n;
        string s;
        for (int i=0; i<n; i++) {
            infile>>a[i];
            sum+=a[i];
            v.push_back(make_pair(a[i], i));
        }
        
        while(sum>0){
            sort(v.begin(), v.end());
            vector< pair<int, int> >::iterator r,e,t=v.end();
            t--;
            r=t;
            r--;
            if((*t).first!=1){
                
                if(((float)((*r).first)/(sum-2))>0.5){
                    s.push_back('A'+(*t).second);
                    s.push_back('A'+(*r).second);
                    s.push_back(' ');
                    (*t).first--;
                    (*r).first--;
                    sum-=2;
                    
                }
                else{
                    s.push_back('A'+(*t).second);
                    s.push_back('A'+(*t).second);
                    s.push_back(' ');
                    (*t).first--;
                    (*t).first--;
                    sum-=2;
                }
            }
            else{
                if(sum%2==1){
                    s.push_back('A'+(*t).second);
                    s.push_back(' ');
                    (*t).first--;
                    sum--;
                }
                else{
                    s.push_back('A'+(*t).second);
                    s.push_back('A'+(*r).second);
                    s.push_back(' ');
                    (*t).first--;
                    (*r).first--;
                    sum-=2;
                }
            }
        }
        outfile<<s<<endl;
    }
    
    
    return 0;
}
