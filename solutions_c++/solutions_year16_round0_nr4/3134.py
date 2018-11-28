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
int K, C, S;

int* createNext(int* in, int size){
    //TODO: optimize
    int* tempTile = new int [size * K];
    int tempIdx = 0;
    for(int i = 0; i< size; i++){
        //L
        if(in[i] == 0){
            for(int i = 0; i < K;i++){
                tempTile[tempIdx + i] = orgTile[i];
            }
        //G
        }else{
            for(int i = 0; i < K;i++){
                tempTile[tempIdx + i] = 1;
            }
        }
        tempIdx  = tempIdx + K;
    }
    return tempTile;
}

void printfNum(int* num, int size){
    //cout << "NN DEBUG Tile:";
    //for(int i = size-1; i >=0;i--){
    //    cout << num[i];
    //}
    //cout << endl;
}

void encodeJam(int num){
    memset(orgTile, 0, sizeof(int) * K);
    int i = 0;
    while(num != 0){
        orgTile[i] = num % 2;
        i++;
        num = num >> 1;
    }
    printfNum(orgTile,K);
}

void run(){
    //int* sumTile = NULL;
    //int size = 0;
    //for(uint32_t comb = 1; comb < (1 << K); comb++){
    //    size = K;
    //    //printf("NN DEBUG Start comb:%d \n",comb);
    //    encodeJam(comb);
    //    int* startTile = orgTile;
    //    for(int i = 1; i< C; i++){
    //        startTile = createNext(startTile,size);
    //        size = size * K;
    //        printfNum(startTile,size);
    //    }
    //    
    //    if(sumTile == NULL){
    //        sumTile = new int[size];
    //        memset(sumTile, 0, sizeof(int) * size);
    //    }
    //    
    //    for(int i =0; i < size;i++){
    //        sumTile[i] = sumTile[i] + startTile[i];
    //    }
    //}
   
    ////printf("NN DEBUG sumtile\n");
    //printfNum(sumTile,size);
    //
    std::stringstream ss;
    //int ans = 0;
    //for(int i = 0; i < size;i++){
    //    if(sumTile[i] == ((1 << K) -1 )){
    //        cout << ' ' << (i+1) << endl;
    //        return;
    //    }else if(sumTile[i] > 0){
    //        ans++;
    //        if(ans <= S)
    //            ss << ' ' << (i + 1);
    //    }
    //}
    //if((ans == 0) || (ans > S)){
    //        cout << " IMPOSSIBLE" << endl;
    //}else{
    for(int i = 0 ; i< S; i++)
            cout << (i+1) << " ";
    cout << endl;
    //}
}

int main(int argc, char**argv){
    int numTest;
    ifstream myfile ("D-small-attempt0.in.txt");
    myfile >>  numTest;
    for(int caseNo = 0; caseNo < numTest; caseNo++){
        myfile >> K;
        myfile >> C;
        myfile >> S;
        orgTile = new int [K];
        printf("Case #%d: ", (caseNo+1));
        //printf("NN DEBUG K:%d C:%d S:%d \n", K, C, S);
        run();
    }
}
