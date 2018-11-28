#include <stdio.h>
#include <stdlib.h>

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX	(1000)

int main(void)
{
    uint32 T = 0;
    char sq[4][4];
    int32 win_o_ch = 0;
    int32 win_x_ch = 0;
    int32 win_o = 0;
    int32 win_x = 0;
    int32 cnt_o = 0, cnt_x = 0, cnt_t = 0;

    scanf("%d", &T);

  for (int32 n=0; n<T; n++)
  {
	win_x = 0;
	win_o = 0;
	win_o_ch = 0;
	win_x_ch = 0;

    scanf("%4s", &sq[0]);
    scanf("%4s", &sq[1]);
    scanf("%4s", &sq[2]);
    scanf("%4s", &sq[3]);

    for (int32 j=0; j<4; j++)
    {
        cnt_x = 0;
        cnt_o = 0;
        cnt_t = 0;
        for (int32 i=0; i<4; i++)
        {
            if (sq[j][i] == 'O')
                cnt_o += 1;
            else if (sq[j][i] == 'X')
                cnt_x += 1;
            else if (sq[j][i] == 'T')
            {
                cnt_t += 1;
            }
        }
        if ((cnt_x + cnt_t) == 4)
            win_x = 1;
        else if ((cnt_o + cnt_t) == 4)
            win_o = 1;
        else if (cnt_o == 0)
            win_x_ch += 1;
        else if (cnt_x == 0)
            win_o_ch += 1;
    }

    for (int32 j=0; j<4; j++)
    {
        cnt_x = 0;
        cnt_o = 0;
        cnt_t = 0;
        for (int32 i=0; i<4; i++)
        {
            if (sq[i][j] == 'O')
                cnt_o += 1;
            else if (sq[i][j] == 'X')
                cnt_x += 1;
            else if (sq[i][j] == 'T')
            {
                cnt_t += 1;
            }
        }
        if ((cnt_x + cnt_t) == 4)
            win_x = 1;
        else if ((cnt_o + cnt_t) == 4)
            win_o = 1;
        else if (cnt_o == 0)
            win_x_ch += 1;
        else if (cnt_x == 0)
            win_o_ch += 1;
    }

        cnt_x = 0;
        cnt_o = 0;
        cnt_t = 0;
        for (int32 i=0; i<4; i++)
        {
            if (sq[i][i] == 'O')
                cnt_o += 1;
            else if (sq[i][i] == 'X')
                cnt_x += 1;
            else if (sq[i][i] == 'T')
            {
                cnt_t += 1;
            }
        }
        if ((cnt_x + cnt_t) == 4)
            win_x = 1;
        else if ((cnt_o + cnt_t) == 4)
            win_o = 1;
        else if (cnt_o == 0)
            win_x_ch += 1;
        else if (cnt_x == 0)
            win_o_ch += 1;
    


        cnt_x = 0;
        cnt_o = 0;
        cnt_t = 0;
        for (int32 i=0; i<4; i++)
        {
            if (sq[3-i][i] == 'O')
                cnt_o += 1;
            else if (sq[3-i][i] == 'X')
                cnt_x += 1;
            else if (sq[3-i][i] == 'T')
            {
                cnt_t += 1;
            }
        }
        if ((cnt_x + cnt_t) == 4)
            win_x = 1;
        else if ((cnt_o + cnt_t) == 4)
            win_o = 1;
        else if (cnt_o == 0)
            win_x_ch += 1;
        else if (cnt_x == 0)
            win_o_ch += 1;


    printf("Case #%d: ", n + 1);
    if (win_x)
        printf("X won\n");
    else if (win_o)
        printf("O won\n");
    else if (win_o_ch == 0 && win_x_ch == 0)
        printf("Draw\n");
    else 
        printf("Game has not completed\n");
  }



  return 0;
}


