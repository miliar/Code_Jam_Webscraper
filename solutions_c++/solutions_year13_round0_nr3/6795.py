#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

bool IsSqure(int n)
{
    double fsqrt = sqrt(n);
    int m = fsqrt;
    return m*m == n;
}
bool IsPal(char *str)
{
    int front;
    int back;
    bool flag = true;
    for(front=0, back=(strlen(str)-1);front<=back;++front,--back)
    {
        if(str[front]!=str[back])
        {
            flag=false;
            break;
        }
    }
    if(flag)
        return true;
    else
        return false;
}

int main()
{
    freopen ("C-small-attempt0.in","r",stdin);
    freopen ("out_c.out", "w",stdout);

    int testCase;
    int count = 1;
    scanf("%d", &testCase);
    while(count <= testCase)
    {
        int start, end;
        int num=0;

        scanf("%d%d", &start, &end);
        for(int i=start;i<=end;i++)
        {
            if(IsSqure(i)==true)
            {   char str1[10];
                int x = sqrt(i);
                sprintf (str1,"%d",x);
                if(IsPal(str1))
                {
                    char str2[10];
                    sprintf (str2,"%d",i);
                    if(IsPal(str2))
                        num++;
                }
            }
        }
        printf("Case #%d: %d\n", count, num);
        count++;
    }

}
