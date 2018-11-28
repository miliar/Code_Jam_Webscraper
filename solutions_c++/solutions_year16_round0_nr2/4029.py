#include <cstdio>
#include <vector>

using namespace std;

int main()
{
	int T, R, size;
	int i, j, F;
	bool cakeStack[100], flips[100], before[100];
	bool Happy, Retry;
	char buf[101];
	FILE *fin, *fout;
	fin = fopen("B-input.txt", "r");
	fout = fopen("B-output.txt", "w");
	
	fscanf(fin, "%d", &T);
	for(i = 1 ; i <= T ; i++)
	{
		R = 0;
		Happy = false;
		fscanf(fin, "%s", &buf);
		for(j = 0 ; buf[j] != '\0' ; j++)
		{	cakeStack[j] = (buf[j] == '+') ? true : false;	}
		size = j;
		while(true)
		{
			Happy = true;
			Retry = true;
			for(j = 0 ; j < size ; j++)
			{
				if(cakeStack[j] == false)
				{	Happy = false;	}
			}
			if(Happy == true)
			{	break;	}
			
			for(j = size - 1 ; j >= 0 ; j--)
			{
				if(cakeStack[j] == false)
				{	F = j;	break;	}
			}
			
			while(Retry)
			{
				for(j = 0 ; j <= F ; j++)
				{	flips[j] = !cakeStack[j];	}
				if(cakeStack[F] != flips[0])
				{	Retry = false;	}
				F = (Retry) ? F - 1 : F;
			}
			
			for(j = 0 ; j <= F ; j++)
			{	cakeStack[F - j] = flips[j];	}
			R++;
		}
		fprintf(fout, "Case #%d: %d\n", i, R);
	}
}