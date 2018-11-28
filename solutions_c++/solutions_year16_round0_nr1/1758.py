#include<iostream>
#include<cstdio>
///#include<string>
#include<fstream>


using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int main ()
{
	printf("Something");
	ifstream input;
	ofstream output;
	input.open("in.txt");
	output.open("out.txt");
	int test,tests;
	input >> tests;
	printf("%d\n", tests);
	forn (test,tests)
	{
		int S;
		printf("%d\n", S);
		input >> S;
		printf("%d\n", S);
		if (S == 0)
		{
			output << "Case #"<< test+1 << ": INSOMNIA"   << "\n";
			continue;
		}
		printf("%d\n", S);
		int dig [10];
		forn (i,10)
			dig[i] = 0;
		int y = 0;
		int check = 0;
		while (check <10)
		{
			check = 0;
			printf("%d\n", S);			
			y = y+S;
			int x = y;
			while(x!=0)
			{
				dig[x%10] = 1;
				x = x/10;
			}	
			forn (i,10){
				check += dig[i];
				printf("%d\n", dig[i]);
			}
			printf("%d", check);
		}
		output << "Case #"<< test+1 << ": " << y << "\n";
	}
}
	
