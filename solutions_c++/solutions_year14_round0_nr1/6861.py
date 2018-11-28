#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <map>

void
get_cols(char *buf, int *vals)
{
    char *ptr = buf;
    char *p2;
    int c = 0;
    while ((p2 = strchr(ptr, ' ')) != NULL)
    {
        *p2 = '\0';
        int val = atoi(ptr);
        vals[c] = val;
        c++;
        ptr = p2+1;
    }

    int val = atoi(ptr);
    vals[c] = val;
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
    int num_tests = atoi(buf);

    //printf("Got %d tests\n", num_tests);

    for (int test_num = 0; test_num < num_tests; test_num++)
    {
        fgets(buf, 10001, f);
        int answer1 = atoi(buf);
        int mat1[16];
        for (int r = 0; r < 4; r++)
        {
            fgets(buf, 10001, f);
            int vals[6];
            get_cols(buf, vals);
            for (int c = 0; c < 4; c++)
            {
                mat1[(r * 4)+c] = vals[c];
            }
        }

        fgets(buf, 10001, f);
        int answer2 = atoi(buf);
        int mat2[16];
        for (int r = 0; r < 4; r++)
        {
            fgets(buf, 10001, f);
            int vals[6];
            get_cols(buf, vals);
            for (int c = 0; c < 4; c++)
            {
                mat2[(r * 4)+c] = vals[c];
            }
        }

        std::map<int, int> m;
        for (int c = 0; c < 4; c++)
        {
            int v1 = mat1[((answer1-1)*4)+c];
            int v2 = mat2[((answer2-1)*4)+c];

            std::map<int, int>::iterator it = m.find(v1);
            if (it == m.end())
                m[v1] = 1;
            else
                (*it).second += 1;

            it = m.find(v2);
            if (it == m.end())
                m[v2] = 1;
            else
                (*it).second += 1;
        }

        std::map<int, int>::const_iterator it;
        int num_mults = 0;
        int soln = 0;
        for (it = m.begin(); it != m.end(); ++it)
        {
            if ((*it).second > 1)
            {
                soln = (*it).first;
                num_mults++;
            }
        }

        char answer[100];
        if (num_mults > 1)
            strcpy(answer, "Bad magician!");
        else if (num_mults == 0)
            strcpy(answer, "Volunteer cheated!");
        else
            sprintf(answer, "%d", soln);
        printf("Case #%d: %s\n", test_num+1, answer);
        //printf("Got %.0f - %.0f\n", lower, upper);
    }

    fclose(f);

    return 0;
}
