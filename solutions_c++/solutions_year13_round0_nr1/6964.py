#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int N;
	in>>N;

	for ( int n = 0; n < N; n++){
        bool Complete = true;
		char TT[4][4];
		for ( int i = 0; i < 4; i++){
			for ( int j = 0; j <4;j++){
				in>>TT[i][j];
				if (TT[i][j] == '.')
                    Complete= false;
			}
		}

        bool next =  false;

		for ( int i = 0; i < 4; i++){
			bool win = true;
			for ( int j = 0; j < 4; j++) {
				if (TT[i][j] != 'T' and TT[i][j] != 'X'){
					win = false;
					break;
				}
			}
			if (win){
                out<<"Case #"<<n+1<<": X won"<<endl;
                next =  true;
                break;
			}
		}

        if (next)
            continue;

        for ( int i = 0; i < 4; i++){
			bool win = true;
			for ( int j = 0; j < 4; j++) {
				if (TT[i][j] != 'T' and TT[i][j] != 'O'){
					win = false;
					break;
				}
			}
			if (win){
                out<<"Case #"<<n+1<<": O won"<<endl;
                next =  true;
                break;
			}
		}

		if (next)
            continue;

        for ( int i = 0; i < 4; i++){
			bool win = true;
			for ( int j = 0; j < 4; j++) {
				if (TT[j][i] != 'T' and TT[j][i] != 'O'){
					win = false;
					break;
				}
			}
			if (win){
                out<<"Case #"<<n+1<<": O won"<<endl;
                next =  true;
                break;
			}
		}

		if (next)
            continue;

        for ( int i = 0; i < 4; i++){
			bool win = true;
			for ( int j = 0; j < 4; j++) {
				if (TT[j][i] != 'T' and TT[j][i] != 'X'){
					win = false;
					break;
				}
			}
			if (win){
                out<<"Case #"<<n+1<<": X won"<<endl;
                next =  true;
                break;
			}
		}
		if (next)
            continue;

        bool win = true;
		for ( int i = 0; i < 4; i++){

				if (TT[i][i] != 'T' and TT[i][i] != 'O'){
					win = false;
					break;
				}

		}
        if (win){
                out<<"Case #"<<n+1<<": O won"<<endl;
                continue;
        }

        win = true;
		for ( int i = 0; i < 4; i++){

				if (TT[i][3-i] != 'T' and TT[i][3-i] != 'X'){
					win = false;
					break;
				}

		}
        if (win){
                out<<"Case #"<<n+1<<": X won"<<endl;
                continue;
        }

                win = true;

		for ( int i = 0; i < 4; i++){

				if (TT[i][3-i] != 'T' and TT[i][3-i] != 'O'){
					win = false;
					break;
				}

		}
        if (win){
                out<<"Case #"<<n+1<<": O won"<<endl;
                continue;
        }

        win = true;
		for ( int i = 0; i < 4; i++){

				if (TT[i][i] != 'T' and TT[i][i] != 'X'){
					win = false;
					break;
				}

		}
        if (win){
                out<<"Case #"<<n+1<<": X won"<<endl;
                continue;
        }
        if (Complete)
            out<<"Case #"<<n+1<<": Draw"<<endl;
        else
            out<<"Case #"<<n+1<<": Game has not completed"<<endl;

	}
    in.close();
    out.close();
}
