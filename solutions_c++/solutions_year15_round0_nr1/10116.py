#include <iostream>
#include <algorithm>
#include <set>
#include<stdio.h>
#include <vector>
#include <cmath>
#include <map>
#include<stdlib.h>
using namespace std;

int main(){
    freopen("A-small-attempt1.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    int test; cin>> test;

    for(int i = 1; i <= test; i++){

        int number; cin >> number;
        int count[100] = {0};
        int count1[100] = {0};
        int count2 = 0;
        string p; cin>>p;
        for(int j = 0;j <= number; j++){
            count[j] = p[j] - 48;
        }
        for(int j = 1;j <= number; j++){
            count[j] =  count[j] + count[j - 1];
        }
        for(int j = 1;j <= number; j++){
            if(count[j-1] + count2 < j && p[j] != '0'){
                count2 += j - count[j-1] - count2;
            }
        }
        cout<<"Case #"<<i<<": "<<count2<<"\n";
    }
    return 0;
}
