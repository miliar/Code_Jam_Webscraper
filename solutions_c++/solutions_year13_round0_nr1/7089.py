#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char table[10][10];

inline void get_input()
{
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            cin >> table[i][j];
    return;
}


string check()
{
    int free = 0;
    int row[10][3];
    int col[10][3];

    int diag1[3];
    int diag2[3];


    for(int i=0; i<10; i++)
		for(int j=0; j<4; j++)
	{
		row[i][j] = 0;
		col[i][j] = 0;
		diag1[j] = 0;
		diag2[j] = 0;
	}


    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if (table[i][j] == '.')
                free ++;
            else if (table[i][j] == 'T')
            {
                row[i][0]++;
                col[j][0]++;
            }
            else if (table[i][j] == 'X')
            {
                row[i][1]++;
                col[j][1]++;
            }
            else if (table[i][j] == 'O')
            {
                row[i][2] ++;
                col[j][2] ++;
            }
        }
    }

    for(int i=0; i<4; i++)
    {
        if (table[i][i] == 'T')
            diag1[0]++;
        else if (table[i][i] == 'X')
            diag1[1]++;
        else if (table[i][i] == 'O')
            diag1[2]++;
    }
    for(int i=0; i<4; i++)
    {
        if (table[i][3-i] == 'T')
            diag2[0]++;
        else if (table[i][3-i] == 'X')
            diag2[1]++;
        else if (table[i][3-i] == 'O')
            diag2[2]++;
    }




//    cerr << endl << endl;
//    cerr << "free : " << free << endl;
//    cerr << "T  X  O" << endl;
//    for(int i=0; i<4; i++)
//		cerr << row[i][0] << " " << row[i][1] << " " << row[i][2] << endl;
//	cerr << endl;
//	for(int i=0; i<4; i++)
//			cerr << col[i][0] << " " << col[i][1] << " " << col[i][2] << endl;
//	cerr << endl;
//	cerr << diag1[0] << " " << diag1[1] << " " << diag1[2] << endl;
//	cerr << diag2[0] << " " << diag2[1] << " " << diag2[2] << endl;
//	cerr << endl << endl;;


    for(int i=0; i<4; i++)
    {
        if (col[i][1] == 4 || (col[i][1] == 3 && col[i][0] == 1)) return "X won";
        if (col[i][2] == 4 || (col[i][2] == 3 && col[i][0] == 1)) return "O won";
        if (row[i][1] == 4 || (row[i][1] == 3 && row[i][0] == 1)) return "X won";
        if (row[i][2] == 4 || (row[i][2] == 3 && row[i][0] == 1)) return "O won";
    }
    if (diag1[1] == 4 || (diag1[1] == 3 && diag1[0] == 1)) return "X won";
    if (diag1[2] == 4 || (diag1[2] == 3 && diag1[0] == 1)) return "O won";
    if (diag2[1] == 4 || (diag2[1] == 3 && diag2[0] == 1)) return "X won";
    if (diag2[2] == 4 || (diag2[2] == 3 && diag2[0] == 1)) return "O won";


    if (free) return "Game has not completed";
    return "Draw";




}

int main()
{
	freopen("1.txt", "r", stdin);
	freopen("1_out.txt", "w", stdout);
    int n;
    cin >> n;
    for(int i=0; i<n; i++)
    {
        get_input();
        cout << "Case #" << i+1 << ": " << check() << endl;
    }
    return 0;
}
