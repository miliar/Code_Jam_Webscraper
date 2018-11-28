#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<string>
#include<math.h>
using namespace std;

int main()
{
	string inp;
	int T;
	cin >> T;
	int test = T	;
	while (T--)
	{
		int n1, n2;
		cout << "Case #" << test - T << ": ";	
		scanf("%d/%d", &n1, &n2);
		int ctr = 1 ;
		float k = log2(n2);

		int a = k;
		if (a < k)
		{
			float l = log2(n2) - log2(n1);
			int f = l;
			if (f<l)
			{
				cout << "impossible\n";
			}
			else
			{
				cout << f << endl;
			}
		}
		else
		{
			while (n2 / 2 > n1)
			{
				ctr++;
				n2 = n2 / 2;
			}
			cout << ctr << endl;
		}
	}
	getch();
	return 0; //Happy Ending
}