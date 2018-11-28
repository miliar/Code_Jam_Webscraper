#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int T,i,j,t,e,q,w;
char a[105][105];
bool flag,flag1,flag2,flag3,flag4;
int main()
{
	freopen("2.out","w",stdout);
    cin >> T;
    for (i=0;i<T;i++)
    {
	flag=1;
        cin >> q >> w;
	printf("Case #%d: ",i+1);
	for (j=0;j<q;j++)
		for (t=0;t<w;t++)
			cin >> a[j][t];
	for (j=0;j<q && flag;j++)
		for (t=0;t<w && flag;t++)
			{
				flag1=flag2=flag3=flag4=0;
				/*if (j==0)
					flag1=1;
				if (j==q-1)
					flag2=1;
				if (t==0)
					flag3=1;
				if (t==w-1)
					flag4=1;*/
				for (e=0;e<j;e++)
					if (a[j][t]<a[e][t])
						flag1=1;
				for (e=j+1;e<q;e++)
					if (a[j][t]<a[e][t])
						flag2=1;
				for (e=0;e<t;e++)
					if (a[j][t]<a[j][e])
						flag3=1;
				for (e=t+1;e<w;e++)
					if (a[j][t]<a[j][e])
						flag4=1;
				if ((flag1==1 && flag1==flag3) || 
(flag2==1 && flag2==flag3) ||
(flag1==1 && flag1==flag4) ||
(flag2==1 && flag2==flag4))
					{printf("NO\n");flag=0;}
			}
	if (flag)
		printf("YES\n");
    }
    return 0;
}

