#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
//#define DEBUG

using namespace std;

int main(int argc, char* argv[])
{
	FILE* pf_in = fopen("D-small-attempt4.in", "r");
	FILE* pf_out = fopen("sout", "w");

	int T;
	fscanf(pf_in, "%d", &T);
	for(int i = 1; i <= T; i++)
	{
		int X, R, C;
		fscanf(pf_in, "%d%d%d", &X, &R, &C);
#ifdef DEBUG
		cout << X << " " << R << " " << C << " ";
#endif
		bool can_asm = false;
		switch(X)
		{
			case 1:
				can_asm = true;
				break;
			case 2:
				if((R % 2 == 0 && C >= 1) || (C % 2 == 0 && R >= 1))
					can_asm = true;
				break;
			case 3:
				if((R == 3 && C >= 2) || (C == 3 && R >= 2))
					can_asm = true;
				break;
			case 4:
				if((R == 4 && C >= 3) || (C == 4 && R >= 3))
					can_asm = true;
				break;
		}
		if(can_asm)
		{
			fprintf(pf_out, "Case #%d: %s\n", i, "GABRIEL");
#ifdef DEBUG
			cout << "G" << endl;
#endif
		}
		else
		{
			fprintf(pf_out, "Case #%d: %s\n", i, "RICHARD");
#ifdef DEBUG
			cout << "R" << endl;
#endif
		}
#ifdef DEBUG
#endif
	}
	return 0;
}

