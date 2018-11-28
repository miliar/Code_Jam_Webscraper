#include <vector>
#include <string>
#include<fstream>
#include<math.h>
#include<stdio.h>

using namespace std;
int mylog(int c,int w)
{
    if(w==1)
        return c-1;
    else
    {
        double temp=(double)c/(double)w;
        return ceil(temp)-1;
    }
    return -1;
}

int main()
{
    //freopen("practice.in","r",stdin);
	//freopen("A-large.in","r",stdin);
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	int test,q;
	scanf("%d",&test);
	for(q=1;q<=test;q++)
    {
        int ans,i,r,c,w;
        ans=0;
        scanf("%d %d %d",&r,&c,&w);
        ans+=(r-1)*c;
        ans+=w;

        ans+=mylog(c,w);
        printf("Case #%d: ",q);
        printf("%d\n",ans);
    }

	return 0;
}


