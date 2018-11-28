#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <deque>
#include <math.h>

using namespace std;






int main(){


int T;
cin>>T;

for (int i=0;i<T;i++){
    cout<<"Case #"<<i+1<<": ";
    int K,C,S;
    cin>>K;
    cin>>C;
    cin>>S;
    if(K==S){
       for (int j=1;j<=K;j++){
       cout<<j<<" ";
       } 
       cout<<endl;
    }
    else{
        if(S==1||C==1){
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            for (int j=0;j<S;j++){
            cout<<(K+1)*j+2<<" ";
            } 
        }
    }
    

}

return 0;

}

