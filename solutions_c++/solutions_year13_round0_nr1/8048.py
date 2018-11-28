#include <iostream>
#include <string>

using namespace std;

int checkstr(string instr){	
	int rstate = 3;
    bool notmatch = false;
    int i;
	char sstate = instr[0];
	
	if(sstate == '.')
		return rstate;
			
	for(i = 1;i < 4;i++){
        if(sstate == 'T'){
            sstate = instr[1];
            continue;
        }
		if(sstate == instr[i]){
            if(sstate == '.'){
                rstate = 3;
                break;
            }
			rstate = 1;
		}
		else if(instr[i] == 'T'){
			rstate = 1;
		}
		else if(instr[i] == '.'){
			rstate = 3;
			break;
		}
		else{
            rstate = 3;
            sstate = 'v';
            notmatch = true;
			if (i == 3) {
                rstate = 4;
            }
		}
	} 
	
	if(i == 4 && rstate == 1)
		if(sstate == 'X')
			rstate = 2;
    if(notmatch)
            rstate = 5;
    
	return rstate;
}

int main(){
	int ncase,ans;
	bool owin, xwin, notcomp;
    string dummy = "";

	string rowArr[4];
	string colArr[4];
	string digArr[2];	

	cin >> ncase;

	for(int i = 0;i < ncase;i++){
        
        owin = false;
        xwin = false;
        notcomp = false;
        
		for(int j = 0;j < 4;j++){
			cin >> rowArr[j];			
		}

		for(int j = 0;j < 4;j++){
            dummy = "";
            dummy += rowArr[0][j];
            dummy += rowArr[1][j];
            dummy += rowArr[2][j];
            dummy += rowArr[3][j];
			colArr[j] = dummy;
        }
		
        dummy = "";
        dummy += rowArr[0][0];
        dummy += rowArr[1][1];
        dummy += rowArr[2][2];
        dummy += rowArr[3][3];
        digArr[0] = dummy;

        dummy = "";
        dummy += rowArr[0][3];
        dummy += rowArr[1][2];
        dummy += rowArr[2][1];
        dummy += rowArr[3][0];
        digArr[1] = dummy;
        
		for(int j = 0; j < 4;j++){
			ans = checkstr(rowArr[j]);
            if(ans == 1)
				owin = true;
			else if(ans == 2)
				xwin = true;
			else if(ans == 3)
				notcomp = true;
		}

		for(int j = 0;j < 4;j++){
			ans = checkstr(colArr[j]);
            if(ans == 1)
				owin = true;
			else if(ans == 2)
				xwin = true;
			else if(ans == 3)
				notcomp = true;
		}

		for(int j = 0;j < 2;j++){
			ans = checkstr(digArr[j]);
            if(ans == 1)
				owin = true;
			else if(ans == 2)
				xwin = true;
			else if(ans == 3)
				notcomp = true;
		}

		if(owin && xwin){
    			cout << "Case #" << i+1 << ": Draw" << endl;
			continue;
		}
		else if(owin){
			cout << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		else if(xwin){
			cout << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
        else if(!notcomp && !owin && !xwin){
            cout << "Case #" << i+1 << ": Draw" << endl;
			continue;
        }
		else if(notcomp){
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
			continue;
		}	
	}	

	return 0;
}
