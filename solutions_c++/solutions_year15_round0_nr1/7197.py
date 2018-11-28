#include <cstdio>

using namespace std;

int main ()
{
  int T, i, j, s_max, st_now, ans;
  char aud[1010];
  FILE *fp, *fd;
  fp = fopen ("input.txt", "r");
  fd = fopen ("output.txt", "w");
  fscanf (fp, "%d", &T);
  for (i = 1; i <= T; i++)
  {
    fscanf (fp, "%d", &s_max);
    fscanf (fp, "%s", aud);
    st_now = 0;
    ans = 0;
    for (j = 0; j <= s_max; j++)
    {
      if ((aud[j]-'0') > 0)
      {
        if (st_now < j)
        {
          ans = ans + (j-st_now);
          st_now = j;
        }
        st_now = st_now + (aud[j]-'0');
      } 
    }
    fprintf (fd, "Case #%d: %d\n", i, ans);
  }
  fclose (fp);
  fclose (fd);
}
