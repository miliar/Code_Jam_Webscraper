/*
ID: alexlin1
PROG: magic
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
    int row; int swag;
    cin >> row;
    for (int i=0;i<(row-1) * 4;i++){
        cin >> swag;
    }
    int a[4];
    for (int i=0;i<4;i++) cin >> a[i];
  //  for (int i=0;i<4;i++) cout << a[i];
    for (int i=0;i<16 - row * 4;i++) cin >> swag;
    
    cin >> row;
    
    for (int i=0;i<(row-1) * 4;i++) cin >> swag;
    int b=0, c=0, d=0;
    
    for (int i=0;i<4;i++){
        cin >> b; //cout << b << " ";
        for (int j=0;j<4;j++){
            if (b == a[j]){ c = b; d++;}
        }
    }
    //cout << "\n";
    
    for (int i=0;i<16 - row * 4;i++) cin >> swag;
    
    if (d == 0) return -1;
    else if (d > 1) return 0;
    else return c;
    
}

int main() {
	if (fopen("magic.in","r")) {
		freopen("magic.in","r",stdin);
		freopen("magic.out","w",stdout);
	}
	
    int N;
    cin >> N;
    int a;
    for (int i=0;i<N;i++){
        a = solve();
        cout << "Case #" << i + 1 << ": ";
        if (a == -1) cout << "Volunteer cheated!\n";
        else if (a == 0) cout << "Bad magician!\n";
        else cout << a << "\n";
        
    }
    
}