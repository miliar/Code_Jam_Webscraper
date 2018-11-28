//
//  main.cpp
//  t3
//
//  Created by Jasper Jia on 13-4-13.
//  Copyright (c) 2013年 Jasper Jia. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>

#define TOI(x) ((x)-'0')
#define TOC(x) ((x)+'0')
#define SAY(x) cout<<(x)<<endl;
using namespace std;

void high_add(char* a, int pos){
    size_t len = strlen(a);
    if(pos >= len){
        for (int i = (int)len; i<pos; i++) a[i] = '0';
        a[pos] = '1';
        a[pos+1] = 0;
    }
    else{
        a[pos]++;
        for (int i = pos; i<len-1; i++) {
            if(TOI(a[i]) == 10) a[i]='0', a[i+1]++;
        }
        if(TOI(a[len-1]) == 10) a[len-1] = '0', a[len] = '1', a[len+1] = 0;
    }
}

int compare(const char* a, const char* b){
    size_t alen = strlen(a);
    size_t blen = strlen(b);
    if(alen != blen) return alen>blen?1:-1;
    else{
        char aa[200], bb[200];
        for(int i=0;i<alen;i++) aa[i] = a[alen-1-i]; aa[alen] = 0;
        for(int i=0;i<alen;i++) bb[i] = b[alen-1-i]; bb[alen] = 0;
        return strcmp(aa,bb);
    }
    return true;
}

bool check_palindrome(const char* w){
    size_t l = strlen(w);
    for (int i = 0; i < l/2+1; i++) {
        if(w[i] != w[l-1-i]) return false;
    }
    return true;
}

int check(const char* w, const char* upper){
    //cout<<"begin "<<w<<' '<<upper<<endl;
    int tlen = ((int)strlen(w)-1)/2+1;
    int count = 0;
    char t[200];
    char tsq[200];
    
    for (int i = 0;i < tlen-1; i++) t[i] = '0'; t[tlen-1] = '1'; t[tlen] = 0;
    for (int i = 0;i < (tlen-1)*2; i++) tsq[i] = '0'; tsq[tlen*2-2] = '1'; t[tlen*2-1] = 0;
    
    int inrange = 0;
    while (inrange < 2) {       
        
        if (inrange == 0 && compare(tsq, w) >= 0) inrange = 1;
        if (compare(tsq, upper) > 0) inrange = 2;
        if (inrange == 1){
            if( check_palindrome(t) && check_palindrome(tsq))
            {count++;}//cout<<t<<' '<<tsq<<endl;}
        }
        
        high_add(tsq, 0);
        tlen = (int)strlen(t);
        for (int c = 0; c<tlen; c++) {
            for (int p = 0; p < TOI(t[c]); p++) {
                high_add(tsq, c);
                high_add(tsq, c);
            }
        }
        high_add(t, 0);
        
        //cout<<t<<' '<<tsq<<endl;

    }
    return count;
}

void inverse(char* w){
    size_t len = strlen(w);
    char aa[200];
    for(int i=0;i<len;i++) aa[i] = w[len-1-i]; aa[len]=0;
    strcpy(w, aa);
}

int main(int argc, const char * argv[])
{
    int T;    
    char lower[200], upper[200];
    int count;
    ifstream fin("/Volumes/Documents/t3/t3/C-small-attempt0.in");
    ofstream fout("/Volumes/Documents/t3/t3/C-small-attempt0.out");
    fin >> T;
    for (int i=0; i<T; i++) {
        fin >> lower >> upper;
        inverse(lower); inverse(upper);
        count = check(lower, upper);
        fout<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}

