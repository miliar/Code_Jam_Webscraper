#include <iostream>
#include <fstream>
#include <cstdlib>
#include<string>
#include<vector>
#include<cmath>
#include <sstream>

using namespace std;


int cases = 0;

string face;

long long tot = 0;
long long temp;


void flip(int a);
int check();

int main()
{


	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cases;
	//cin.ignore();

	
	for (int i = 0; i < cases; i++)
	{
		tot = 0;
		cin >> face;
		for (int a = 0; a < face.length(); a++)
		{
			if (face[a] == '-')
			{
				tot++;
			}
			
		}
		if (tot == 0)
		{
			cout << "Case #" << i + 1 << ": " << tot << endl;
		}
		tot = 0;

		while (check() == 0)
		{


		}
		if(tot != 0){
			cout << "Case #" << i + 1 << ": " << tot << endl;
		}
		tot = 0;
	}



	return 0;
}


int check()
{
	for (int x = face.length() - 1; x > -1; x--)
	{

		if (face[x] == '-')
		{
			
			tot++;
			flip(x + 1);
			
			return 0;
		}

	}
	return 1;


}

void flip(int pos)
{
	for (int i = 0; i < pos; i++)
	{
		
		if (face[i] == '-')
		{
			face[i] = '+';
		}
		else  
		{
			face[i] = '-';
		}
		//cout << face[i];
	}

}




