

//#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>
#include <set>

int y[10];

void fun(long long int a){
    while (a>0){
        y[a%10]=1;
        a=a/10;
    }
}
using namespace std;
int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
    long long int a;
    int t;
    cin >> t;
    for (int k = 0; k < t; ++k){
        cin >> a;
        for (int i = 0; i < 10; ++i){
            y[i]=0;
        }
        cout << "CASE #"<< k+1 << ": ";
        int n = 10000;
        bool pr = 0;
        for (int i = 1; i < n && !pr; ++i){
            long long int h = a*i;
            fun(h);
            int count = 0;
            for (int j = 0; j < 10; ++j){
                count += y[j];
            }
            if (count == 10){
                cout << h << endl;
                pr = 1;
            }
        }
        if (!pr) {
            cout << "INSOMNIA" << endl;
        }
    }
    return 0;
    
}