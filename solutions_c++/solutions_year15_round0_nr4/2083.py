#include <iostream>

using namespace std;

int main(){
	
	int T;
	cin >> T;

	for (int i=1; i<=T; i++){
		
		int X,R,C;
		cin >> X >> R >> C;
		bool richard;
		
		if (X>R && X>C){
			richard = true;
		}		
		
		else if (X==1){
			richard = false;
		}

		else if (X==2){
			if ((R*C)%X!=0)
				richard = true;
			else
				richard = false;	
		
		}

		else if (X==3){
			if ((R*C)%X!=0)
				richard = true;
			else
				if (R==1 || C==1) richard=true;
				else richard = false;
		}

		else if (X==4){
			if ((R*C)%X!=0) richard = true;
			else 
				if (R==1 || C==1) richard=true;
				else if (R==2 || C==2) richard=true;
				else richard = false;
		}

		if (richard) cout << "Case #" << i << ": RICHARD" << endl;
		else cout << "Case #" << i << ": GABRIEL" << endl;
	}


	return 0;
}
