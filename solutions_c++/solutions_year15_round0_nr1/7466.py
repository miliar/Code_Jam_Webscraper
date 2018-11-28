#include <cstdio>

#define MAX 1002

using namespace std;

int main()
{
    int test_case;
    char input[MAX];
    long count;
    int answer;
    int max_shyness;
    scanf("%d", &test_case);
    for(int i = 1; i <= test_case; ++i)
    {
        scanf("%d", &max_shyness);
        scanf("%s",input);
        count = 0;
        answer = 0;
        for(int j = 0; j <= max_shyness; ++j)
        {
            if(count < j)
            {
                ++count;
                ++answer;
            }
            count += (input[j]-'0');
        }
        printf("Case #%d: %d\n",i,answer);
    }
    return 0;
}

