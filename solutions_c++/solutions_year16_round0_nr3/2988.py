#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

void print(long long a){
    vector<long long>dig;
    while(a){
        dig.push_back(a%2);
        a >>=1;
    }
    for(int i=dig.size()-1; i>=0; --i)
        cout << dig[i];
    cout << " ";
    return;
}

long long isprime(long long a, long long b){
    if(a == 1) return -1;
    for(long long i=2; i*i <=a; ++i)
        if(a%i == 0 && i!= b) return i;
    return -1;
}

int main()
{
    freopen("C-small-attempt4.in","r",stdin);
    freopen("cout1.txt","w",stdout);
    int t;
    cin >> t;
    cout << "Case #1:" << endl;
    long long n, j;
    cin >> n >> j;
    for(long long i=(1 << (n-1)); i<(1<<n) && j; ++i){
        int b= i&1;
        if(b == 0) continue;
        bool works = true;
        vector<long long>div;
        for(long long base =2; base <= 10; ++base){
            long long temp = i, pow=1, num=0;
            while(temp){
                if(temp&1){
                    num += pow;
                }
                pow *= base;
                temp >>=1;
            }
            long long a = isprime(num, base);
            if(a == -1){
                works = false;
                break;
            } else {
                div.push_back(a);
            }
        }
        if(works){
            --j;
            //cout << i << endl;
            print(i);
            for(int k=0; k<div.size(); ++k)
                cout << div[k] << " ";
            cout << endl;
        }
    }
}
