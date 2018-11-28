#include <stdio.h>

char dir_x[] = "EW";
char dir_y[] = "NS";

void simple(int dis, char *dir)
{
    if (dis == 0)
        return;

    if (dis > 0)
    {
        while (dis--)
        {
            printf("%c%c", dir[1], dir[0]);
        }
    }
    else
    {
        dis = -dis;

        while (dis--)
        {
            printf("%c%c", dir[0], dir[1]);
        }
    }

}

void run(int x, int y)
{
    simple(x, dir_x);
    simple(y, dir_y);
    printf("\n");
}

int main()
{
    int num_case;

    scanf("%d", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        int x, y;
        scanf("%d %d", &x, &y);

        printf("Case #%d: ", i);
        run(x, y);
    }

    return 0;
}
