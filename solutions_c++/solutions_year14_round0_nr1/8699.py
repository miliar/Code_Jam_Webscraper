#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	freopen ("a.in","r",stdin);
	freopen ("a.out","w",stdout);
	int n;
	cin >> n;
	int numeros[16];
	for(int s = 0; s < n; s++)
	{
		memset(numeros, 0, sizeof(numeros));
		int fila;
		cin >> fila;
		for(int i = 0; i < 4; i++)
		{
			int num;
			for(int j = 0; j < 4; j++)
			{
				cin >> num;
				if(i == fila - 1)
					numeros[num-1]++;
			}
		}
		cin >> fila;
		for(int i = 0; i < 4; i++)
		{
			int num;
			for(int j = 0; j < 4; j++)
			{
				cin >> num;
				if(i == fila - 1)
					numeros[num-1]++;
			}
		}
		int num = -1;
			
		for(int i = 0; i < 16; i++)
		{
			if(numeros[i] == 2)
			{
				if(num > 0)
				{
					num = 17;
					break;
				} else {
					num = i+1;
				}
			}
		}
		cout << "Case #" << s + 1 << ": ";
		if(num == 17)
			cout << "Bad magician!" << endl;
		else if(num > 0)
			cout << num << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
	return 0;
}
