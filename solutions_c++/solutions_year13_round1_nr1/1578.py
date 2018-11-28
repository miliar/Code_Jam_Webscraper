#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

main()
{
 int i, j, k, l;
 int no_cases;
 char buf[1001];
 int r, t;
 char *buf2;

 gets(buf);
 no_cases=atoi(buf);
// printf("buf=%s, no_cases=%d", buf, no_cases);
 for (i = 1; i <= no_cases; i++)
   {
    int count;
    gets(buf);
    buf2 = strtok(buf, " \t\r\n");
    r = atoi(buf2);
    buf2 = strtok(NULL, " \t\r\n");
    t = atoi(buf2);
    printf("Case #%d: ", i);
//    printf("r=%d, t=%d\n", r, t);
    count = 0;
    while (t >= 0)
       {
        int area1, area2;
        area1 = r * r;
        area2 = (r+1) * (r+1);
        int area = area2 - area1;
        t -= area;
        r += 2;
        count++;
       }
    count--;
    printf("%d\n", count);
   }
 
}

