#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define size 2501
using namespace std;

int main()
{
    FILE *fin = freopen("B-large.in", "r", stdin);
    FILE *fout = freopen("B-large.out", "w", stdout);
    long T,j=0,N,height;
    string S,last_word,temp1,temp2;
    cin>>T;
    while(T--){
        j++;
        int list[size]={0};
        cin>>N;
        for(int i=0;i<(2*N-1)*N;i++){
            cin>>height;
            list[height]++;
        }
        cout<<"Case #"<<j<<": ";
        for(int i=1;i<size;i++){
            // cout<<list[i]<<" ";
            if(list[i]%2 !=0)
                cout<<i<<" ";
        }
        cout<<endl;
    }
    
    return 0;
}