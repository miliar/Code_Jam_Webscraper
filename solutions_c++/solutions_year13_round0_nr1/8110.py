#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

char a[4][4];
ofstream fout("out.txt");
int nr = 0;

bool in_matrix(int i, int j) {
    return i >= 0 && j >= 0 && i < 4 && j < 4;
}

bool check_win(int count_x, int count_o, bool found_t) {

    if(count_x == 3 || count_o == 3) {
        if(found_t == true) {
            char c = (count_x == 3)? 'X' : 'O';
            fout << "Case #" << nr <<": " << c << " won\n";
            return true;
        }

    } else if(count_x == 4 || count_o == 4) {
        char c = (count_x == 4)? 'X' : 'O';
        fout << "Case #" << nr <<": " << c << " won\n";
        return true;
    }

    return false;
}


void solve() {
	int count_x = 0, count_o = 0, x, y;
	bool found_t = false;
    bool found_dot = false;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j) {
            if(a[i][j] == '.')
                found_dot = true;
            found_t = false ;
            count_x = count_o = 0;
            x = i, y = j;
            while(in_matrix(x, y)) {
                if(a[x][y] == 'T') {
                    if(count_x != 3)
                        count_x = 0;
                    if(count_o != 3)
                        count_o = 0;
                    found_t = true;
                }else if(a[x][y] == 'O')
                    count_o++;
                else if(a[x][y] == 'X')
                    count_x++;
                y++;
            }
            if(check_win(count_x, count_o, found_t))
                return;

            found_t = false ;
            count_x = count_o = 0;
            x = i, y = j;
            while(in_matrix(x, y)) {
                if(a[x][y] == 'T') {
                    if(count_x != 3)
                        count_x = 0;
                    if(count_o != 3)
                        count_o = 0;
                    found_t = true;
                }else if(a[x][y] == 'O')
                    count_o++;
                else if(a[x][y] == 'X')
                    count_x++;
                x++;
            }
            if(check_win(count_x, count_o, found_t))
                return;

            found_t = false ;
            count_x = count_o = 0;
            x = i, y = j;
            while(in_matrix(x, y)) {
                if(a[x][y] == 'T') {
                    if(count_x != 3)
                        count_x = 0;
                    if(count_o != 3)
                        count_o = 0;
                    found_t = true;
                }else if(a[x][y] == 'O')
                    count_o++;
                else if(a[x][y] == 'X')
                    count_x++;
                x++; y++;
            }
            if(check_win(count_x, count_o, found_t))
                return;

            found_t = false ;
            count_x = count_o = 0;
            x = i, y = j;
            while(in_matrix(x, y)) {
                if(a[x][y] == 'T') {
                    if(count_x != 3)
                        count_x = 0;
                    if(count_o != 3)
                        count_o = 0;
                    found_t = true;
                }else if(a[x][y] == 'O')
                    count_o++;
                else if(a[x][y] == 'X')
                    count_x++;
                x--; y++;
            }
            if(check_win(count_x, count_o, found_t))
                return;

		}
    if(found_dot == true)
        fout << "Case #" << nr <<": Game has not completed\n";
    else
        fout << "Case #" << nr <<": Draw\n";

}

void input() {
    int T;
	ifstream fin("in.txt");
	fin >> T;
	for(int k = 0; k < T; ++k) {
        ++nr;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				fin >> a[i][j];
		solve();
		fin.get();
	}
}

int main(int argc, char* argv[]) {

	input();


	return 0;
}

