# include<cstdio>
# include<iostream>
# include<fstream>
# include<algorithm>
# include<functional>
# include<cstring>
# include<string>
# include<cstdlib>
# include<iomanip>
# include<numeric>
# include<cctype>
# include<cmath>
# include<ctime>
# include<queue>
# include<stack>
# include<list>
# include<set>
# include<map>

using namespace std;

const double PI=4.0*atan(1.0);

typedef long long LL;
typedef unsigned long long ULL;

# define inf 999999999
# define MAX 1234

char s[MAX];
int a[MAX];

int main(void)
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("ddddlarge.out","w",stdout);

    int icase = 1;
    int t;cin>>t;
    while ( t-- )
    {
        int x,r,c;
        cin>>x>>r>>c;

        printf("Case #%d: ",icase++);
        if ( x==1 )
        {
            printf("GABRIEL\n");
            continue;
        }
        else if ( x==2 )
        {
            if ( (r*c)%2==0 )
            {
                 printf("GABRIEL\n");
            }
            else
            {
                printf("RICHARD\n");
            }
        }
        else if ( x==3 )
        {
            if ( r==3&&(c==3||c==4) )
            {
                 printf("GABRIEL\n");
            }
            else if ( c==3&&(r==3||r==4) )
            {
                 printf("GABRIEL\n");
            }
            else if ( r==2&&c==3 )
            {
                printf("GABRIEL\n");
            }
            else if ( r==3&&c==2 )
            {

                printf("GABRIEL\n");
            }
            else
            {
                printf("RICHARD\n");
            }
        }
        else
        {
            if ( r==3&&c==4 )
            {
                 printf("GABRIEL\n");
            }
            else if ( c==3&&r==4 )
            {
                 printf("GABRIEL\n");
            }
            else if ( c==4&&r==4 )
            {
                printf("GABRIEL\n");
            }
            else
            {
                printf("RICHARD\n");
            }
        }

    }



	return 0;
}
