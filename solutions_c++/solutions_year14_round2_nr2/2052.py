#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib> // for abs
using namespace std;

#ifndef ASSERT
#ifdef _MSC_VER
#define ASSERT(x) if (!(x)) { __debugbreak(); }
#else
#define ASSERT(x)
#endif
#endif
#ifndef _In_
#define _In_
#endif
#ifndef ARRAYSIZE
#define ARRAYSIZE(x) (sizeof(x)/sizeof(x[0]))
#endif

void main()
{
    // This is the stupid, brute force way.  Obviously this doesn't scale to 1E9, but for the small data set......

	ifstream in("c:\\doom\\B-small-attempt0.in");
	ofstream out("c:\\doom\\out.txt");

	int numCases;
	in >> numCases;

    for (int line = 1; line <= numCases; ++line)
    {
        unsigned int A;
        unsigned int B;
        unsigned int K;
        unsigned int count = 0;

        in >> A >> B >> K;

        for (unsigned int i = 0; i < A; ++i)
        {
            for (unsigned int j = 0; j < B; ++j)
            {
                unsigned int n = i & j;
                if (n < K)
                {
                    ++count;
                }
            }
        }

        out << "Case #" << line << ": " << count << endl;
    }
}