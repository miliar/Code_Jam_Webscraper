#include <iostream>
#include <math.h>
#include <stdio.h>
#include <string>
using namespace std;

long long int baseList[9];

int checkPrime(long long int n){
    if(n %2 ==0 ){
        return 2;
    }
    for(long long int i=3 ; i <= sqrt(n) ; i+=2){
        if(n %i == 0){
            return i;
        }
        
    }
    return 0;
}
void reset(){
    for(int i=0 ; i< 9; i++){
        baseList[i] = 0;
    }
}
void printJamcoin(string str){
    cout << str;
    for(int i =0; i< 9; i++){
        cout << " " << baseList[i];
    }
    printf("\n");
}
    
int baseConversion(int base, string cand){
    long long int sum =0;
    int len = cand.length();
    for(int i = 0; i < len; i++){
        sum+= cand.at(i) * pow(base,len-i-1);
    }
    //printf("%d base = %d\n ",base, sum);
    return checkPrime(sum);
}

string decToBin(long long int n){
    string cur = "";
    if (n/2!= 0) {
        cur = decToBin(n/2);
    }
    char c = '0' + (n%2);
    
    return cur+c;
    
}
void createJamcoin(int N, int J){
    int cnt=0 ;
    long long int curnum = 0;
    while(cnt < J){
        string midStr = decToBin(curnum);
        for(int j=midStr.length();j < N-2; j++){
            midStr = '0' + midStr;
        }
        midStr = "1" + midStr + "1";
        //cout << midStr << endl;
        long long int res ;
        for(int i = 2; i <= 10 ; i++ ){
            res= baseConversion(i,midStr);
            if(res == 0){
                break;
            }
            else{
                baseList[i-2] = res;
            }
            
        }
        if(res != 0){
            printJamcoin(midStr);
            cnt++;
        }
        curnum++;
        reset();
    }
}

int main() {
    int testCase;
    int N, J;
    cin >>testCase;
    
    for(int i =0; i< testCase; i++){
        cin >> N;
        cin >> J;
        printf("Case #%d: \n",i+1);
        createJamcoin(N,J);
    }
}