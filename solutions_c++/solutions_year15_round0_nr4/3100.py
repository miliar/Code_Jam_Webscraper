#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 0; i<t;i++){
        int X,R,C;
        cin >> X >> R >> C;

        cout << "Case #" << i+1 << ": ";
		
		if(
		  (max(R,C) < X) ||
		  (X != 2 && ((X / 2 + 1) > min(R,C))) ||
		  (((R * C) % X) != 0)
		  )
		  	cout << "RICHARD" << endl;
		else
			cout << "GABRIEL" << endl; 		
    }
	return 0;
}
