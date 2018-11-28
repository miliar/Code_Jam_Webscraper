#include <bits/stdc++.h>
using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int j = 0; j < N; ++j)
	{
		string s ;
		cin >> s ;
		int pos = 0 ;
		int flop = 0 ;
		int i = 0 ;
		while(i<s.size())
		{	
			if(s[i]=='+')
			{
				pos ++ ;
				i++;
			}
			else
			{
				if(pos!=0) flop++;

				while(i < s.size() && s[i]=='-' )
				{
					i++ ;
				}

				flop++;
				pos = i ;

			}

		}

		cout << "Case #" << j+1 <<  ": " << flop << endl ;	
	}
}