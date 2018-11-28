// GoogleJam_Problem1.cpp : Defines the entry point for the console application.
//

//#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include "stdafx.h"
#include "StringHelpers.h"
#include "windows.h"
#include <queue>
#include <xmmintrin.h>
#include <mpir.h>
 

//vector<long long> ix;

char * g_hash = NULL; 
size_t g_hashSize = 500 * 1024 * 1024;

std::hash_map<unsigned long long, long long> g_h;

class Cmp
{
public:
    bool operator()(short l, short r)
    {
        return r < l;
    }
};

struct Point
{
    Point() : x(0), y(0), id(0)  {};
    Point(long long x1, long long y1, int id1) : x(x1), y(y1), id(id1)  {};

    long long x;
    long long y;
    int id;
};

double g_a[103][103];
double g_p[103][103]; 
//char g_os[20][100][3];
//
//int g_numo[20] = { 0, 1, 2, 6, 100 };




/// ---------------
//  SMALL
///

VLL g_primes;
long long g_maxp;

long long GetDivisor(long long t)
{
	long long mp = (long long)sqrt(t);

	for (unsigned int i = 0; i < g_primes.size(); ++i)
	{
		long long p = g_primes[i];
		if (t % p == 0)
			return p;
		if (p > mp)
			return 0;
	}

	return 0;
}

long long GetDivisor(mpz_t t)
{
	mpz_t mp;
	mpz_init2(mp, 96);
	mpz_t rem;
	mpz_init2(rem, 96);

	mpz_sqrt(mp, t);
	long long r = 0;

	for (unsigned int i = 0; i < g_primes.size(); ++i)
	{
		long long p = g_primes[i];
		long long reminder = mpz_mod_ui(rem, t, p);
		if (reminder == 0)
		{
			r = p;
			break;
		}

		if (mpz_cmp_ui(mp, p) < 0)
		{
			break;
		}
	}

	mpz_clear(rem);
	mpz_clear(mp);

	return r;
}

gmp_randstate_t g_state;

bool IsPrimeNew(long long t)
{
	if (t < g_maxp)
	{
		// use array
		return (*(g_hash + t / 8)) & (1 << (t&0x7));
	}
	else
	{
		long long d = GetDivisor(t);
		return d == 0;
	}
}

bool IsPrimeNew(mpz_t t)
{
	return mpz_probable_prime_p(t, g_state, 25, 0);
}


void getPrimes(long long m, VLL &vp, char * phash)
{
	memset(phash, 0, m / 8 + 1);

	long long l = (long long)(sqrt(m)) + 1;
	vp.reserve(l);
	vp.push_back(2);
	*(phash + 2 / 8) |= (1 << (2 & 0x7));

	for (long long i = 3; i <= m; i += 2)
	{
		unsigned int j = 0;
		bool good = true;
		for (; j < vp.size(); ++j)
		{
			long long p = vp[j];
			if (i % p == 0)
			{
				good = false;
				break;
			}

			if (p * (long long)p > i)
				break;
		}

		if (good)
		{
		    vp.push_back(i);
			*(phash + i/8) |= (1 << (i&0x7));
		}
	}

	g_maxp = m;
}

long long GetNumber(long long t, int base)
{
	long long p = t&0x1;
	long long b = base;

	long long t1 = t >> 1;
	while(t1)
	{
		if (t1 & 1)
		{
			p += b;
		}

		b *= base;
		t1 = t1 >> 1;
	}

	return p;
}

void GetNumber(long long t, int base, mpz_t p)
{
	mpz_set_ui(p, t & 0x1);
	mpz_t b;
	
	mpz_init2(b, 96);
	mpz_set_ui(b, base);

	long long t1 = t >> 1;
	while (t1)
	{
		if (t1 & 1)
		{
			mpz_add(p, p, b);
		}

		mpz_mul_ui(b, b, base);
		t1 = t1 >> 1;
	}
}

void SolveSmall(long long minn, long long maxn, int num, MLL &mr)
{
	mr.reserve(num);
	long long v[10];

	for (long long t = minn | 1; t <= maxn; t += 2)
	{
		if (IsPrimeNew(t))
		{
			continue;
		}

		v[0] = t;

		bool isgood = true;
		for (int i = 3; i <= 10; ++i)
		{
			long long p = GetNumber(t, i);

			if (IsPrimeNew(p))
			{
				isgood = false;
				break;
			}

			v[i - 2] = p;
		}

		if (isgood)
		{
			mr.push_back(vector<long long>());
			VLL & vr = mr.back();
			vr.push_back(t);
			FOR(i, 2, 11)
			{
				long long d = GetDivisor(v[i - 2]);
				if (d == 0) // Devisor was too big
				{
					isgood = false;
					break;
				}
				vr.push_back(d);
			}

			if (isgood)
			{
				if (mr.size() >= num)
				{
					break;
				}

				if (mr.size() % 10 == 0)
				{
					printf("Generated %I64u numbers\n", mr.size());
				}
			}
			else
			{
				mr.resize(mr.size() - 1);
			}
		}
	}

}

