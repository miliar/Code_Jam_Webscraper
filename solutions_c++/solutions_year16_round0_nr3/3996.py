#include<iostream>
#include<string>
#include<queue>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
unsigned long long divisor[12];
unsigned long long mark;
vector<int>number;
int l,n,counter;
unsigned long long result;
bool check_prime ( ){
   unsigned long long i;

    if (result <= 3){
        return false;
    }
    else if (result % 2 == 0){
         mark = 2;
        return true;
    }
    else if (result % 3 == 0){
        mark = 3;
        return true;
    }
    i = 5;
    while( (i*i) <= result){
        if (result % i == 0){
            mark = i;
            return true;
        }
        if (result % (i + 2) == 0){
            mark = i + 2;
            return true;
        }
        i = i + 6;
    }
    return false;
}
bool func( ){
    for(int i = 2; i <= 10; i++){
        result = 0;
        for(int j = 0; j < number.size(); j++){
            result = (result*i) + number[j];
        }
        bool flag = check_prime();
        if( flag ){
            divisor[i] = mark;
        }
        else{
            return false;
        }

    }
    return true;
}
void backtrack( ){
    if( counter == l ){
        return;
    }
    bool flag;
    if( number.size() == n - 1){
        number.push_back(1);
        flag = func();
        if( flag ){
            for( int i = 0; i < number.size(); i++){
                printf("%d",number[i]);
            }
            for(int i = 2; i <= 10; i++){
                printf(" %llu",divisor[i]);
            }
            printf("\n");
            counter++;
        }
        number.pop_back();
    }
    else{
        number.push_back(0);
        backtrack();
        number.pop_back();
        number.push_back(1);
        backtrack();
        number.pop_back();
    }
}
int main(){

    number.push_back(1);
    int testcase;
    //freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
    scanf("%d",&testcase);
    for( int i = 1; i <= testcase; i++ ){
        scanf("%d%d",&n,&l);
        printf("Case #%d:\n",i);
        counter = 0;
        backtrack();
    }
return 0;
}
