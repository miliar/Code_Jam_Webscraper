#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main (){
	

    int N;
	cin >> N;
	for (int i =0; i < N; i++){
        int a,x,y;
        cin >> a >> x >> y;
        if ((a == 1 || (a==2 && max(x,y) >= 2) ||
                (max(x,y) >= a && min(x,y) >= a-1)) && x*y % a == 0)
            cout << "Case #" << (i + 1) << ": GABRIEL" <<  '\n';
        else
            cout << "Case #" << (i + 1) << ": RICHARD" <<  '\n';
	}
	return 0;			
}

