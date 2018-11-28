#include <iostream>
using namespace std;

int char_to_int(char c)
{
    return c - '0';
};

int main()
{
    int T;
    scanf("%d", &T);
    
    int S, count, result;
    char data[1001];
    
    for (int i = 1; i <= T; ++i)
    {
        scanf("%d", &S);
        scanf("%s", data);

        result = 0;
        count = char_to_int(data[0]);
        for (int j = 1; j <= S; ++j) 
        {
            int current = char_to_int(data[j]);

            if (count < j)
            {
                result += j - count;
                count = j + current;
            }
            else
            {
                count += current;    
            }
        }

        printf("Case #%d: %d\n", i, result);
    }
}