#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>




int 
main()
{
    using namespace std;

    int nb_cas;

    cin >> nb_cas;
    for(int cas = 0; cas < nb_cas; cas++)
    {
	cout << "Case #" << cas+1 << ": ";
	int map[4][4];

	int line_0[4] = {0,0,0,0};
	int col_0[4] = {0,0,0,0};
	int line_1[4] = {0,0,0,0};
	int col_1[4] = {0,0,0,0};
		
	int diag1_0= 0;
	int diag2_0= 0;
	int diag1_1= 0;
	int diag2_1= 0;
 
	int not_done = 0;
	bool is_T = false;

	int col_t = -1;
	int line_t = -1;
	bool diag_t1=false;
	bool diag_t2=false;

	for(int i = 0; i<4; i++)
	{
	    for(int j =0; j<4; j++)
	    {
		char c;
		cin >> c;
		if(c == '.')
		{
		    map[i][j] = -1;		   
		    not_done ++;
		}
		else if(c == 'T')
		{
		    map[i][j] = 3;
		    line_t = i;		    
		    col_t  = j;
		    is_T = true;
		}
		else if(c == 'X')
		{
		    line_1[i] ++;
		    col_1[j]  ++;
		    map[i][j] = 1;
		    if(i == j)
		    {
			diag1_1 ++;
		    }
		    if(i+j == 3)
		    {
			diag2_1 ++;
		    }
		}
		else if(c == 'O')
		{
		    line_0[i] ++;
		    col_0[j]  ++;
		    map[i][j] = 0;
		    if(i == j)
		    {
			diag1_0 ++;
		    }
		    if(i+j == 3)
		    {
			diag2_0 ++;
		    }

		}
	    }
	}
	if(col_t != -1 && line_t != -1)
	{
	    if(col_t == line_t)
	    {
		diag_t1 = true;
	    }
	    if(col_t + line_t == 3)
	    {
		diag_t2 = true;
	    }
	}
	
	int winner = -1;

	for(int i =0; i<4; i++)
	{
	    if(col_0[i] == 4 || (col_0[i] == 3 && col_t == i))
	    {
		winner = 0;
		//cerr << "0 win col" << i << endl;
		break;
	    }
	    if(col_1[i] == 4 || (col_1[i] == 3 && col_t == i))
	    {
		winner = 1;
		//cerr << "X win col" << i << endl;
		break;
	    }
	    if(line_0[i] == 4 || (line_0[i] == 3 && line_t == i))
	    {
		winner = 0;
		//cerr << "0 win line" << i << endl;
		break;
	    }
	    if(line_1[i] == 4 || (line_1[i] == 3 && line_t == i))
	    {
		winner = 1;
		//cerr << "X win line" << i << endl;
		break;
	    }
	}
	if(winner == -1) // check diagonal
	{
	    if((diag1_1 == 4 || (diag1_1 == 3 && diag_t1)) || (diag2_1 == 4 || (diag2_1 == 3 && diag_t2))) 
	    {
		winner = 1;
		if(diag1_1 == 4)
		{
		    //cerr << "X win diag1" << endl;
		}
		if(diag1_1 == 3 && diag_t1)
		{
		    //cerr << "X win diag2" << endl;
		}
		if(diag2_1 == 4)
		{
		    //cerr << "X win diag3" << endl;
		}
		if(diag2_1 == 3 && diag_t2)
		{
		    //cerr << "X win diag4" << endl;	       
		}
	    }
	    if((diag1_0 == 4 || (diag1_0 == 3 && diag_t1)) || (diag2_0 == 4 || (diag2_0 == 3 && diag_t2))) 
	    {
		//cerr << "0 win diag"  << endl;
		winner = 0;
	    }
	}

	switch (winner)
	{
	case -1:
	    if(not_done > 0)
		cout << "Game has not completed";
	    else 
		cout << "Draw";	    
	    break;
	case 0:
	    cout << "O won";
	    break;
	case 1:
	    cout << "X won";
	    break;
	}
	cout << endl;
    }
    
    return 0;
}
