//============================================================================
// Name        : sheep.cpp
// Author      : Xining Li
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
using namespace std;


void setarray(int N,bool* a){
    string s=to_string(N);
    for(int i=0;i<s.length();i++){
        int k=s[i]-48;
        a[k]=true;
    }
    
}

bool checkarray(bool* a){
    int i=0;
    for(;i<10;i++){
        if(a[i]==0){
            break;
        }
    }
    return i==10;
}

int Count(int N){
    bool a[10];
    for(int i = 0;i < 10;i++)
        a[i] = 0;
    
    int n=N;
    int count=0;
    while(checkarray(a)==0){
        setarray(n,a);
        n=n+N;
        count++;
        if(count>100000){
            break;
        }
    }
    return n-N;
}
int main(){
    ifstream myfile;
    ofstream out("output.txt");
    int n;
    myfile.open("input.in");
    if (myfile.fail()) {
        cout << "Read file fail!!!" << endl;
        return -1;
    }
    myfile >> n;
    int s;
    for(int i=0;i<n;i++){
        myfile>> s;
        if (s==0) {
        out <<"Case #"<<i+1<<": "<<"INSOMNIA"<<'\n';
        }
        else{
            out <<"Case #"<<i+1<<": "<< Count(s)<<'\n';
        }
    }
    myfile.close();
    out.close();
    return 0;
}
