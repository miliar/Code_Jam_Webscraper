#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int double_cmp(const void *x, const void *y)
{
  double xx = *(double*)x, yy = *(double*)y;
  if (xx < yy) return -1;
  if (xx > yy) return  1;
  return 0;
}

int main()
{
    int test, i, N, chk_ind, cnt1, cnt2, cs = 1;
    double p1[1001], p2[1001];

    //freopen("D-large.in", "r", stdin);
    //freopen("D-large.out", "w", stdout);

    cin>>test;
    while(test--)
    {
        cin>>N;
        for(i=0;i<N;i++)
        {
            cin>>p1[i];
        }
        for(i=0;i<N;i++)
        {
            cin>>p2[i];
        }
        qsort(p1, N, sizeof(double), double_cmp);
        qsort(p2, N, sizeof(double), double_cmp);

        chk_ind = N-1;
        cnt2 = 0;
        for(i=N-1; i >= 0 && chk_ind >= 0; i--)
        {
            if(p1[i] > p2[chk_ind])
            {
                cnt2++;
            }
            else
            {
                chk_ind--;
            }
        }
        //printf("cnt2: %d\n", cnt2);
        chk_ind = N-1;
        cnt1 = 0;
        for(i=N-1; i >= 0 && chk_ind >= 0; i--)
        {
            if(p1[chk_ind] < p2[i])
            {
                cnt1++;
            }
            else
            {
                chk_ind--;
            }
        }
        //printf("cnt1: %d\n", N-cnt1);
        printf("Case #%d: %d %d\n", cs++, N-cnt1, cnt2);
    }
    return 0;
}
