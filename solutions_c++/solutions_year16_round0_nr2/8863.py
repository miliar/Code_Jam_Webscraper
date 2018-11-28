#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <unistd.h>

using namespace std;

size_t findNextPancakeTowerTop (char *buf, size_t bufsize, size_t c)
{
    while (c<bufsize && buf[c] != '+' && buf[c] != '-')
        ++c;
    return c;
}
void printPancake (char *buf, size_t id, size_t b, size_t e)
{
    fprintf (stderr, "pancake[%2d]: |", (int)id);
    for (size_t i = b; i < e; ++i)
        fprintf (stderr, "%c", buf[i]);
    fprintf (stderr, "|\n");
}
size_t findLowestBack (char *buf, size_t b, size_t e)
{
    if (e == 0)
    {
        return b;
    }
    for (size_t i = e-1; i >= b; --i)
    {
        if (buf[i] == '-')
        {
            return i;
        }
    }
    return b-1;
}
void flip (char *buf, size_t b, size_t e)
{
    for (size_t i = 0; i < (e-b)/2; ++i)
    {
        char t = buf[b+i];
        buf[b+i] = buf[e-1-i];
        buf[e-1-i] = t;
    }
    for (size_t i = b; i < e; ++i)
    {
        if (buf[i] == '+')
        {
            buf[i]='-';
        } else {
            buf[i]='+';
        }
    }
}

char buffer [1024*1024]; /*100*100 characters + some stuff is expected. Must be enough.*/
int main(int argc, char** argv) {

    unsigned int T = 0;
    scanf ("%u", &T);

    fprintf (stderr, "Doing %d testcases\n", T);
    
    ssize_t bytesRead = fread(buffer, 1, sizeof(buffer), stdin);
    if (bytesRead < 0 || (size_t)bytesRead >= sizeof(buffer))
    {
        fprintf (stderr, "Need more memory!\n");
        return 0;
    }   
    
    size_t cursor = 0;
    
    for (size_t t = 0; t < T; ++t)
    {
        fprintf (stderr, "\n#%d-------------------\n", (int)(t+1));
        cursor = findNextPancakeTowerTop(buffer, sizeof(buffer), cursor);
        fprintf (stderr, "\n#The pancake starts at %d\n", (int)cursor);
        
        if (cursor >= sizeof(buffer))
        {
            fprintf (stderr, "cannot find next top!\n");
            return 0;
        }
        size_t begin = cursor;  // the top of the pancake
        
        while (cursor<sizeof(buffer) && (buffer[cursor] == '+' || buffer[cursor] == '-'))
            ++cursor;

        size_t end = cursor;  // One after the bottom of the pancake

        size_t iteration = 0;
        size_t lowestBack = 0;
        
        printPancake (buffer, iteration, begin, end);
        while ((lowestBack = findLowestBack(buffer, begin, end)) >= begin)
        {
            if (buffer[begin] == '-')
            {
                fprintf (stderr, "The top pancake is back up, flip all the top: [%d, %d)!\n", (int)begin, (int)lowestBack+1);
                flip(buffer, begin, lowestBack+1);
            } else {
                size_t happyEnd = begin;
                while (buffer[happyEnd] == '+')
                {
                    ++happyEnd;
                }
                fprintf (stderr, "The top pancake is happy up, flip all the happies: [%d, %d)!\n", (int)begin, (int)happyEnd);
                flip(buffer, begin, happyEnd);                
            }
            ++iteration;
            printPancake (buffer, iteration, begin, end);
        }
        fprintf (stderr, "We are ready. \n");
        printf ("Case #%d: %d\n", (int)(t+1), (int)iteration);
    }    
}

#ifdef problem_A
int main(int argc, char** argv) {

    int T = 0;
    scanf ("%d", &T);
    fprintf (stderr, "Doing %d testcases", T);
    
    for (int t = 0; t < T; ++t)
    {
        int N = 0;
        scanf("%d", &N);
        
        if (N == 0)
        {
            printf ("Case #%d: INSOMNIA\n", t+1);
        } else {
            unsigned int digits = 0;
            int i = 1;
            while (1)
            {
                int iN = i*N;
                if (iN < N)
                {
                    fprintf (stderr, "ERROR, overflow\n");
                    return 0;
                }
                while (iN > 0)
                {
                    digits |= 1 << (iN%10);
                    iN /=10;
                }
                if (digits == 0x03ff)
                {
                    fprintf (stderr, "%d: i=%d, iN=%d\n", N, i, i*N);
                    printf ("Case #%d: %d\n", t+1, i*N);
                    break;
                }
                ++i;
            }
        }
    }
    return 0;
}
#endif
