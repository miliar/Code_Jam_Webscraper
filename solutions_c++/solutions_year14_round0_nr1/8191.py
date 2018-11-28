#include<bits/stdc++.h>
#define pb push_back
#define sz(x) (int)x.size()
#define scf scanf
#define ptf printf
#define fst first
#define scd second
#define forp(i,j,k) for(int i=j;i<k;i++)
#define form(i,j,k) for(int i=j;i>k;i--)
using namespace std;
typedef long long LL;

int cnt[20];

int main()
{
	int T,x,y;
	scf("%d",&T);
	forp(tcnt,0,T)
	{
		memset(cnt,0,sizeof(cnt));
		scf("%d",&x);x--;
		forp(i,0,4)
			forp(j,0,4)
			{
				scf("%d",&y);
				if(x==i)cnt[y]++;
			}
		scf("%d",&x);x--;
		forp(i,0,4)
			forp(j,0,4)
			{
				scf("%d",&y);
				if(x==i)cnt[y]++;
			}
		int t0=0,t1;
		forp(i,1,17)if(cnt[i]>1)t0++,t1=i;
		ptf("Case #%d: ",tcnt+1);
		if(!t0){puts("Volunteer cheated!");continue;}
		if(t0>1){puts("Bad magician!");continue;}
		ptf("%d\n",t1);
	}
    return 0;
}
