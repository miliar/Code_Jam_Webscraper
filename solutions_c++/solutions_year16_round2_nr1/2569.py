#include<iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string s;
		cin >> s;
		int a[10] = {0};
		int len = s.length();
		int b[256] = {0};
		for(int j = 0; j<len; j++ )
		{
			b[s[j]]++;	
		}
		if (b['Z'] != 0)
		{
			a[0] = b['Z'];
		
			b['E'] -= b['Z'];
			 b['R'] -= b['Z'];
			 b['O'] -= b['Z'];
			 	b['Z'] = 0;
			 
		}
		if (b['W'] != 0)
		{
			a[2] = b['W'];
			b['T'] -= b['W'];
			 
			 b['O'] -= b['W'];
			 b['W'] = 0;
			 
		}
		if (b['U'] != 0)
		{
			 a[4] = b['U'];
			b['F'] -= b['U'];
			 b['O'] -= b['U'];
			
			  b['R'] -= b['U'];
			
			  b['U'] =0;
		}
		if (b['X'] != 0)
		{
			a[6] = b['X'];
			b['S'] -= b['X'];
			 b['I'] -= b['X'];
			 b['X'] -= b['X'];
			  
			 
			 
		}
		if (b['G'] != 0)
		{
			a[8] = b['G'];
			b['E'] -= b['G'];
			 b['I'] -= b['G'];
			
			  b['H'] -= b['G'];
			  b['T'] -= b['G'];
			  b['G'] = 0;
			 
		}
		if (b['O'] != 0)
		{
			a[1] = b['O'];
		
			 b['N'] -= b['O'];
			 b['E'] -= b['O'];
			  	b['O'] = 0;
			 
			 
		}
		if (b['R'] != 0)
		{
			a[3] = b['R'];
			b['T'] -= b['R'];
			 b['H'] -= b['R'];
			 
			  b['E'] -= b['R'];
			  b['E'] -= b['R'];
			 
			 b['R'] = 0;
		}
		if (b['F'] != 0)
		{
			 a[5] = b['F'];
			
			 b['I'] -= b['F'];
			 b['V'] -= b['F'];
			  b['E'] -= b['F'];
			 b['F'] = 0;
			
			 
		}
		if (b['S'] != 0)
		{
			a[7] = b['S'];
			
			 b['E'] -= b['S'];
			 b['V'] -= b['S'];
			  b['E'] -= b['S'];
			  b['N'] -= b['S'];
			 b['S'] = 0;
			 
		}
		a[9] = b['I'];
		cout << "Case #" << i+1 << ": ";
		for(int k = 0; k <= 9; k++)
			{
				if (a[k] != 0)
				{
					while(a[k]!= 0)
						{
							cout << k;
							a[k]--;
						}
				
				}
			}
			cout << endl;
	}
}
