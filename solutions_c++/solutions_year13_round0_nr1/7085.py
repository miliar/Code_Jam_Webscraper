# include <iostream>
# include <vector>
# include <fstream>
# include <string>


using namespace std;

int check_diags(vector <string> inp) {
    int i = 0;
    if ((inp[0][0] == 'X' || inp[0][0] == 'T') && (inp[1][1]=='X' || inp[1][1] == 'T') && (inp[2][2] =='X' || inp[2][2] == 'T') && (inp[3][3] == 'X' || inp[3][3] == 'T'))
	return 1;
    else if ((inp[i+0][i+0] == 'O' || inp[i+0][i+0] == 'T') && (inp[i+1][i+1]=='O' || inp[i+1][i+1] == 'T') && (inp[i+2][i+2] =='O' || inp[i+2][i+2] == 'T') && (inp[i+3][i+3] == 'O' || inp[i+3][i+3] == 'T'))
	return 2;
    else if ((inp[0][3] == 'X' || inp[0][3] == 'T') && (inp[1][2]=='X' || inp[1][2] == 'T') && (inp[2][1] =='X' || inp[2][1] == 'T') && (inp[3][0] == 'X' || inp[3][0] == 'T'))
	return 1;
    else if ((inp[0][3] == 'O' || inp[0][3] == 'T') && (inp[1][2]=='O' || inp[1][2] == 'T') && (inp[2][1] =='O' || inp[2][1] == 'T') && (inp[3][0] == 'O' || inp[3][0] == 'T'))
	return 2;
    return 0;
}

int check_row(vector <string> inp) {
    for (int i = 0; i < 4; i++) {
	if ((inp[i][0] == 'X' || inp[i][0] == 'T') && (inp[i][1]=='X' || inp[i][1] == 'T') && (inp[i][2] =='X' || inp[i][2] == 'T') && (inp[i][3] == 'X' || inp[i][3] == 'T'))
	    return 1;
	else if ((inp[i][0] == 'O' || inp[i][0] == 'T') && (inp[i][1]=='O' || inp[i][1] == 'T') && (inp[i][2] =='O' || inp[i][2] == 'T') && (inp[i][3] == 'O' || inp[i][3] == 'T'))
	    return 2;
    }
    return 0;
}

int check_col(vector <string> inp) {
    for (int i = 0; i < 4; i++) {
	if ((inp[0][i] == 'X' || inp[0][i] == 'T') && (inp[1][i]=='X' || inp[1][i] == 'T') && (inp[2][i] =='X' || inp[2][i] == 'T') && (inp[3][i] == 'X' || inp[3][i] == 'T'))
	    return 1;
	else if ((inp[0][i] == 'O' || inp[0][i] == 'T') && (inp[1][i]=='O' || inp[1][i] == 'T') && (inp[2][i] =='O' || inp[2][i] == 'T') && (inp[3][i] == 'O' || inp[3][i] == 'T'))
	    return 2;
    }
    return 0;
}

int main() {
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    int dflag = 1;
    int cflag = 1;
    int pflag = 0;
    int Ti=0;
    while (Ti++ < T) {
	pflag = 0;
	vector <string> inp;
	for (int i = 0; i < 4; i++)  {
	    string temp;
	    cin >> temp;
	    inp.push_back(temp);
	    if (temp.find(".",0)!= string::npos) {
		pflag = 1;
	    }
	}
	int result=0;
	result = check_diags(inp);
	if (result == 0) result = check_row(inp);
	if (result == 0) result = check_col(inp);
	switch (result) {
	    case 1:
		// X wins
		cout << "Case #"<<Ti<<": X won\n";
		break;
	    case 2:
		// O wins
		cout << "Case #"<<Ti<<": O won\n";
		break;
	    default:
		if (pflag) {
		    cout << "Case #"<<Ti<<": Game has not completed\n";
		}
		else {
		    cout << "Case #"<<Ti<<": Draw\n";
		}
	}
    }
    return 0;
}
