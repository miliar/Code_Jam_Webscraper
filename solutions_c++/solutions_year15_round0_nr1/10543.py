#include <stdio.h>
#include <algorithm>
using namespace std;

//int x[1000001],y[1000001];
//int N,c[1000][1000];
//int dx[4] = {0,1,0,-1};
//int dy[4] = {1,0,-1,0};
int smax, shy[10], person, myfriend, str;

int main()
{
	freopen ("1.in","r",stdin);
	freopen ("1.out","w",stdout);

	int Test; scanf ("%d",&Test);
	for (int Case=1;Case<=Test;Case++)
        {
            printf ("Case #%d: ",Case);
            scanf ("%d",&smax);
            person=0;
            myfriend=0;
            scanf("%d",&str);
            for(int i=smax;i>=0;i--)
            {
                shy[i]=str%10;
                str=str/10;
            }
            for (int i=0;i<=smax;i++)
            {
                while(i>person)
                {
                    myfriend++;
                    person++;
                }
                person=person+shy[i];

			}
			printf("%d\n",myfriend);
		}

	return 0;
}
