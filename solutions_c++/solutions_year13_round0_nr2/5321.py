///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="B%d.in";
int FILE_FROM = 0;
int FILE_TO = 0;

//#ifdef GCONF_MSSTL_TUNING
#define _SECURE_SCL 0
#define _SCL_SECURE_NO_DEPRECATE
#define _HAS_ITERATOR_DEBUGGING 0
//#endif

//#undef _HAS_EXCEPTIONS
//#define _HAS_EXCEPTIONS 0

#include <set>
#include <vector>
#include <map>	
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <limits>
#include <memory>

template <class T>
inline const T& min(const T& a,const T& b)
{
	return (a < b)? a : b ;
}

template <class T>
inline const T& max(const T& a,const T& b)
{
	return (a > b)? a : b ;
}

#define VECTOR std::vector
#define LIST   std::list
#define SET    std::set
#define MAP    std::map
#define MULTIMAP std::multimap
#define DEQUE  std::deque
#define STACK  std::stack
#define PAIR   std::pair
#define AUTO_PTR std::auto_ptr

#define foreach(TYPE, CONT, ITER) for(TYPE::iterator ITER=(CONT).begin(); ITER != (CONT).end(); ++ITER)
#define foreach_const(TYPE, CONT, ITER) for(TYPE::const_iterator ITER=(CONT).begin(); ITER != (CONT).end(); ++ITER)

const bool OUT_FILE = true;
FILE *FILE_OUT;

char* GetString(__int64 value)
{
	char buffer[4096];
	char* c=buffer;
	while (value || c==buffer)
	{
		*(c++)='0'+(value%10);
		value /= 10;
	}
	*c=0;
	--c;
	char *c2=buffer;
	for (;c2<c;++c2,--c)
	{
		char ct=*c2;
		*c2=*c;
		*c=ct;
	}
	return buffer;
}

///////////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int i=0; i<T; ++i)
	{
		int N,M;
		fscanf(fin, "%d %d", &N, &M);
		char* GrassMaxX = new char[M];
		char* GrassMaxY = new char[N];
		char* Grass = new char[N*M];
		for (int n=0; n<N; ++n)
		{
			GrassMaxY[n]=0;
			for (int m=0; m<M; ++m)
			{
				int c;
				fscanf(fin, "%d", &c);
				Grass[n*M+m] = c;
				if (Grass[n*M+m]>GrassMaxY[n])
					GrassMaxY[n] = Grass[n*M+m];
			}
		}

		for (int m=0; m<M; ++m)
		{
			GrassMaxX[m]=0;
			for (int n=0; n<N; ++n)
			{
				if (Grass[n*M+m]>GrassMaxX[m])
					GrassMaxX[m] = Grass[n*M+m];
			}
		}
		bool res = true;
		for (int n=0; n<N && res; ++n)
			for (int m=0; m<M && res; ++m)
				if (Grass[n*M+m] != GrassMaxX[m] && Grass[n*M+m] != GrassMaxY[n])
					res = false;

		delete []Grass;
		delete []GrassMaxX;
		delete []GrassMaxY;
		fprintf(FILE_OUT, "Case #%d: %s\n", i+1, res ? "YES" : "NO");
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
