#include <iostream>
#include <string>

using namespace std;

int main (void)
{
	int num;
	cin >> num;
	
	char puzzle[4][4];
	
	int x,y,k;
	for (x=0;x<num;x++){
		for (y=0;y<4;y++)
			for (k=0;k<4;k++)
				cin >> puzzle[y][k];
		
		bool Xwon=false, Owon=false, Full=true;
		int XPoints=0,OPoints=0,TPoints=0,DPoints=0;
		
		for (y=0;y<4;y++){
			for (k=0;k<4;k++){
				if (puzzle[y][k]=='X') XPoints++;
				if (puzzle[y][k]=='O') OPoints++;
				if (puzzle[y][k]=='T') TPoints++;
				if (puzzle[y][k]=='.') DPoints++;
			}
			if (XPoints==4) Xwon=true;
			if (XPoints==3 && TPoints==1) Xwon=true;
			if (OPoints==4) Owon=true;
			if (OPoints==3 && TPoints==1) Owon=true;
			XPoints=0;
			OPoints=0;
			TPoints=0;
		}
		
		if (DPoints>0) Full=false;
		
		for (y=0;y<4;y++){
			for (k=0;k<4;k++){
				if (puzzle[k][y]=='X') XPoints++;
				if (puzzle[k][y]=='O') OPoints++;
				if (puzzle[k][y]=='T') TPoints++;
			}
			if (XPoints==4) Xwon=true;
			if (XPoints==3 && TPoints==1) Xwon=true;
			if (OPoints==4) Owon=true;
			if (OPoints==3 && TPoints==1) Owon=true;
			XPoints=0;
			OPoints=0;
			TPoints=0;
		}
		
		for (k=0;k<4;k++){
			if (puzzle[k][k]=='X') XPoints++;
			if (puzzle[k][k]=='O') OPoints++;
			if (puzzle[k][k]=='T') TPoints++;
		}
		if (XPoints==4) Xwon=true;
		if (XPoints==3 && TPoints==1) Xwon=true;
		if (OPoints==4) Owon=true;
		if (OPoints==3 && TPoints==1) Owon=true;
		XPoints=0;
		OPoints=0;
		TPoints=0;
		
		for (k=0;k<4;k++){
			if (puzzle[k][3-k]=='X') XPoints++;
			if (puzzle[k][3-k]=='O') OPoints++;
			if (puzzle[k][3-k]=='T') TPoints++;
		}
		if (XPoints==4) Xwon=true;
		if (XPoints==3 && TPoints==1) Xwon=true;
		if (OPoints==4) Owon=true;
		if (OPoints==3 && TPoints==1) Owon=true;
		XPoints=0;
		OPoints=0;
		TPoints=0;
		
		
		if (Xwon) cout << "Case #" << x+1 << ": X won" << endl;
		else {
			if (Owon) cout << "Case #" << x+1 << ": O won" << endl;
			else {
				if (Full) cout << "Case #" << x+1 << ": Draw" << endl;
				else cout << "Case #" << x+1 << ": Game has not completed" << endl;
			}
		}

		Full=true;
		Xwon=false;
		Owon=false;
		
	}
	
	return 0;
}
