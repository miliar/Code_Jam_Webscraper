#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std;

char array[110];
int flag = 0;

void change()
{

    flag = (flag + 1) % 2;
}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int tc = 0;
    scanf("%d", &tc);
    int cs = 1;

    while(tc--)
    {

        int i = 0;
        scanf("%s", &array);
        flag = 0;
        int len = strlen(array);
        i = len - 1;
        int count = 0;

        while(i >= 0)
        {
            if(flag == 0)
            {
                char x = array[i];
                if(x != '+')
                {
                    count++;
                    change();
                }
            }
            else
            {
                char x = array[i];
                if(x != '-')
                {
                    count++;
                    change();
                }
            }

            i--;

        }

        printf("Case #%d: %d\n", cs++, count);

    }
    return 0;
}
