//============================================================================
// Name        : CodeJam.cpp
// Author      : test
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main()
{
    // Load cases
	int cases = 0;
	cin >> cases;


	char currentCase[4][4];
	for(int i = 0; i < cases; ++i)
	{
	    // Load case
	    char buffer = 0;
	    int emptyFields = 0;
	    for(int row = 0; row < 4; ++row)
	    {
	        for(int col = 0; col < 4; ++col)
	        {
	            cin >> buffer;
	            currentCase[row][col] = buffer;
	            if(buffer == '.')
	            {
	                ++emptyFields;
	            }
	        }
	    }
	    bool determined = false;
	    // Check for row winning
	    for(int row = 0; row < 4; ++row)
	    {
	        int Xs = 0;
	        int Ys = 0;
	        int Ts = 0;
	        for(int col = 0; col < 4; ++col)
	        {
	            switch(currentCase[row][col])
	            {
	            case 'X':
	                ++Xs;
	                break;
	            case 'O':
	                ++Ys;
	                break;
	            case 'T':
	                ++Ts;
	                break;
	            default:
	                break;
	            }
	        }
	        if(Xs == 4 || (Xs == 3 && Ts == 1))
	        {
	            cout << "Case #" << (i + 1) << ": X won" << endl;
	            determined = true;
	            break;
	        }
	        if(Ys == 4 || (Ys == 3 && Ts == 1))
	        {
                cout << "Case #" << (i + 1) << ": O won" << endl;
                determined = true;
                break;
	        }
	    }
	    if(determined) continue;
	    // Check for column winning
        for(int col = 0; col < 4; ++col)
        {
            int Xs = 0;
            int Ys = 0;
            int Ts = 0;
            for(int row = 0; row < 4; ++row)
            {
                switch(currentCase[row][col])
                {
                case 'X':
                    ++Xs;
                    break;
                case 'O':
                    ++Ys;
                    break;
                case 'T':
                    ++Ts;
                    break;
                default:
                    break;
                }
            }
            if(Xs == 4 || (Xs == 3 && Ts == 1))
            {
                cout << "Case #" << (i + 1) << ": X won" << endl;
                determined = true;
                break;
            }
            if(Ys == 4 || (Ys == 3 && Ts == 1))
            {
                cout << "Case #" << (i + 1) << ": O won" << endl;
                determined = true;
                break;
            }
        }
        if(determined) continue;
	    // Check for \ winning
		{
            int Xs = 0;
            int Ys = 0;
            int Ts = 0;
			for(int j = 0; j < 4; ++j)
			{
                switch(currentCase[j][j])
                {
                case 'X':
                    ++Xs;
                    break;
                case 'O':
                    ++Ys;
                    break;
                case 'T':
                    ++Ts;
                    break;
                default:
                    break;
                }
            }
			
            if(Xs == 4 || (Xs == 3 && Ts == 1))
            {
                cout << "Case #" << (i + 1) << ": X won" << endl;
                determined = true;
            }else if(Ys == 4 || (Ys == 3 && Ts == 1))
            {
                cout << "Case #" << (i + 1) << ": O won" << endl;
                determined = true;
            }
		}
        if(determined) continue;
	    // Check for / winning
		{
            int Xs = 0;
            int Ys = 0;
            int Ts = 0;
			for(int j = 0; j < 4; ++j)
			{
                switch(currentCase[3 - j][j])
                {
                case 'X':
                    ++Xs;
                    break;
                case 'O':
                    ++Ys;
                    break;
                case 'T':
                    ++Ts;
                    break;
                default:
                    break;
                }
            }
			
            if(Xs == 4 || (Xs == 3 && Ts == 1))
            {
                cout << "Case #" << (i + 1) << ": X won" << endl;
                determined = true;
            }else if(Ys == 4 || (Ys == 3 && Ts == 1))
            {
                cout << "Case #" << (i + 1) << ": O won" << endl;
                determined = true;
            }
		}
        if(determined) continue;
	    // Draw/nobody wins
	    if(emptyFields > 0)
	    {
	        cout << "Case #" << (i + 1) << ": Game has not completed" << endl;
	    }else
	    {
	        cout << "Case #" << (i + 1) << ": Draw" << endl;
	    }
	}
	return 0;
}
