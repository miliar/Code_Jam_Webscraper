#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;

int T;
int N;
double A[1000+1],B[1000+1];
int Y,Z;
bool used[1000+1];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("lyzout.txt","w",stdout);
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++)
	{
		scanf("%d",&N);
		for (int i=1;i<=N;i++)
			scanf("%lf",&A[i]);
		for (int i=1;i<=N;i++)
			scanf("%lf",&B[i]);
		sort(A+1,A+N+1);
		sort(B+1,B+1+N);
		/*for (int i=1;i<=N;i++)
            cout << A[i] << ' ';
        cout << endl;
        for (int i=1;i<=N;9i++)
            cout << B[i] << ' ';
        cout << endl;*/
		Y=Z=0;
		memset(used,0,sizeof used);
		for (int i=1;i<=N;i++)
			for (int j=1;j<=N;j++)
				if (!used[j] && A[i]>B[j])
				{
					++Y;
					used[j]=true;
					break;
				}

        memset(used,0,sizeof used);
		for (int i=1;i<=N;i++)
        {
            int j;
            for (j=1;j<=N;j++)
                if (A[i]<B[j] && !used[j])
                {
                    used[j]=true;
                        break;
                }
            if (j==N+1) ++Z;
        }
		printf("Case #%d: %d %d\n",Case,Y,Z);
	}

    return 0;
}
