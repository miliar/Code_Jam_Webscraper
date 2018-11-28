#include <bits/stdc++.h>

using namespace std;

void input();
int solve ();


int xomino, row, col;
int times;
int t;

int main()
{

	cin >> times;

	for (t = 1; t <= times; t++)
	{
		input();
        solve();
    }
    return 0;
}



void input()
{
    cin>>xomino ;
    cin>>row;
	cin>>col;
}


int solve ()
{
    if ((row * col) % xomino)
		{
			cout << "Case #"<<t <<": "<<"RICHARD"<<endl;
		}
		else
		{
			if (xomino == 1)
			{
				cout << "Case #"<<t <<": "<<"GABRIEL"<<endl;
			}
			else if (xomino == 2)
			{
				cout << "Case #"<<t <<": "<<"GABRIEL"<<endl;
			}
			else if (xomino == 3)
			{
				if (row * col != 3)
				{
                    cout << "Case #"<<t <<": "<<"GABRIEL"<<endl;

				}
				else
				{
					cout << "Case #"<<t <<": "<<"RICHARD"<<endl;
				}
			}
			else
			{
				if (row * col == 4 || row * col == 8)
				{
					cout << "Case #"<<t <<": "<<"RICHARD"<<endl;
				}
				else
				{
					cout << "Case #"<<t <<": "<<"GABRIEL"<<endl;
				}
			}
		}


}

