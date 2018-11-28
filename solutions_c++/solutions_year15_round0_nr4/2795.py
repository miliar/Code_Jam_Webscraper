#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#define mp make_pair
#define st first
#define nd second
#define ll long long
#define ld long double

using namespace std;
typedef pair <int, int> para;

int main()
{
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		int X, R, C;
		cin >> X >> R >> C;
		
		cout << "Case #" << i << ": ";
		
		if(X == 1)
		{
			cout << "GABRIEL" << endl;
			goto A;
		}
		
		if(X == 2)
		{
			if(R % 2 == 1 && C % 2 == 1)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			else
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
		}
		
		if(X == 3)
		{
			if(R < 3 && C < 3)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			
			if(R * C % 3 != 0)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			if(R == 1 && C == 3)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			if(R == 3 && C == 1)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			
			if(R == 2 && C == 3)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
			
			if(R == 3 && C == 2)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
			if(R == 2 && C == 3)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
			if(R == 3 && C == 4)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
			if(R == 4 && C == 3)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
			if(R == 3 && C == 3)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
		}
		
		if(X == 4)
		{
			if(R < 4 && C < 4)
			{
				cout << "RICHARD" << endl;
				goto A;
			}	
			if(R == 1 && C == 4 || R == 4 && C == 1)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			if(R == 2 && C == 4 || R == 4 && C == 2)
			{
				cout << "RICHARD" << endl;
				goto A;
			}
			if(R == 3 && C == 4 || R == 4 && C == 3)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
			if(R == 4 && C == 4)
			{
				cout << "GABRIEL" << endl;
				goto A;
			}
		}
			
		A:;	
	}
	
	return 0;
}

