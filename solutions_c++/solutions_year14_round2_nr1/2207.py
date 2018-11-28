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

#define MAXCASES 100
#define MAXLENGTH 100
#define MAXSTRINGS 100

string reducePattern(_In_ string const &s);

struct Segment
{
    char letter;
    int count[MAXSTRINGS];
};

void main()
{
	ifstream in("c:\\doom\\A-small-attempt0.in");
	ofstream out("c:\\doom\\out.txt");

    string words[MAXSTRINGS];
    Segment *chunks = new(std::nothrow) Segment[MAXLENGTH];
	if (chunks == nullptr)
	{
		ASSERT(false && L"Insufficient Memory");
	}

    // Take N strings; you're allowed to duplicate a character (and place it next to itself) or remove a duplicate character that is next to itself
    // 1) See if you can make all the strings the same, first of all.  This is as simple as seeing if, when removing all duplicates, they reduce to the same string
    // 2) Determine the minimum number of moves to turn them into the same string.
    //     2a) In the most basic case, you could use sum(len(string) - len(minimized string))
    //     2b) But the trick becomes when you have strings like { abbc, abbbc } or { aabc, aabbc, abbc }

    // General theory: We are assured that 1 <= len(string) <= 100.  Thus, there can be at most 100 different chunks.  Similarly, even in the large data set, we
    // are assured that 2 <= number of strings <= 100.  Thus, we should have enough memory to compute how many segments there are, count the length of each segment
    // for all the provided strings, and determine what number it is most efficient to move all the segments to.  It's possible that taking the mode would work in
    // most cases, but with a max length of 100, it's simple enough to just brute force between the most and fewest occurrences of the pattern and calculate the absolute
    // ideal. (proof that the number that requires the fewest transforms is between the highest and lowest occurrences in the chunks is left as an exercise to the reader)

	int numCases;
	in >> numCases;
    ASSERT(numCases <= MAXCASES);

	for (int line = 1; (line <= numCases); ++line)
    {
        ASSERT(in.good());

        int numStrings;
        in >> numStrings;
        ASSERT(numStrings <= MAXSTRINGS);

        for (int i = 0; i < numStrings; ++i)
        {
            in >> words[i];
        }

        // Stage 1: Verify that they're all the same
        bool canBeEqualized = true;
        string const reduced = reducePattern(words[0]);
        for (int i = 1; i < numStrings; ++i)
        {
            if (reducePattern(words[i]) != reduced)
            {
                canBeEqualized = false;
                break;
            }
        }

        if (canBeEqualized)
        {
            int sum = 0;
            int const numChunks = reduced.size();

            for (int i = 0; i < numChunks; ++i)
            {
                chunks[i].letter = reduced[i];
            }

            for (int i = 0; i < numStrings; ++i)
            {
                char c = words[i][0];
                unsigned int chunk = 0;
                unsigned int count = 0;
                for (auto it = words[i].begin(); ; ++it)
                {
                    if ((it != words[i].end()) && ((*it < 'a') || (*it > 'z')))
                    {
                        continue;
                    }

                    if (it == words[i].end() || (*it != c))
                    {
                        ASSERT(c == chunks[chunk].letter);
                        chunks[chunk].count[i] = count;
                        ++chunk;
                        if (it == words[i].end())
                        {
                            ASSERT(chunk == numChunks);
                            break;
                        }
                        else
                        {
                            c = *it;
                            count = 0;
                        }
                    }
                    else
                    {
                        ++count;
                    }
                }
            }

            for (int i = 0; i < numChunks; ++i)
            {
                // Compute the minimum number of moves necessary
                int minN = MAXLENGTH + 1;
                int maxN = 0;
                int minMoves = MAXLENGTH + 1;
                for (int j = 0; j < numStrings; ++j)
                {
                    int const currentCount = chunks[i].count[j];
                    if (currentCount < minN)
                    {
                        minN = currentCount;
                    }
                    if (currentCount > maxN)
                    {
                        maxN = currentCount;
                    }
                }
                ASSERT(minN <= maxN);
                for (int j = minN; j <= maxN; ++j)
                {
                    int localSum = 0;
                    for (int k = 0; k < numStrings; ++k)
                    {
                        localSum += abs(j - chunks[i].count[k]);
                    }
                    if (localSum < minMoves)
                    {
                        minMoves = localSum;
                    }
                }
                sum += minMoves;
            }

            out << "Case #" << line << ": " << sum << endl;
        }
        else
        {
            out << "Case #" << line << ": Fegla Won" << endl;
        }
    }
}

string reducePattern(_In_ string const &s)
{
    string out = "";
    char c = '\0';
    for (auto i = s.begin(); i != s.end(); ++i)
    {
        if ((*i < 'a') || (*i > 'z'))
        {
            continue;
        }

        if (*i != c)
        {
            c = *i;
            out += c;
        }
    }

    return out;
}