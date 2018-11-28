#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T;
int a[5][5] =  {{0, 0, 0, 0, 0},
                {0, 1, 2, 3, 4},
                {0, 2,-1, 4,-3},
                {0, 3,-4,-1, 2},
                {0, 4, 3,-2,-1}};
int ans;
char s[10005];
int L;
long long X;
int main()
{
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);

    cin>>T;
    int t = 0;
    while(t < T)
    {

        ans = 1;
        cin>>L>>X;
        cin>>s;
        t++;
        printf("Case #%d: ",t);
        int l = 0;
        long long x = 1;
        int des = 2;
        int cur = 1;
        int neg = 1;
        int xnum = 0;
        while(x <= X && des <= 4)
        {
            while(l < L)
            {
                int k = s[l] - 'g';
                cur = a[cur][k];
                if (cur*neg == des)
                {
                    des++;
                    cur = 1;
                    neg = 1;
                    xnum = 0;
                    l++;
                    break;
                }
                if (cur < 0)
                {
                    cur = -cur;
                    neg = -neg;
                }
                l++;
            }
            if (l == L )
            {
                l = 0;
                x++;
                xnum++;
                if (xnum >= 5) { ans = 0; break;}

            }
            if (ans == 0) break;
        }
        if (des == 5)
        {
            if (x <= X)
            {
                int cur1,neg1,cur2,neg2;
                cur1 = neg1 = cur2 = neg2 = 1;
                for(int i = l; i < L; i++)
                {
                    int k = s[i] - 'g';
                    cur1 = a[cur1][k];
                    if (cur1 < 0)
                    {
                        cur1 = -cur1;
                        neg1 = -neg1;
                    }
                }
                for (int i = 0; i < l;i++)
                {
                    int k = s[i] - 'g';
                    cur2 = a[cur2][k];
                    if (cur2 < 0)
                    {
                        cur2 = -cur2;
                        neg2 = -neg2;
                    }
                }
                cur2 = a[cur2][cur1];
                neg2 *= neg1;
                if (cur2 < 0) { cur2 = -cur2; neg2 = -neg2; }
                int xx = X - x;
                xx = xx % 4;
                if (xx == 0)
                {
                    cur2 = 1;
                    neg2 = 1;
                }else
                if (xx == 1)
                {
                    cur2 = cur2;
                    neg2 = neg2;
                }else
                if (xx == 2)
                {
                    if (cur2 != 1) { cur2 = 1; neg2 = -1; }
                    else { cur2 = 1; neg2 = 1; }
                }else
                if (xx == 3)
                {
                    int jc2 = cur2;
                    int jn2 = neg2;
                    cur2 = a[cur2][cur2];
                    neg2 = 1;
                    if (cur2 < 0) { cur2 = 1; neg2 = -1;}
                    cur2 = a[cur2][jc2];
                    neg2 *= jn2;
                }
                cur1 = a[cur1][cur2];
                neg1 *= neg2;
                if (cur1 * neg1 != 1) ans = 0;
            }
        }
        else if (des < 5)
        {
            ans = 0;
        }
        if (ans) printf("YES\n"); else printf("NO\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
