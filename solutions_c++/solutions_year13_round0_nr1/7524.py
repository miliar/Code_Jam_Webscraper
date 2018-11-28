#include <iostream>
#include <string>
#define case1 "X won"
#define case2 "O won"
#define case3 "Draw"
#define case4 "Game has not completed"

using namespace std;

void result(int case_n, int c)
{
	switch (c)
	{
	    case 1:
	       cout << "Case #" << case_n << ": " << case1 << endl;
		   break;
		case 2:
	       cout << "Case #" << case_n << ": " << case2 << endl;
		   break;
		case 3:
	       cout << "Case #" << case_n << ": " << case3 << endl;
		   break;
        case 4:
	       cout << "Case #" << case_n << ": " << case4 << endl;
		   break;
	}
}

int main()
{
	const int MAXITEMS = 4;
	int t, c = 1; string line;

	cin >> t;
	getchar();
	while (t--)
	{
        bool _dot = false, _won = false;
		string _s; int _sc = 0;
		string items[MAXITEMS] = {};
		
		for (int i=0;i<5;i++)
		{
			getline(cin,line);
			//cout << line << endl;
			if (!line.empty()) {
			    items[i] = line;  	
			}	
		}

		for (int z = 0; z < MAXITEMS; z++)
        {
			int _xc = 0, _oc = 0, _tc = 0, _dc = 0;
            for (int i = 0;i<MAXITEMS;i++)
			{	                
				_s[_sc] = items[z][i];				
				_sc++;
				
			    switch (items[z][i])
				{
					case 'X':
						_xc++;
						break;
				    case 'O':
                        _oc++;
                        break;
				    case 'T':
						_tc++;
                        break;
				    case '.':
						_dc++;
					    _dot = true;
				}
				
			}
			
			// horizontal check
            if (_xc >=3 && _oc == 0 && _dc == 0)
			{
				_won = true;
				result(c, 1);
				break;
			}
            else if (_oc >=3 && _xc == 0 && _dc == 0)
			{
                _won = true;
				result(c, 2);
				break;
			}				
		}	

		// vertical check
		if (_won == false)
		{
			for (int i = 0;i<MAXITEMS;i++)
			{
				int _xc = 0, _oc = 0, _tc = 0, _dc = 0;
				for (int z=(i+0); z <= (16-MAXITEMS+i); z+=4)
				{
					switch (_s[z])
				    {
					    case 'X':
						  _xc++;
						  break;
				        case 'O':
                          _oc++;
                          break;
					    case 'T':
						  _tc++;
                          break;
				        case '.':
						  _dc++;
					      _dot = true;	 
				    }
				}

                if (_xc >=3 && _oc == 0 && _dc == 0)
			    {
				    _won = true;
				    result(c, 1);
				    break;
			    }
                else if (_oc >=3 && _xc == 0 && _dc == 0)
			    {
                    _won = true;
				    result(c, 2);
				    break;
			    }				
			}
		}
		
		// DIAGONAL CHECK
        if (_won == false)
		{
			// left
			int _xc = 0, _oc = 0, _tc = 0, _dc = 0;
			for (int z=0; z <= 15; z+=5)
			{
				switch (_s[z])
			    {
				    case 'X':
						_xc++;
						break;
					case 'O':
						_oc++;
						break;
					case 'T':
						_tc++;
						break;
					case '.':
						_dc++;
						_dot = true;	 
						break;
				}
			}
			
			if (_xc >=3 && _oc == 0 && _dc == 0)
			{
				_won = true;
				result(c, 1);
			}
			else if (_oc >=3 && _xc == 0 && _dc == 0)
			{
				_won = true;
				result(c, 2);
			}	
			
			// right
			_xc = 0, _oc = 0, _tc = 0, _dc = 0;
			for (int u=3; u <= 12; u += 3)
			{
				switch (_s[u])
			    {
				    case 'X':
						_xc++;
						break;
					case 'O':
						_oc++;
						break;
					case 'T':
						_tc++;
						break;
					case '.':
						_dc++;
						_dot = true;	
                        break;						
				}
			}
			
			if (_xc >=3 && _oc == 0 && _dc == 0)
			{
				_won = true;
				result(c, 1);
			}
			else if (_oc >=3 && _xc == 0 && _dc == 0)
			{
				_won = true;
				result(c, 2);
			}	
			
		}
				
		if (_won == false && _dot == true)
			result(c, 4);
		else if (_won == false && _dot == false)
			result(c, 3);
		
        c++;
	}
		
	return 0;
}
