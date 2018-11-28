#include<cstdio>
#include<iostream>

using namespace std;

int t;
double c,f,x;
double g[1000000]={0};

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d",&t);
    for (int k = 1; k <= t; k++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        g[0] = 0;
        int i =1;
        double res = x/2,temp = 0;
        while (true)
        {
            g[i] = g[i-1] + c / (f * (double) (i-1) + 2);
            temp = g[i] + x /  (f * (double) i + 2);
            if (temp > res) { break; }
            else { res=temp; }
            i++;
        }
        printf("Case #%d: %.7lf\n", k, res);

    }

    fclose(stdin);
    fclose(stdout);

}

