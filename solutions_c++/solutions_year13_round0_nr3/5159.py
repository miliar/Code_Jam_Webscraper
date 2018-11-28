#include <stdexcept>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <stack>
#include <list>
#include <map>
#include <queue>
#include <cmath>
#include <climits>
#include <ctime>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <utility>
#include <set>
using namespace std;

#ifndef COMMON_H
#define COMMON_H

template <class E>
void print_vector(vector<E> A){
    for(int i = 0; i < (int)A.size(); i++){
        cout << A[i] << "\t";
    }
    cout << endl;
}

template <class E>
void print_matrix(vector<vector<E> > A){
    for(int i = 0; i <(int)A.size(); i ++){
        vector<E> tv = A[i];
        for(int j = 0; j < (int)tv.size(); j++){
            cout << tv[j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}

void print_array(int* A, int sz){
    for(int i = 0; i < sz; i++){
        cout << A[i] << "\t";
    }
    cout << endl;
}

template <class T>
void print_array(T* A, int sz){
    for(int i = 0; i < sz; i++){
        cout << A[i] << "\t";
    }
    cout << endl;
}

template <class T>
void print_vector(vector<T> A, int beg, int end){
    for(int i = beg; i < end; i ++)
        cout << A[i] << "\t";    
    cout << endl;
}

void print_vector(vector<pair<int, int> > A){
    for(int i = 0; i < (int)A.size(); i++){
        cout << "(" << A[i].first << ", " << A[i].second << ") ";
    }
    cout << endl;
}

void swap(vector<int>& A, int a, int b){
    int t = A[a];
    A[a] = A[b];
    A[b] = t;
}

void swap(int& a, int& b){
    int t = a;
    a = b;
    b = t;
}

void swap(int*& A, int a, int b){
    int t = A[a];
    A[a] = A[b];
    A[b] = t;
}

void swap(string& A, int a, int b){
    char t = A[a];
    A[a] = A[b];
    A[b] = t;
}

template <class T>
bool check_vector(vector<T> A,vector<T> B){
    if(A.size() != B.size())
        return false;
    for(int i = 0; i < (int)A.size(); i++){
        if(A[i] != B[i])
            return false;
    }
    return true;
}

template <class T, class E>
bool check_vector(vector<pair<T,E> > A, vector<pair<T,E> > B){
    if(A.size() != B.size())
        return false;
    for(int i = 0; i < (int)A.size(); i++){
        if(A[i].first == B[i].first && A[i].second == B[i].second){
            //do nothing
        }else{
            return false;
        }
    }
    return true;
}

template <class T> 
bool check_matrix(vector<vector<T> > A, vector<vector<T> > B){
    if(A.size() != B.size())
        return false;    
    int sz = (int)A.size();
    for(int i = 0; i < sz; i++){
        if(A[i].size() != B[i].size())
            return false;
        for(int j = 0; j < (int)A[i].size(); j++){
            if(A[i][j] != B[i][j])
                return false;
        }
    }
    return true;
}

void message(bool flag, string msg = ""){
    if(flag){
        cout << "\tpass\t" << msg << endl;
    }else{
        cout << "\tfail\t" << msg << endl;
    }
}

vector<vector<int> > load_int_file(string fileName){
    vector<vector<int> > A;
    ifstream fin(fileName.c_str());
    if(!fin.good()){
        cout << "Error, cannot read file " << fileName << endl;
        return A;
    }
    int nTest;
    fin >> nTest;
    string line;
    getline(fin,line);
    for(int i = 1; i <= nTest; i++){
        getline(fin,line);
        vector<int> tv;
        char* pch = strtok((char*)line.c_str(),",");
        while(pch != NULL){
            int x = atoi(pch);
            tv.push_back(x);
            pch = strtok(NULL,",");
        }
        A.push_back(tv);        
    }
    return A;
}

#endif
//#include "common.h"

string add(string s1, string s2){
    int sz1 = s1.size();
    int sz2 = s2.size();
    int i = sz1-1;
    int j = sz2-1;
    int t = 0, carry = 0;
    int a, b;
    string ret = "";
    while(1){
        if(i<0&&j<0)
            break;
        a = 0;
        if(i>=0)
            a = s1[i--]-'0';
        b = 0;
        if(j>=0)
            b = s2[j--]-'0';
        t = a + b + carry;
        carry = t/10;
        t = t%10;
        ret.insert(0,1,t+'0');
    }
    if(carry > 0)
        ret.insert(0,1,carry+'0');
//    cout << "a+b = " << s1 << "+" << s2 << " = " << ret << endl;
    return ret;
}

string multiply(string str, char ch){
    string s = "";
    int t = 0, carry = 0, a = 0, b = (ch-'0');
    for(int i = str.size()-1; i >= 0; i--){
        a = str[i]-'0';
        t = a * b + carry;
        carry = t/10;
        t = t%10;
        s.insert(0,1,t+'0');
    }
    if(carry > 0)
        s.insert(0,1,carry+'0');
    return s;
}

string multiply(string a, string b){
        string t = "";
        for(int j = b.size()-1; j >= 0 ; j--){
            string tmp = multiply(a,b[j]);
            int i = b.size()-1-j;
            while(i>0){
                tmp = tmp + "0";
                i--;
            }

            t = add(t,tmp);
        }
        return t; 
}

bool check(string s){
    int i = 0;
    int j = s.size()-1;
    while(i<j){
        if(s[i++] != s[j--])
            return false;
    }
    return true;
}
bool cmp_less(string a, string b){
    if(a.size() < b.size())
        return true;
    if(a.size() > b.size())
        return false;
    for(int i = 0; i < a.size(); i++){
        if(a[i] < b[i])
            return true;
        else if(a[i] > b[i])
            return false;
    }
    return false;
}

void check_all(string beg, int k){
//    string beg = "100000000";
    string end = "1";
    string i = beg;
//    int k = 51;
    while(k>=0){
        end = multiply(end,"10");
        k--;
    }
    while(cmp_less(i,end)){
        if(check(i)){
            string s = multiply(i,i);    
            if(check(s)){
                cout << i << endl;
//                cout << i << "\tsquare = " << s << "\t 1" << endl;
            }
        }
        i = add(i,"1");
    }
}

/*
bool check(unsigned long long a){
    int base = 1;
    unsigned long long b = a;
    while(b >= 10){
        b = b/10;
        base = 10 * base;
    }
    b = a;
    int c = 0;
    while(base >= 1){
        c = a/base;
        if(c != a%10)
            return false;
        a = (a - c * base)/10;
        base = base / 100;
    }
    return true;
}


void check_all0(){
    unsigned long long end = pow(10,7);
    unsigned long long i;
    for(i = 1; i <= end; i++){
        unsigned long long square = i * i;
        if(check(square)){
            cout << "i = " << i << "\tsquare = " << square << "\t 1" << endl;
        }
    }
}

void test(){
    cout << INT_MAX << endl;
    cout << LONG_MAX << endl;
    cout << ULONG_MAX << endl;
    unsigned long long a;
    for(a = 1; a < 1800; a++){
        bool ret = check(a);
        cout << a << "\t" << ret << endl;
    }
}
*/

int cmp_str(string a, string b){
    if(a.size() < b.size())
        return -1;
    if(a.size() > b.size())
        return 1;
    for(int i = 0; i < a.size(); i++){
        if(a[i] < b[i])
            return -1;
        else if(a[i] > b[i])
            return 1;
    }
    return 0;
}

int search_upper(vector<string>& A, string key){
    int i = 0;
    int j = (int)A.size()-1;
    int m;
    while(i <= j){
        m = (i+j)/2;
        if(cmp_str(A[m],key) == 0){
            return m;
        }else if(cmp_str(A[m],key) < 0){
            i = m+1;
        }else{
            j = m-1;
        }
    }
    return i;
}

int search_lower(vector<string>& A, string key){
//    cout << "A.size() = " << A.size() << endl;
    int i = 0;
    int j = (int)A.size()-1;
    int m;
    while(i <= j){
        m = (i+j)/2;
//        cout << "key = " << key << endl;
//        cout << "A[m] = A[" << m << "]= " << A[m] << endl;
        if(cmp_str(A[m],key) == 0){
            return m;
        }else if(cmp_str(A[m],key) < 0){
            i = m+1;
        }else{
            j = m-1;
        }
    }
    return j;
}

vector<string> load_data(){
    ifstream fin("./a555.log");
    if(!fin.good()){
        cout << "Error, cannot open file" << endl;
        vector<string>B;
        return B;
    }
    vector<string> A;
    string line;
    while(getline(fin,line)){
        A.push_back(line);
    }
    fin.close();
    return A;
}

void parse_line(string s, string& a, string& b){
    int i = 0;
    for(i = 0; i < s.size(); i++){
        if(s[i] == ' ')
            break;
    }
    a = s.substr(0,i);
    for(i = s.size()-1; i >=0; i--)
        if(s[i] == ' ')
            break;
    i++;
    b = s.substr(i);
    cout << "line = [" << s << "]" << endl;
    cout << "a  = [" << a << "]" << endl;
    cout << "b  = [" << b << "]" << endl;
}

void solve(){
    vector<string> A = load_data();
    cout << "loading data(): A.size() = " << A.size() << endl;


    ifstream fin("./c-small.in");
    if(!fin.good()){
        cout << "Error, cannot open file" << endl;
        return;
    }
    
    ofstream fout("./out.txt");
    if(!fout.good()){
        cout << "Error, cannot open file" << endl;
        return;
    }

    
    int nTest;
    string a, b;
    fin>>nTest;
    string line;
    getline(fin,line);

    for(int i = 0; i < nTest; i++){
        getline(fin,line);        
        parse_line(line,a,b);
        int lower = search_upper(A,a);
        int upper = search_lower(A,b);
//        cout << "lower = " << lower << endl;
//        cout << "upper = " << upper << endl;
        fout << "Case #" << (i+1) << ": " << upper-lower+1 << endl;    
    }
    fin.close();
    fout.close();
}

void test(){
    string a = "4";
    string b = "485";
    vector<string> A = load_data();
    cout << "A.size() = " << A.size() << endl;
    int idxb = search_lower(A,b);
    cout << idxb << endl;
}

void write_square(){
    vector<string> A = load_data();
    ofstream fout("./a555.log");
    for(int i = 0; i < A.size(); i ++){
        string s = A[i];
        string t = multiply(s,s);
        fout << t << endl;
    }
    fout.close();
}

int main(){
    //test();
//    string beg = "1";
//    int k = 7;
//    test();
    //check_all(beg,k);
    solve();
//    write_square();

    return 0;
}
