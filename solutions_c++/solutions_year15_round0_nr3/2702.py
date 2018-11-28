#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
//#define DEBUG

using namespace std;

#define q1 1
#define qi 2
#define qj 3
#define qk 4
char s[10001];
int qm[5][5] = {
	{0, 0, 0, 0, 0},
	{0, q1, qi, qj, qk},
	{0, qi, -q1, qk, -qj},
	{0, qj, -qk, -q1, qi},
	{0, qk, qj, -qi, -q1}
};

int main(int argc, char* argv[])
{
	FILE* pf_in = fopen("C-small-attempt0.in", "r");
	FILE* pf_out = fopen("sout", "w");

	int T;
	fscanf(pf_in, "%d", &T);
	for(int i = 1; i <= T; i++)
	{
		int L;
		fscanf(pf_in, "%d", &L);
		unsigned long long X;
		fscanf(pf_in, "%llu", &X);

		fscanf(pf_in, "%s", s);

		int cyc = 0;
		int v = q1;
		bool iok = false;
		bool jok = false;
		bool kok = false;
		bool ijkok = false;
		int neg_count = 0;
		while(cyc < X)
		{
			kok = false;
			for(int n = 0; n < L; n++)
			{
				v = qm[v][s[n] - 'i' + 2];
				if(v < 0)
				{
					neg_count++;
					v = -v;
				}
#ifdef DEBUG
				switch(v)
				{
					case 1:
						cout << "1" << " ";
						break;
					case 2:
						cout << "i" << " ";
						break;
					case 3:
						cout << "j" << " ";
						break;
					case 4:
						cout << "k" << " ";
						break;
				}
#endif

				if(!iok && v == qi)
				{
					iok = true;
					v = q1;
#ifdef DEBUG
					cout << "I" << " ";
#endif
				}
				if(iok && !jok && v == qj)
				{
					jok = true;
					v = q1;
#ifdef DEBUG
					cout << "J" << " ";
#endif
				}
				if(jok && v == qk && n == L - 1)
				{
					kok = true;
#ifdef DEBUG
					cout << "K" << " ";
#endif
				}
			}
			cyc++;
			if(cyc == X && kok)
				ijkok = true;
		}
#ifdef DEBUG
		cout << endl;
#endif
		if(ijkok && neg_count % 2 == 0)
			fprintf(pf_out, "Case #%d: %s\n", i, "YES");
		else
			fprintf(pf_out, "Case #%d: %s\n", i, "NO");
#ifdef DEBUG
#endif
	}
	return 0;
}

