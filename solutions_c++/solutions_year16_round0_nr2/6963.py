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

string pReverse(string s,int a,int b){
    for(int i=a;i<=b;i++){
        if(s[i]=='+') s[i]='-';
        else if(s[i]=='-') s[i]='+';
    }
    while(a<=b){
        char temp;
        temp = s[a];
        s[a] = s[b];
        s[b] = temp;
        a++;
        b--;
    }
    return s;
}

int main(){
    int cases,ccount=1;
    in.open("input.txt");
    out.open("result.txt");
    in>>cases;
    while(ccount<=cases){
        string s;
        in>>s;
        int k=s.length()-1,ans=0;
        while(k>=0){
            if(s[k]=='+'){
                k--;
                continue;
            }
            if(s[0]=='-'){
                s = pReverse(s,0,k);
                ans++;
            }else{
                int i=0;
                while(s[i]=='+'&&i<s.length()){
                    i++;
                }
                s=pReverse(s,0,i-1);
                ans++;
                s=pReverse(s,0,k);
                ans++;
            }
            k--;
        }
        out<<"Case #"<<ccount<<": "<<ans<<endl;
        ccount++;
    }
    return 0;
}
