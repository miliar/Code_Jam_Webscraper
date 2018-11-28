#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include<cstring>

using namespace std;
int n,m;
int A[101][101];
bool solve()
{
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<m; j++)
        {
            bool row=1,col=1;

            for (int w=0; w<n; w++)
            {

                if(A[w][j]>A[i][j])
                {
                    col=0;
                    break;
                }

            }

            for (int w=0; w<m; w++)
            {

                if(A[i][w]>A[i][j])
                {
                    row=0;
                    break;
                }

            }

            if(row==0&&col==0)
                return 0;


        }
    }
    return 1;
}

int main()

{

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
        memset(A,0,sizeof A);


        scanf("%d %d",&n,&m);

        for (int j=0; j<n; j++)
        {
            for (int k=0; k<m; k++)
            {
                int c;
                scanf("%d",&c);
                A[j][k]=c;

            }

        }
        bool ans=solve();
        if(ans)
            printf("Case #%d: YES\n",i);

        else
            printf("Case #%d: NO\n",i);


    }

}