void SolveLarge(long long minn, long long maxn, int num, MLL &mr)
{
	gmp_randinit_default(g_state);

	mr.reserve(num);
	mpz_t v[10];
	mpz_t p;
	mpz_init2(p, 96);
	FOR(i, 0, AS(v))
	{
		mpz_init2(v[i], 96);
	}

	for (long long t = minn | 1; t <= maxn; t += 2)
	{
		if (IsPrimeNew(t))
		{
			continue;
		}

		mpz_set_ui(v[0], t);

		bool isgood = true;
		for (int i = 3; i <= 10; ++i)
		{
			GetNumber(t, i, p);

			if (IsPrimeNew(p))
			{
				isgood = false;
				break;
			}

			mpz_set(v[i - 2], p);
		}

		if (isgood)
		{
			mr.push_back(vector<long long>());
			VLL & vr = mr.back();
			vr.push_back(t);
			FOR(i, 2, 11)
			{
				long long d = GetDivisor(v[i - 2]);
				if (d == 0) // Devisor was too big
				{
					isgood = false;
					break;
				}
				vr.push_back(d);
			}

			if (isgood)
			{
				if (mr.size() >= num)
				{
					break;
				}

				if (mr.size() % 10 == 0)
				{
					printf("Generated %I64u numbers\n", mr.size());
				}
			}
			else
			{
				mr.resize(mr.size() - 1);
			}
		}
	}

	FOR(i, 0, AS(v))
	{
		mpz_clear(v[i]);
	}

	mpz_clear(p);
}


void Test()
{
	if (IsPrimeNew(17) == false) printf("ERROR\n");
	if (IsPrimeNew(661945231) == false) printf("ERROR\n");
	if (IsPrimeNew(661945235) == true) printf("ERROR\n");

	if (GetNumber(9, 3) != 28) printf("ERROR\n");
	if (GetNumber(9, 4) != 65) printf("ERROR\n");
	if (GetNumber(9, 5) != 126) printf("ERROR\n");
	if (GetNumber(9, 6) != 217) printf("ERROR\n");
	if (GetNumber(9, 7) != 344) printf("ERROR\n");
	if (GetNumber(9, 8) != 513) printf("ERROR\n");
	if (GetNumber(9, 9) != 730) printf("ERROR\n");
	if (GetNumber(9, 10) != 1001) printf("ERROR\n");

	long long t = 0b10000000000000000000011101000001ll;
	long long p = GetNumber(t, 3);
	if (GetDivisor(p) != 2) printf("ERROR\n");

	MLL mr;
	SolveSmall(9, 10, 1, mr);
	MLL mr1;
	SolveLarge(9, 10, 1, mr1);

}

void Init()
{

}

int _tmain(int argc, _TCHAR* argv[])
{
    __int64 start = GetTickCount64();

    char * outPath = "S:\\progs\\GoogleJam_Problem1\\out.txt";

    if(argc < 2)
    {
        printf("Error. Need in and out files\n");
        return -1;
    }

    if (argc >= 3)
    {
        outPath = argv[2];
    }

    FILE * fin = NULL;
    FILE * fout = NULL;

    fout = _fsopen(outPath, "w", _SH_DENYNO);
    if(fout == NULL)
    {
        printf("Can't open %s\n", outPath);
        return -1;
    }

    vector<string> l = fileToLines(argv[1]);
    int c = 0;
    if (l.size() == 0)
    {
        printf("Can't open %s\n", argv[1]);
        return -1;
    }
    int numTests = atoi(l[c++].c_str());

    g_hash = (char *)VirtualAlloc((LPVOID)NULL, g_hashSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    Init();

	{
		mpz_t integ;
		mpz_init2(integ, 96);		mpz_clear(integ);	}
	getPrimes((1ll << 19) - 1, g_primes, g_hash);

	Test();

    for(int t = 1; t <= numTests; ++t)
    {
        //int n = atoi(l[c++].c_str());
        VI v = splitInt(l[c++].c_str());

		MLL mr;
		//SolveSmall((1ull << (v[0] - 1)) + 1, 1ull << v[0], v[1], mr);
		SolveLarge((1ull << (v[0] - 1)) + 1, 1ull << v[0], v[1], mr);
        fprintf(fout, "Case #%d:\n", t);
        for (int i = 0; i < mr.size(); ++i)
        {
			VLL &vr = mr[i];
			long long val = vr[0];
			long long j = 1ll << 31;
			while (!(val & j)) j = j >> 1;
			while (j)
			{
				fprintf(fout, "%s", val & j ? "1" : "0");
				j = j >> 1;
			}
            
     		FOR(i1, 1, 10)
			{
				fprintf(fout, " %I64d", vr[i1]);
			}
			fprintf(fout, "\n");
		}
    }

    fclose(fout);

    __int64 end = GetTickCount64();

    printf("Time = %.3f sec\n", ((double)(end - start))/1000);

    return 0;
}

