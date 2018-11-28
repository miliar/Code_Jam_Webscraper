#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	
	for(int Barti = 1; Barti <= T; Barti++)
	{
		int N;
		cin >> N;

		string X, Y;
		cin >> X >> Y;
		
		bool kolejnosc = true;
		
		string M = "", NN = "";
		
		M += X[0], NN += Y[0];
		
		for(int i = 1; i < X.size(); i++)
		{
			if(X[i] != X[i - 1])
				M += X[i];	
		}
		
		for(int i = 1; i < Y.size(); i++)
		{
			if(Y[i] != Y[i - 1])
				NN += Y[i];	
		}
	
		if(M == NN)
			kolejnosc = true;
		else
			kolejnosc = false;
		
		cout << "Case #" << Barti << ": ";
		
		if(kolejnosc == false)
		{
			cout << "Fegla Won";
		}
		else
		{
			
			int WYNIK = 0;
			//mamy M bedzimey liczyc ile kolejno znakow w X i Y i odejmowac 
			
			int sX = 0;
			int sY = 0;
			
			for(int i = 0; i < M.size(); i++)
			{
				char szukany = M[i];
				
				int ileX = 0, ileY = 0;
				
				while(sX < X.size() && X[sX] == szukany)
				{
					ileX++;
					sX++;
				}
				
				while(sY < Y.size() && Y[sY] == szukany)
				{
					ileY++;
					sY++;
				}
				
				WYNIK += abs(ileX - ileY);
			}
			
			
			cout << WYNIK;
		}
		
		cout << endl;
	}

	return 0;
}

