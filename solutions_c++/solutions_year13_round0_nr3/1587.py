//
//  main.cpp
//  codejam3
//
//  Created by Zulkarnine Mahmud on 4/13/13.
//  Copyright (c) 2013 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include "math.h"
#include <algorithm>
#include <vector>
#include <string>
#include <array>
#include <sstream>


using namespace std;
int T;
long long A,B;
long long Squares[]={1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
 int squareCounter=39;

vector< int> fair;

string TrueFalse(bool b){
    return (b? "true":"false");
    
}
string convToString( long long number){
    stringstream s;
    s<<number;
    return s.str();
    
}


bool checkFair( long long x){
    string st=convToString(x);
    //cout<<"st="<<st<<endl<<"st.size()="<<st.size()<<endl;
     long long length=st.size();
    bool result=true;
    for ( long long i=0; i<length; i++) {
         long long m=st.at(i);
         long long n=st.at(length-(i+1));
        
        if (m!=n) {
            result=false;
            break;
        }
        
    
    }
    return result;

}

void FindSquaresWithinLimit( long long x, long long y){
     long long nearestSmallestRoot;
    nearestSmallestRoot=sqrt(x);
    for ( long long j=nearestSmallestRoot; j*j<=y; j++) {
        while (!checkFair(j)) {
            j++;
        }
        if (j*j>=x&&j*j<=y) {
             long long tempValue=j*j;
            if (checkFair(tempValue)==true) {
                Squares[squareCounter]=j*j;
                squareCounter++;
            }
            
        }
    }
}

 long long solveCase(long long Y,long long Z){
     long long count=0;
     for (long long x=0; x<squareCounter; x++) {
         if ((Squares[x]>=A)&&(Squares[x]<=B)) {
             count++;
         }
     }
     
     return count;

    
    
}



int main(){
    
    /*FindSquaresWithinLimit(1, 100000000000000);
    cout<<"{";
    for (int x=0; x<squareCounter; x++) {
        cout<<Squares[x]<<", ";
    }
    cout<<"}";
    cout<<"\n"<<"square counter: "<<squareCounter;
    */
    freopen("C-large-1.in", "r", stdin);
    freopen("3_2.out", "w", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++) {
        cin>>A;
        //cout<<A<<endl;
        cin>>B;
        //cout<<B<<endl;
        //cout<<"case:"<<cas<<endl;
        //cout<<"A="<<A<<endl<<"B="<<B<<endl;
        cout<<"Case #"<<cas<<": "<<solveCase(A,B)<<endl;
        
        /*for (int i=0; i<squareCounter; i++) {
            cout<<sqrt(Squares[i])<<endl;
        }
        for (int i=0; i<squareCounter; i++) {
            cout<<"fair and square:"<<Squares[i]<<"\t";
        }
        cout<<endl;*/
        
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
    
}
