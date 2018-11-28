#include <cstdio>
#include <algorithm>

using namespace std;

double Naomi[1001];
double Ken[1001];

int main()
{
    int t, n;
    scanf("%d", &t);
    for(int k=1; k<=t; k++)
    {
        int War = 0;
        int D_War = 0;

        scanf("%d", &n);
        for(int i=0; i<n; i++)
            scanf("%lf", &Naomi[i]);
        for(int i=0; i<n; i++)
            scanf("%lf", &Ken[i]);

        sort(Naomi, Naomi+n);
        sort(Ken, Ken+n);

        //war
        int Kp = 0; int Np = 0;

        for(int i=0; i<n;)
        {
            while(Naomi[Np] > Ken[Kp] && Kp<n)
            {
                Kp++;
                i++;
            }
            if(Kp<n)
            {
                Np++;
                Kp++;
                i++;
            }
        }
        War = Kp-Np;

        //D_war

        Kp = 0; Np = 0;
        int Kq = n-1; int Nq = n-1;

        for(int i=0; i<n;)
        {
            printf("!: %lf, %lf\n", Ken[Kp], Naomi[Np]);
            if(Ken[Kp] > Naomi[Np])
            {
                Kq--;
                Np++;
                i++;
            }
            else
            {
                Kp++;
                Np++;
                i++;
                D_War++;
            }
        }
        printf("Case #%d: %d %d\n", k, D_War, War);
        for(int i=0; i<=n; i++) Ken[i] = Naomi[i] = 0;
    }
    return 0;
}
