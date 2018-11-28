#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<list>
#include<map>
#include <iostream>     // std::cout
#include <fstream>   
using namespace std;

void run(string S, int caseNo){
    list<char> ans;
    ans.push_back(S[0]);
    for(int i = 1; i< S.size(); i++){
    //printf("NN DEBUG %c \n", S[i]);
        if( S[i] >= ans.front()){
            ans.push_front(S[i]);
        }else{
            ans.push_back(S[i]);
        }
    }
    list<char>::iterator it;
    string ansOut = "";
    for(it = ans.begin(); it!= ans.end(); it++){
        ansOut = ansOut + (*it);
    }
    printf("Case #%d: %s \n", caseNo, ansOut.c_str());
}

int main(int argc, char**argv){
    int numTest;
    ifstream myfile ("A-large.in.txt");
    myfile >>  numTest;
    for(int i = 0; i < numTest; i++){
        string test_input;
        myfile >> test_input;
        //printf("NN DEBUG: %d\n", test_input);
        run(test_input, i+1);
    }
}
