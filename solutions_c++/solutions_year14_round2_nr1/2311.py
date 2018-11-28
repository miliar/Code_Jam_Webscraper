///////////////////////////////////////////////////////////////////////////////
// TESTING PARAMETERS
const char* FILENAME="A%d.in";
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

///////////////////////////////////////////////////////////////////////////////

const int kMaxStringLength = 128;

typedef PAIR<char, int> RUN;
typedef VECTOR<RUN> RUNS;
class GAME_STRING : public RUNS
{
public:
	void Set(const char* Str)
	{
		for (RUN Run(0,0);; ++Str, ++Run.second)
		{
			if (*Str != Run.first)
			{
				if (Run.second)
					this->push_back(Run);
				if (!*Str)
					break;
				Run = RUN(*Str, 0);
			}
		}
	}

	bool IsSimilar(const GAME_STRING& other) const
	{
		if (this->size() != other.size())
			return false;
		for (int i=0; i<this->size(); ++i)
			if ((*this)[i].first != other[i].first)
				return false;
		return true;
	}
};

void ProcessFile(FILE* fin)
{
	int T;
	fscanf(fin, "%d", &T);
	for (int t=0; t<T; ++t)
	{
		int N;
		fscanf(fin, "%d", &N);

		typedef VECTOR<GAME_STRING> GAME_STRINGS;
		GAME_STRINGS GameStrings;
		GameStrings.resize(N);
		bool bCanWin = true;
		for (int n=0; n<N; ++n)
		{
			char str[kMaxStringLength];
			fscanf(fin, "%s", str);

			if (bCanWin)
			{
				GAME_STRING& GameString= GameStrings[n];
				GameString.Set(str);
				if (n>0 && !GameString.IsSimilar(GameStrings[0]))
					bCanWin = false;
			}
		}
		if (!bCanWin)
			fprintf(FILE_OUT, "Case #%d: Fegla Won\n", t+1);
		else
		{
			int Items = GameStrings[0].size();
			VECTOR<long> Sums;
			Sums.resize(Items);
			foreach(GAME_STRINGS, GameStrings, itGameString)
			{
				for(int i=0; i<Items; ++i)
					Sums[i] += (*itGameString)[i].second;
			}
			for(int i=0; i<Items; ++i)
				Sums[i] = (Sums[i]+N/2)/N;
			int Steps = 0;
			foreach(GAME_STRINGS, GameStrings, itGameString)
			{
				for(int i=0; i<Items; ++i)
					Steps += abs((*itGameString)[i].second - Sums[i]);
			}
			fprintf(FILE_OUT, "Case #%d: %d\n", t+1, Steps);
		}
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
