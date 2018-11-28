#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int mx[8]={1, 1, -1, -1, 0, 0, 1, -1}, my[8]={1, -1, 1, -1, 1, -1, 0, 0};

int main(){
    freopen ("in.txt", "r", stdin); freopen ("out.txt", "w", stdout);

    int t, n;
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> n;
        vector <double> a, b, tempA, tempB; double in;
        for (int j = 0; j < n; j++, a.push_back(in)) cin >> in;
        for (int j = 0; j < n; j++, b.push_back(in)) cin >> in;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        tempA=a, tempB=b;
        //War
        int scoreW=0;
        for (int j = 0; j < n; j++){
            int indA = a.size()-1, indB = b.size()-1;
            if (a[indA]<b[indB]){a.erase(a.end()-1); b.erase(b.end()-1);}
            else {
                scoreW++;
                a.erase(a.end()-1); b.erase(b.begin());
            }
        }
        //DWar
        int scoreDW=0;
        a=tempA, b=tempB;
        for (int j = 0; j < n; j++){
            int indA=a.size()-1, indB=b.size()-1;
            if (a[indA]>b[indB]){scoreDW++; a.erase(a.end()-1); b.erase(b.end()-1);}
            else{
                if (a[0]>=b[indB]) scoreDW++;
                a.erase(a.begin()); b.erase(b.end()-1);
            }
        }

        cout << "Case #" << i+1 << ": " << scoreDW << " " << scoreW << endl;
    }

    return 0;
}
