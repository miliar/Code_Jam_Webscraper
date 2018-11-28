#include<iostream>
#include<cmath>
#include<fstream>
#include<string>

using namespace std;

void addbinary(int num[], int len);
unsigned long long convertbinary(int num[], int len, int base);
int testprime(unsigned long long num);

int main(){
    
    ifstream infile;
    ofstream outfile;
    
    infile.open("C-small-attempt1.in");
    outfile.open("output.txt");
    
    int t,n,j;
    // t = test case;
    // j = distinct jam coin
    // n = coin length
    int* num;
    unsigned int prove[9] = {0};
    unsigned long long ans;
    bool isprime = true;
    
    infile >> t;
    
    for(int i = 0; i<t; i++){
        
        infile >> n >> j;
        
        num = new int[n];
        num[0] = 1;
        num[n-1] = 1;
        
        for(int i=1; i < n-1;i++){
            num[i] = 0;
        }
        
        outfile << "CASE #" << i+1 << ":" << endl;
        
        //repeat for distinct jam coin.
        //don't finish til ajam coin is found
        for(int k = 0; k<j; k++){
            
            isprime = true;
            
            while(isprime){
                isprime = false;
                for(int base = 2; base <= 10 && !isprime; base++){
                    
                    ans = convertbinary(num, n, base);
                    prove[base-2] = testprime(ans);
                    
                    if(prove[base-2] == -1){
                        isprime = true;
                        addbinary(num, n);
                    }
                    else{
                        isprime = false;
                    }
                }
            }
            
            for(int i = n-1; i >= 0; i--){
                outfile << num[i];
            }
            
            outfile<< " ";
            
            for(int i = 0; i<9; i++){
                outfile << prove[i] << " ";
            }
            outfile<< endl;
            
            addbinary(num,n);
        }
        
    }
    
    
    infile.close();
    outfile.close();
}

void addbinary(int num[], int len){
    
    int carry = 0;
    
    if((num[1] + 1) == 1){
        num[1] = 1;
        carry = 0;
    }
    else{
        num[1] = 0;
        carry =1;
    }
    
    for(int i=2; i<len; i++){
        if((num[i] + carry) == 0){
            num[i] = 0;
            carry = 0;
        }
        else if((num[i] + carry) == 1){
            num[i] = 1;
            carry = 0;
        }
        else if((num[i] + carry) == 2){
            num[i] = 0;
            carry = 1;
        }
    }
}

unsigned long long convertbinary(int num[], int len, int base){
    
    unsigned long long ans = 0;
    
    for(int i = 0; i<len; i++){
        ans += (num[i] * pow(base, i));
    }
    return ans;
}

int testprime(unsigned long long num){
    unsigned long long limit;
    int div = 2;
    limit = sqrt(num);

    if(!(num%div)){
        return div;
    }
    div++;
    
    while(div<=limit){
        if(!(num%div)){
            return div;
        }
        div += 2;
    }
    
    return -1;
}