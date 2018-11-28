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

bool
isvowel(char ch)
{
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

long
numConseq(const char *word, long num)
{
    long count = 0;
    long len = strlen(word);
    for (long i = 0; i < len - num + 1; i++)
    {
        bool matches = false;
        long lastConstOffset = -1;
        for (long j = i; j < len; j++)
        {
            if (matches)
            {
                count++;
                continue;
            }
            bool thisConst = !isvowel(word[j]);
            if (num == 1 && thisConst)
            {
                matches = true;
                count++;
                //break;
            }
            else
            {
                if (thisConst && lastConstOffset >= 0)
                {
                    long numLetters = (j - lastConstOffset) + 1;
                    if (numLetters >= num)
                    {
                        matches = true;
                        count++;
                        //break;
                    }
                }

                if (thisConst && lastConstOffset == -1)
                    lastConstOffset = j;
                if (!thisConst)
                    lastConstOffset = -1;
            }
        }

        //if (matches)
        //    count++;
    }
    return count;
}

bool
processRecord(FILE *f, unsigned long testCaseNum)
{
    char buf[4096];
    char *vals[4096];

    long count = 0;
    if (fgets(buf, 4096, f))
    {
        int numVals = split(buf, vals);
        if (numVals == 2)
        {
            const char *word = vals[0];
            long numConsts = atol(vals[1]);

            count = numConseq(word, numConsts);
        }
        else
            return false;
    }
    else
        return false;

    printf("Case #%lu: %ld", testCaseNum, count);
    printf("\n");

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
