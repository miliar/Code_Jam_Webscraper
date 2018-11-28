#include<cstdio>
#include<cstring>

char swap(char c)
{
    if (c == '+')
        return '-';
    else
        return '+';
}

int main(int argc, char** argv)
{
    int t, k, len, count;
    bool flag;
    char str[1001] = {'\0'};

    FILE *input, *output;

    if (argc != 3)
    {
        printf("input을 제대로 넣어주세요.\n");
        return 0;
    }

    input = fopen(argv[1], "r+");
    output = fopen(argv[2], "w+");

    fscanf(input, "%d", &t);

    for (int i = 1; i <= t; i++)
    {
        flag = true;
        count = 0;

        fscanf(input, "%s %d", str, &k);

        len = strlen(str);
        for (int j = 0; j < len - k + 1; j++)
        {
            if (str[j] == '-')
            {
                count++;
                for (int l = j; l < j + k; l++)
                    str[l] = swap(str[l]);
            }
        }

        for (int j = len - k; j < len; j++)
        {
            if (str[j] == '-')
                flag = false;
        }

        if (flag)
            fprintf(output, "Case #%d: %d\n", i, count);
        else
            fprintf(output, "Case #%d: IMPOSSIBLE\n", i);
    }

    fclose(input);
    fclose(output);

    return 0;
}
