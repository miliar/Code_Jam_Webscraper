#include <cstdio>
#include <math.h>
FILE *f,*g;
int v[1010];
int t[1010];
int d[1010];



void pre()
{
    int i,j,mx,mxi;

    t[2] = 1;
    for (i=3;i<=1000;i++)
    {
        mxi = 1;
        mx = d[1]+d[i-1];
        for (j=2;j<i;j++)
            if (d[j]+d[i-j]<mx)
            {
                mx = d[j]+d[i-j];
                mxi = j;
            }
        d[i] = mx+1;
        t[i] = mxi;
    }
}



/*
12 - 1
6 6 - 2
3 3 3 3 - 4
1 2 1 2 1 2 1 2

12 - 1
4 8 - 2
2 2 4 4 - 2
2 2 2 2 2 2
*/

int main()
{
    f=fopen("input.txt","r");
    g=fopen("output.txt","w");

     int q,i,T,n,cnt,ans,x,mx;

    pre();
    fscanf(f,"%d",&T);



    for (q=1;q<=T;q++)
    {
        for (i=1;i<=1000;i++)
            v[i] = 0;

        fscanf(f,"%d",&n);
        for (i=1;i<=n;i++)
        {
            fscanf(f,"%d",&x);
            v[x]++;
        }

        /*
        for (i=1000;v[i]==0;i--);

        ans = i;
        mx = i;


        for (cnt=1;cnt<mx && i>1;cnt++)
        {
            v[i/2]++;
            v[i/2+i%2]++;
            int rad = sqrt(i);
            rad = i /rad;
            if (rad==i) rad--;


          // v[rad]++;
          // v[i-rad]++;

            v[i]--;
            while (v[i]==0) i--;

            if (i+cnt < ans)  ans = i+cnt;
        }
        */

        ans = -1;
        for (i=1;i<=10;i++)
        {
            int cost = i;
            for (int j=1;j<=10;j++)
                if (j%i!=0)
                    cost += (j/i) *v[j];
                else
                    cost += (j/i-1) *v[j];

            if (ans == -1 || cost<ans) ans = cost;
        }


        fprintf(g,"Case #%d: %d\n",q,ans);
    }


}
