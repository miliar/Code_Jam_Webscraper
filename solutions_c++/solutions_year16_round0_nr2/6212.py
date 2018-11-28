#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;



int main()
{
	ifstream myfile;
//	myfile.open("testB.txt");
	myfile.open("B-large.in");

	int T;
	myfile >> T;
	
	for (int t=0; t<T; t++)
	{
		char s[101], s1[101];
		myfile >> s;
		
		int conta = 0;
		
		// cout << "lavoro su:" << s; getchar();
		
		for (int i=strlen(s)-1; i>=0; i--)
		{
			
			if (s[i] == '-')
			{
				int j;
				for (j=0; j<i && s[j] == '+'; j++);
				if (j!=0)
				{
					for (int k=0; k<j; k++)
					{
						s[k]='-';
					}
					i++;
				}
				else
				{
					int k, l;
					for (k=0, l=i; k<=i;k++, l--)
					{
						s1[k] = (s[l]== '+' ? '-' : '+');
					}
					for (k=0; k<=i; k++)
						s[k]=s1[k];
				}
				conta++;
			}

			// cout << conta << ": " << s << "("<<i<<")"; getchar();
			
		}

		
		cout << "Case #" << t+1 << ": " << conta <<"\n";
	} 
	
	myfile.close();
	return 0;	
}

