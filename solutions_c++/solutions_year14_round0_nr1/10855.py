#include <algorithm>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
long long int  x,y,tam;
int A[10][10];
int B[10][10];
int T;
int r1,r2;
int main(){
    cin >> T;
    for(int i = 1; i<=T; i++){
        
        cin >> r1;
        for(int i = 1; i <=4; i++){
            for(int j = 1; j<=4; j++)cin >>A[i][j];
        }
        cin >> r2;
        for(int i = 1; i <=4; i++){
            for(int j = 1; j<=4; j++)cin >>B[i][j];
        }
        int rpt=0;
        int index = 0;
        for(int i = 1; i <=4; i++){
            for(int j = 1; j<=4; j++){
                if(B[r2][j]==A[r1][i]){rpt++;
                index = i;}
            }
        }
       if(rpt>1)cout <<"Case #"<<i<<": "<< "Bad magician!"<<endl;
       else{
           if(!rpt){
               cout <<"Case #"<<i<<": "<< "Volunteer cheated!"<<endl;
           }
           else{
           cout <<"Case #"<<i<<": "<< A[r1][index]<<endl;
           }
       }
       
    }
    return 0;
 }