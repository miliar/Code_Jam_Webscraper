#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	string line;
	cin >> N;

	for (int I=0;I<N;I++){

		vector<bool> ORow = vector<bool>(4,true),
				OCol = vector<bool>(4,true),
				XRow = vector<bool>(4,true),
				XCol = vector<bool>(4,true);
		bool ODiag1 = true,
				ODiag2 = true,
				XDiag1 = true,
				XDiag2 = true,
				Draw = true;

		for (int i=0;i<4;i++){
			cin >> line;
			switch (line[i]){
				case '.':	XDiag1 = false;
				case 'X':	ODiag1 = false;	break;
				case 'O':	XDiag1 = false;
			}
			switch (line[3-i]){
				case '.':	XDiag2 = false;
				case 'X':	ODiag2 = false;	break;
				case 'O':	XDiag2 = false;
			}
			for (int j=0;j<4;j++){
				if (line[j] == '.')
					Draw = false;
				switch (line[j]){
					case '.':	XRow[i] = false; XCol[j] = false;
					case 'X':	ORow[i] = false; OCol[j] = false; break;
					case 'O':	XRow[i] = false; XCol[j] = false;
				}
			}
		}
		bool Xwins=false;
		bool Owins=false;
		for (int i=0;i<4;i++){
			Xwins = Xwins || XRow[i] || XCol[i];
			Owins = Owins || ORow[i] || OCol[i];
		}
		Xwins = Xwins || XDiag1 || XDiag2;
		Owins = Owins || ODiag1 || ODiag2;

		cout << "Case #" << I+1 << ": ";
		if (Xwins)
			cout << "X won" << endl;
		else if (Owins)
			cout << "O won" << endl;
		else if (Draw)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
	return 0;
}
