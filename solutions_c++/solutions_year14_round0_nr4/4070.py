/*
ID: alexlin1
PROG: war
LANG: C++
*/

#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;

int solve() {
    int N;
    cin >> N;
    
    double a;
    
    vector<double> n1;
    vector<double> n2;
    vector<double> k1;
    vector<double> k2;
    
    for (int i=0;i<N;i++){
        cin >> a;
        n1.push_back(a);
        n2.push_back(a);
    }
    for (int i=0;i<N;i++){
        cin >> a;
        k1.push_back(a);
        k2.push_back(a);
    }
   
    if (N > 1){
        sort(n1.begin(),n1.end());
        sort(k1.begin(),k1.end());
        sort(n2.begin(),n2.end());
        sort(k2.begin(),k2.end());
    }
    /*
    cout << "\n";
    for (int i=0;i<N;i++){
        cout << n1[i] << " ";
    } cout <<"\n";
    for (int i=0;i<N;i++){
        cout << k1[i] << " ";
    } cout << "\n";
   */
    int b;
    int n1score = 0, n2score = 0, k1score = 0, k2score = 0;
    
    for (int i=0;i<N;i++){
        b = -1;
        for (int j=0;j<k1.size();j++){
            if (k1[j] > n1[0]){
                b = j;
                break;
            }
        }
        if (b == -1){
            n1score++;
            k1.erase(k1.begin());
            n1.erase(n1.begin());
        }
        else{
            k1score++;
            k1.erase(k1.begin() + b);
            n1.erase(n1.begin());
        }
    }

    
    for (int i=0;i<N;i++){
        if (n2[0] > k2[0]){
            n2score++;
            n2.erase(n2.begin());
            k2.erase(k2.begin());
        }
        else{
            k2score++;
            k2.erase(k2.begin() + k2.size() - 1);
            n2.erase(n2.begin());
        }
    }
    
    cout << n2score << " " << n1score;
    
    return 0;
}

int main() {
	if (fopen("war.in","r")) {
		freopen("war.in","r",stdin);
		freopen("war.out","w",stdout);
	}
	int N;
    cin >> N;
    for (int i=0;i<N;i++){
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << "\n";
    }
}