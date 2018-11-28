#include<stdio.h>
#include <stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;

bool cmp(int a,int b)
{
    return a>b;
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T,TC;

	scanf("%d",&T);
	for(TC=1;TC<=T;TC++)
    {
        printf("Case #%d: ", TC);
        int N;
        int m[2000];
        int m1[2000];
        int ans1=0;
        int ans2=0;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&m[i]);

        }
        for(int i=1;i<N;i++)
        {
            m1[i-1]=m[i-1]-m[i];

        }
        sort(m1,m1+N-1,cmp);
        for(int i=1;i<N;i++)
        {
            if(m[i]>m[i-1])
            {
                continue;
            }
            else{ans1+=(m[i-1]-m[i]);}
        }

        for(int i=0;i<N-1;i++)
        {
            if(m[i]>=m1[0])
            {
                ans2+=m1[0];
            }
            else{ans2+=(m[i]);}
        }





        printf("%d %d\n", ans1, ans2);

    }

}
