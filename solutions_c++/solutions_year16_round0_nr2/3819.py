#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<map>
#include <iostream>     // std::cout
#include <fstream>   
using namespace std;

int digs[10];
int *inStack;
void pop(int N){
    while(N != 0){
        //printf("N%d Nmod:%d \n", N, N%10);
        digs[N % 10]++;
        N = N /10; 
    }
}

bool check(int* myStack, int size){
    for(int i = 0; i < size; i++){
        if(myStack[i] == '0')
            return false;
    }
    return true;
}


int flips = 0;

int run(int* myStack, int start, int size, int caseNo){
    
    int neg = start;
    while(myStack[neg] != 0){
        neg++;
        //All top pos
        if(neg == size)
            return 0;
    }
    int numPostop = neg - start;
    int extraFlip = (numPostop > 0)? 2 : 1;
    while(myStack[neg] != 1){
        neg++;
        //All bottom neg
        if(neg == size)
            return extraFlip;
    }
    
    return extraFlip + run(myStack, neg, size, caseNo);
    
}

int main(int argc, char**argv){
    int numTest;
    ifstream myfile ("B-large.in.txt");
    myfile >>  numTest;
    for(int caseNo = 0; caseNo < numTest; caseNo++){
        string test_input;
        myfile >> test_input;
        inStack = new int[test_input.size()];
        for(int i = 0; i < test_input.size(); i++){
            if(test_input[i] == '+')
                inStack[i] = 1;
            else
                inStack[i] = 0;
            //printf("NN DEBUG %d \n",inStack[i]);
        }
        int ans = run(inStack,0, test_input.size(), caseNo);
        printf("Case #%d: %d \n", (caseNo+1), ans);
    }
}
