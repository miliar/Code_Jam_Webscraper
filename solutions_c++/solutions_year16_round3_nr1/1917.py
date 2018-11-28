///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

#include <vector>
#include <algorithm>

const bool OUT_FILE = true;
FILE *FILE_OUT;

typedef std::pair<int, char> SEN_CHAR;
bool order(const SEN_CHAR& l, const SEN_CHAR& r)
{
	return l.first > r.first;
}

void Check(const std::vector<SEN_CHAR>& P)
{
	int Ps = 0;
	int PMax = 0;
	for (auto p : P)
	{
		if (PMax < p.first)
			PMax = p.first;
		Ps += p.first;
	}
	if (PMax > Ps / 2)
	{
		int alma = 0;
	}
}

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int N;
		fscanf(fin, "%d", &N);
		std::vector<SEN_CHAR> P(N);
		int Ps = 0;
		for (int j = 0; j < N; ++j)
		{
			fscanf(fin, "%d", &P[j].first);
			Ps += P[j].first;
			P[j].second = 'A' + j;
		}
		fprintf(FILE_OUT, "Case #%d:", i+1);
		std::sort(P.begin(), P.end(), &order);
		for (;Ps>0;)
		{
			Check(P);
			for (int j = 0; j<P.size(); ++j)
			{
				SEN_CHAR& p = P[j];
				if (j>0 && p.first != P[j-1].first + 1)
					break;
				if ((j + 1 >= P.size() || p.first != P[j + 1].first) && j>0)
				{
					fprintf(FILE_OUT, "%c", p.second);
					--p.first;
					--Ps;
					Check(P);
				}
				else {
					Check(P);
					fprintf(FILE_OUT, " %c", p.second);
					--p.first;
					--Ps;
				}
			}
		}
		fprintf(FILE_OUT, "\n");
	}
}

///////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	char fileName[256];
	printf ("Which file: ");
	fgets ( fileName, 256, stdin );
	if (fileName[0]>13)
	{
		int i = atoi (fileName);
		FILE_FROM = FILE_TO = i;
	}
	for (int file_from=FILE_FROM; file_from<=FILE_TO; ++file_from)
	{
		sprintf(fileName, FILENAME, file_from);
		FILE *fin = fopen(fileName, "r");
		if (!fin)
		{
			printf("!!! CANNOT INF FILE %s", fileName);
			continue;
		} else {
			printf("Processing file: %s ...\n", fileName);
		}
		if (OUT_FILE)
		{
			char fileNameOut[256];
			sprintf(fileNameOut, "%s.out", fileName);
			FILE_OUT = fopen(fileNameOut, "w");
		} else
		{
			FILE_OUT = stdout;
		}
		ProcessFile(fin);
		fclose(fin);
		if (OUT_FILE)
			fclose(FILE_OUT);
	}
	printf("\nREADY!!!\n");
	getc(stdin);
	return 0;
}
