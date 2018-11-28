#include<iostream>
#include<time.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <unistd.h>
#include<fstream>

using namespace std;

ifstream in;
ofstream out;


int multiply(int a,int sol[],int size,int *rem){
    int carry = 0;
    int ans;
    for(int i=0;i<size;i++){
        ans = a*sol[i]+carry;
        rem[ans%10]--;
        carry = ans/10;
    }
    while(carry){
        rem[carry%10]--;
        carry = carry/10;
        size++;
    }
    return size;
}

int countDigits(int *a,int n){
    int i=0;
    while(n){
        a[i]=n%10;
        n/=10;
        i++;
    }
    return i;
}


void printd(int a,int sol[],int size){
    int carry = 0;
    int ans;
    for(int i=0;i<size;i++){
        ans = a*sol[i]+carry;
        sol[i] = ans%10;
        carry = ans/10;
    }
    while(carry){
        sol[size] = carry%10;
        carry = carry/10;
        size++;
    }
    for(int i=size-1;i>=0;i--){
        out<<sol[i];
    }
}

int main(){
    int cases,ccount=1;
    in.open("input.txt");
    out.open("result.txt");
    in>>cases;
    while(ccount<=cases){
        int n;
        in>>n;
        if(n==0){
            out<<"Case #"<<ccount<<": "<<"INSOMNIA"<<endl;
            ccount++;
            continue;
        }
        int a[10000]={0};
        int rem[10];
        for(int i=0;i<10;i++){
            rem[i]=1;
        }
        int digits = countDigits(a,n);
        for(int i=1;i<100000000;i++){
            multiply(i,a,digits,rem);
            int flag=0;
            for(int j=0;j<10;j++){
                if(rem[j]>0){
                    flag=1;
                }
            }
            if(flag==0){
                out<<"Case #"<<ccount<<": ";
                printd(i,a,digits);
                out<<endl;
                break;
            }
        }
        ccount++;
    }
    return 0;
}
