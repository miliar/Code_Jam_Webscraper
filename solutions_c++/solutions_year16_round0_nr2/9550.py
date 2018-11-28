#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	string pilha;
	
	cin >> T;
	
	for(int t = 1; t <= T; t++)
	{
		cin >> pilha;
		
		bool turned = false;
		int flips = 0;
		
		for(int i = pilha.size()-1; i >= 0; i--)
		{
			if(turned)
			{
				if(pilha[i] == '+')
				{
					turned = false;
					flips++;
				}
			}
			else
			{
				if(pilha[i] == '-')
				{
					turned = true;
					flips++;
				}
			}
		}
		
		cout << "Case #" << t << ": " << flips << endl;
	}
	return 0;
}
