#include<iostream>
#include<fstream>
using namespace std;

int writeSummary(char*entry, int n);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		char entry[1000001];
		int n;
		myfileIn >> entry;
		myfileIn >> n;
		int ans = writeSummary(entry, n);
		cout << "Case #" << (i+1) << ": " << ans << endl;
		myfileOut << "Case #" << (i+1) << ": " << ans << endl;
	}

	return 0;
}

int writeSummary(char*entry, int n)
{
	int how = 0;
	for(int i = 0; entry[i+(n-1)]; i++)
	{
		int highest = 0;
		int counting = 0;
		for(int j = i; entry[j]; j++)
		{
			switch(entry[j])
			{
			case 'A':
			case 'a':
			case 'E':
			case 'e':
			case 'I':
			case 'i':
			case 'O':
			case 'o':
			case 'U':
			case 'u':
				counting = 0;
				break;
			default:
				counting++;
				if(counting > highest)
				{
					highest = counting;
				}
				break;
			}
			if(highest >= n)
			{
				how++;
			}
		}
	}
	return how;
}