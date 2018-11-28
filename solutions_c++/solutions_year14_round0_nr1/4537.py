// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	vector<int> fila1;
	int t,c,f,num, f_num, mycount, app(0), found_num, i(0);

	cin >> t;
	while( t--)
	{	
			cin.ignore();
			cin.clear();

			cin >> f_num;
			c = f = 0;
			while(f != 4 && cin >> num)
			{
				if (f == f_num-1) fila1.push_back(num);
				if (c == 3) c=-1, f++;		

				c++;
			}
			
			c = f = 0;
			cin >> f_num;
			while(f != 4 && cin >> num)
			{
				if (f == f_num-1)
				{
					mycount = count(fila1.begin(), fila1.end(), num);
					if( mycount >= 1) app++, found_num = num;
				}
				if (c == 3) c=-1, f++;		
				c++;
			}

			if( app == 1 )
				{
					vector<int>::iterator it = std::search_n (fila1.begin(), fila1.end(), 1, found_num);
					cerr << "Case #" << i+1 << ": " << fila1[(it-fila1.begin())] << endl;					
			}
			else if( app > 1 )
					cerr << "Case #" << i+1 << ": " << "Bad magician!" << endl;
			else
					cerr << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;		

			fila1.clear(), app = 0, i++;
				
	}

	cin.ignore();
	cin.clear();

	cin.get();

	return 0;
}

