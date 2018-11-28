#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <unistd.h>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

char inbuffer[1024*1024];
//char outbuffer[10*1024];


size_t findNextWordStart (char *buf, size_t bufsize, size_t c)
{
    while (c<bufsize && (buf[c] < 'A' || buf[c] > 'Z'))
        ++c;
    return c;
}

size_t printhistogram (int *histogram)
{
    /*
    fprintf (stderr, "[ ");
    for (int i = 'A'; i <= 'Z'; ++i )
    {
        if (histogram[i] > 0)
        {
            for(int j = 0; j < histogram[i]; ++j)
            {
                fprintf (stderr, "%c", i);
            }
            fprintf (stderr, " ");
        }
        if (histogram[i] < 0)
        {
            for(int j = 0; j < -histogram[i]; ++j)
            {
                fprintf (stderr, "%c", i-'A'+'a');
            }
            fprintf (stderr, " ");
        }
    }
    fprintf (stderr, "]\n");
    */
}

const char* numbertexts [] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
};

void decreaseWithString (int *histogram, const char * string)
{
    fprintf (stderr, "decreaseWithString");
    fprintf (stderr, "with %s\n", string);
    
    
    int len = strlen (string);
    
    for(int i = 0; i < len; ++i )
    {
        --histogram[string[i]];
    }
    printhistogram (histogram);

}

int main(int argc, char** argv) {

    unsigned int T = 0;
    scanf ("%u", &T);

    fprintf (stderr, "Doing %d testcases\n", T);
    
    ssize_t bytesRead = fread(inbuffer, 1, sizeof(inbuffer), stdin);
    if (bytesRead < 0 || (size_t)bytesRead >= sizeof(inbuffer))
    {
        fprintf (stderr, "Need more memory!\n");
        return 0;
    }
    
    int cursor = 0;
    
    for (uint t = 0; t < T; ++t)
    {
        cursor = findNextWordStart (inbuffer, bytesRead, cursor);
        
        vector<int> numbers;

        unsigned int start = 1024;
        
        int histogram[256];
        
        memset(histogram, 0, sizeof(histogram));
        
        while (cursor<bytesRead && inbuffer[cursor] >= 'A' && inbuffer[cursor] <= 'Z')
        {
            ++histogram[inbuffer[cursor]];
            ++cursor;
        }
        
        /* do the stuff */

        printhistogram (histogram);
        int occurence;
        
        occurence = histogram['Z'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(0);
            decreaseWithString(histogram, numbertexts[0]);
        }

        occurence = histogram['W'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(2);
            decreaseWithString(histogram, numbertexts[2]);
        }

        occurence = histogram['U'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(4);
            decreaseWithString(histogram, numbertexts[4]);
        }
        
        occurence = histogram['X'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(6);
            decreaseWithString(histogram, numbertexts[6]);
        }

        occurence = histogram['G'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(8);
            decreaseWithString(histogram, numbertexts[8]);
        }
        
        occurence = histogram['O'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(1);
            decreaseWithString(histogram, numbertexts[1]);
        }
        
        occurence = histogram['H'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(3);
            decreaseWithString(histogram, numbertexts[3]);
        }
        
        occurence = histogram['F'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(5);
            decreaseWithString(histogram, numbertexts[5]);
        }
        
        occurence = histogram['S'];
        for (int i = 0; i < occurence; ++i) 
        {
            numbers.push_back(7);
            decreaseWithString(histogram, numbertexts[7]);
        }
                
        occurence = histogram['E'];
        for (int i = 0; i < occurence; ++i) 
        {   
            numbers.push_back(9);
            decreaseWithString(histogram, numbertexts[9]);
        }
        
        sort(numbers.begin(), numbers.end());
        
        printf ("Case #%d: ", t+1);
        for (int i = 0; i<numbers.size(); ++i )
        {
            printf ("%d", numbers[i]);
        }
        printf ("\n");
        fprintf (stderr, "------------------------------\n");
    }
}

#if 0
char grid[100][100];

class Line
{
    vector
}

set<string> lines;

int main(int argc, char** argv) {
    unsigned int T = 0;
    scanf ("%u", &T);

    fprintf (stderr, "Doing %d testcases\n", T);
    
    for (uint t = 0; t < T; ++t)
    {
        uint N;
        
        scanf ("%u", &N);
        
        for (uint line = 0; line < 2*N-1; ++line)
        {
            for (uint height = 0; height < N; ++height)
            {
                uint h;
                scanf ("%d", &h);
                lines += '0'+h
            }
        }

        
        cursor = findNextWordStart (inbuffer, bytesRead, cursor);

        unsigned int start = 1024;
        unsigned int len = 0;
        
        while (cursor<bytesRead && inbuffer[cursor] >= 'A' && inbuffer[cursor] <= 'Z')
        {
            if (len == 0)
            {
                outbuffer[start] = inbuffer[cursor];
            } else {
                if (inbuffer[cursor] >= outbuffer[start])
                {
                    start--;
                    outbuffer[start] = inbuffer[cursor];
                } else 
                {
                    outbuffer[start+len] = inbuffer[cursor];
                }                    
            }
            ++len;
            ++cursor;
        }
        printf ("Case #%d: ", t+1);
        fwrite(outbuffer+start, 1, len ,stdout);
        printf ("\n");
    }
}
#endif



#if 0
char inbuffer[1024*1024];
char outbuffer[10*1024];

size_t findNextWordStart (char *buf, size_t bufsize, size_t c)
{
    while (c<bufsize && (buf[c] < 'A' || buf[c] > 'Z'))
        ++c;
    return c;
}

int main(int argc, char** argv) {

    unsigned int T = 0;
    scanf ("%u", &T);

    fprintf (stderr, "Doing %d testcases\n", T);
    
    ssize_t bytesRead = fread(inbuffer, 1, sizeof(inbuffer), stdin);
    if (bytesRead < 0 || (size_t)bytesRead >= sizeof(inbuffer))
    {
        fprintf (stderr, "Need more memory!\n");
        return 0;
    }
    
    int cursor = 0;
    
    for (uint t = 0; t < T; ++t)
    {
        cursor = findNextWordStart (inbuffer, bytesRead, cursor);

        unsigned int start = 1024;
        unsigned int len = 0;
        
        while (cursor<bytesRead && inbuffer[cursor] >= 'A' && inbuffer[cursor] <= 'Z')
        {
            if (len == 0)
            {
                outbuffer[start] = inbuffer[cursor];
            } else {
                if (inbuffer[cursor] >= outbuffer[start])
                {
                    start--;
                    outbuffer[start] = inbuffer[cursor];
                } else 
                {
                    outbuffer[start+len] = inbuffer[cursor];
                }                    
            }
            ++len;
            ++cursor;
        }
        printf ("Case #%d: ", t+1);
        fwrite(outbuffer+start, 1, len ,stdout);
        printf ("\n");
    }
    
    
    
    

    
}

#endif


#if 0
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
#endif
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
