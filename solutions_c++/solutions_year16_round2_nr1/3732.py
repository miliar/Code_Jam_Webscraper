#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<map>
#include <iostream>     // std::cout
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

int *orgTile;
int K, C;
string S;
string Sarr[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
map<char, int> charMap;
std::stringstream ss;

void decRef(string inS){
    for(uint32_t i = 0; i < inS.size(); i++){
        charMap[inS[i]]++;
    }
}

bool findMatch(string inS){
    for(uint32_t i = 0; i < inS.size(); i++){
        if(charMap[inS[i]] == 0){
            for(uint32_t j = 0; j < i; j++){
                charMap[inS[j]]++;
            }
            return false;
        }
        charMap[inS[i]]--;
    }
    return true;
}

bool checkDone(){
    map<char, int>::iterator it;
    for(it = charMap.begin(); it != charMap.end();it++){
       if(it->second != 0)
           return false;
    }
    return true;
}

string regress(uint32_t start){
    stringstream ret;
    for(uint32_t i = start; i < 10; i++){
        //printf("Find match %s \n", Sarr[i].c_str());
        if(findMatch(Sarr[i])){
            string temp = regress(i);
            if(!checkDone()){
                decRef(Sarr[i]);
            }else{
                ret << i << temp;
                break;
            }
        }
    }
    return ret.str();
}

void run(){
    charMap.clear();
    for(uint32_t i = 0; i < S.size(); i++){
        charMap[S[i]] = charMap[S[i]] + 1;
        //printf("Map char:%c %d \n", S[i], charMap[S[i]]);
    }
    cout << regress(0)<< endl;
}                    

int main(int argc, char**argv){
    int numTest;
    ifstream myfile ("A-small-attempt0.in.txt");
    myfile >>  numTest;
    for(int caseNo = 0; caseNo < numTest; caseNo++){
        myfile >> S;
        printf("Case #%d: ", (caseNo+1));
        run();
    }
}
