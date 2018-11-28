//
//  main.cpp
//  Codejam
//
//  Created by Sorawit Paiboonrattanakorn on 4/13/56 BE.
//  Copyright (c) 2556 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>

#define N 32

using namespace std;


vector<int> v;
int first, last;

bool ok(string s){
    int len = s.length();
    int i;
    for(i=0;i<len/2;i++){
        if(s[i]!=s[len-i-1])
            return false;
    }
    return true;
}

int bsl(int n, int a, int b){
    int mid = (a+b)/2;
    if(first == a && last == b){ 
        while(v[mid]>n) mid--; return mid;
        
    }
    if(a<=b){
        first = a; last = b;
//        cout << n << " " << a << " " << b << " " << mid << endl;
        if(n==v[mid]) return mid;
        else if(n>v[mid]) return bsl(n,mid,b);
        else return bsl(n,a,mid);
    }
}


int bsu(int n, int a, int b){
    int mid = (a+b)/2;
    if(first == a && last == b){ 
        while(v[mid]<n) mid++; return mid;
        
    }
    if(a<=b){
        first = a; last = b;
//        cout << n << " " << a << " " << b << " " << mid << endl;
        if(n==v[mid]) return mid;
        else if(n>v[mid]) return bsu(n,mid,b);
        else return bsu(n,a,mid);
    }
}

int main ()
{
    int T,t,i,j;
    int a,b;
    cin >> T;
    v.clear();
    for(i=0;i<=N;i++){
        string tmp, tmp2;
        char temp[50],temp2[40];
        sprintf(temp,"%d",i*i);
        sprintf(temp2,"%d",i);
        
        tmp.assign(temp);
        tmp2.assign(temp2);
        if(ok(tmp)&&ok(tmp2)){
            v.push_back(i*i);
        }
    }
    
 
    for(t=1;t<=T;t++){
        first = last = -1;
        cout << "Case #" << t << ": " ;
        cin >> a >> b;
        int result;
        vector<int>::iterator one,two,three,four;
        one = lower_bound(v.begin(), v.end(), b);
        two = upper_bound(v.begin(), v.end(), b);
        result = upper_bound(v.begin(), v.end(), b) - lower_bound(v.begin(), v.end(), a);
//        if(one != two) result++;
        three = lower_bound(v.begin(), v.end(), a);
        four = upper_bound(v.begin(), v.end(), a);
        
        //if(one != two) result++;
        //else if(three != four) result++;
        cout << result << endl;
    }
    return 0;
}

