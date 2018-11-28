#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <sstream>

const char *
getToken(
    const char **pptr, 
    char *tok, 
    int maxtoklen, 
    const char *delims, 
    const char *white, 
    const char *quotes
    )
{
    int in_quote = 0;

    while (strchr(white, **pptr))
        if (**pptr != '\0')
            (*pptr)++;
        else
            break;
    if (**pptr == '\0')
        return NULL;
	
    if (quotes)
        if (strchr(quotes, **pptr))
        {
            (*pptr)++;
            in_quote = 1;
        }
	
    if (in_quote)
    {
        int i;
        for (i = 0; i < maxtoklen - 1; i++, (*pptr)++)
            if (**pptr == '\0')
                break;
            else if (strchr(quotes, **pptr))
            {
                (*pptr)++;
                break;
            }
            else
                *(tok+i) = **pptr;
        *(tok+i) = '\0';
    }
    else
    {
        int i;
        for (i = 0; i < maxtoklen - 1; i++, (*pptr)++)
            if (**pptr == '\0')
                break;
            else if (strchr(delims, **pptr))
            {
                (*pptr)++;
                break;
            }
            else
                *(tok+i) = **pptr;
        *(tok+i) = '\0';
        for (i--; i > 0; i--)
            if (strchr(white, *(tok+i)))
                *(tok+i) = '\0';
            else
                break;
    }

    return tok;
}

int
split(char *buf, char **values)
{
    char *ptr = buf;
    char *p2;
    int c = 0;
    while ((p2 = strchr(ptr, ' ')) != NULL)
    {
        *p2 = '\0';
        values[c] = ptr;
        c++;
        ptr = p2+1;
    }

    if ((p2 = strchr(ptr, '\n')) != NULL)
        *p2 = '\0';

    values[c] = ptr;
    return c+1;
}

struct stDecision {
    long currentOps;
    long numToDelete;
};

bool
processRecord(FILE *f, unsigned long testCaseNum)
{
    char buf[4096];
    char *vals[4096];

    int mySize;
    int numMotes;
    long moteSizes[101];

    if (fgets(buf, 4096, f))
    {
        int numVals = split(buf, vals);
        if (numVals != 2)
            return false;
        mySize = atoi(vals[0]);
        numMotes = atoi(vals[1]);
    }
    else
        return false;

    if (fgets(buf, 4096, f))
    {
        int numVals = split(buf, vals);
        if (numVals != numMotes)
            return false;

        for (int i = 0; i < numMotes; i++)
        {
            moteSizes[i] = atol(vals[i]);
        }
    }
    else
        return false;

    stDecision decisions[101];
    int decisionOffset = 0;

    //std::ostringstream log;
    long accum = mySize;
    int numOps = 0;
    std::sort(moteSizes,moteSizes+numMotes);
    for (int i = 0; i < numMotes; )
    {
        if (accum > moteSizes[i])
        {
            // good skip to next...
            accum += moteSizes[i];
            i++;

            // if (testCaseNum == 6)
            // {
            //     printf("0: accum = %ld (mote size = %ld)\n", accum, moteSizes[i-1]);
            // }
        }
        else
        {
            int numOpsLeft = numMotes - i;
            // should we make the rest deletes?
            long remain = moteSizes[i] - accum;

            // save our current decision
            decisions[decisionOffset].currentOps = numOps;
            decisions[decisionOffset].numToDelete = numOpsLeft;
            decisionOffset++;

            if (remain < accum && remain > 0)
            {
                // ok we can add one...
                // if (testCaseNum == 6)
                // {
                //     printf("1: accum = %ld, after will be %ld\n", accum, accum + accum - 1);
                // }

                numOps++;
                accum += (accum-1);
                accum += moteSizes[i];
                i++;

            }
            else
            {
                // we can delete the current one...
                // or add another one...
                if (numOpsLeft == 1 || accum-1 <= 0)
                {
                    // delete
                    i++;
                    numOps++;

                    // if (testCaseNum == 6)
                    // {
                    //     printf("2: deleted\n");
                    // }
                }
                else
                {
                    int numOpsToMake = 0;
                    while (accum <= moteSizes[i])
                    {
                        numOpsToMake++;
                        //log << "Added " << (accum - 1) << + "to " << accum << ", ";

                        // if (testCaseNum == 6)
                        // {
                        //     printf("3: added %ld to %ld\n", (accum - 1), accum);
                        // }
                        accum += (accum-1);
                    }
                    if (numOpsToMake > numOpsLeft)
                    {
                        //log << "OK, " << numOpsToMake << " > " << numOpsLeft << " deleting remaining";
                        // delete remaining...
                        numOps += numOpsLeft;
                        i = numMotes;

                        // if (testCaseNum == 6)
                        // {
                        //     printf("4: deleted remainder\n");
                        // }

                    }
                    else
                    {
                        numOps += numOpsToMake;
                        accum += moteSizes[i];
                        i++;
                    }
                }
            }
        }
    }

    for (int i = 0; i < decisionOffset; i++)
    {
        long testOps = decisions[i].currentOps + decisions[i].numToDelete;
        if (testOps < numOps)
        {
            // if (testCaseNum == 6)
            // {
            //     printf("5: replacing %ld with %ld\n", (long)numOps, testOps);
            // }
            numOps = testOps;
        }
    }
    printf("Case #%lu: %d\n", testCaseNum, numOps);

    return true;
}

int
main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s <input.txt>\n", argv[0]);
        return 0;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f)
    {
        printf("Couldn't open file\n");
        return 0;
    }

    char buf[10001];
    fgets(buf, 10001, f);
    long numRecs = atol(buf);
    //printf("There are %ld recs\n", numRecs);

    for (unsigned long recNum = 0; recNum < numRecs; recNum++)
    {
        if (!processRecord(f, recNum+1))
        {
            fprintf(stderr, "Error processing record number %ld\n", recNum+1);
        }
    }

    fclose(f);

    return 0;
}
