#include <iostream.h>
#include <fstream.h>

// Code Jam 2015


int main(int argc, char *argv[])
{
	int T;
	int t;
	int Smax;
	int s;
	int standing;
	char c;
	
	int answer;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	for (t=0;t<T;t++)
	{
		inFile >> Smax;
		inFile >> std::skipws >> c;
		standing = (c-0x30);
		answer = 0;
		//printf("Smax: %d\n", Smax);
		//printf("standing: %d\n", standing);
		for (s=1;s<=Smax;s++)
		{
			inFile >> c;
			//printf(" read: %d\n", (c-0x30));
			//printf(" standing: %d\n", standing);
			//printf(" s: %d\n", s);
			if ( standing >= s )
			{
				standing = standing + (c-0x30);
			}
			else
			{
				if ( c-0x30 > 0 )
				{
					//printf("adding %d\n", s-standing);
					answer = answer + (s-standing);
					standing = standing +(s-standing);
					standing = standing + (c-0x30);
				}
			}
			
		}
		
		
		

		cout << "Case #" << t+1 << ": " << answer << endl;		
	}
		
		
	
	inFile.close();
	return 0;
}