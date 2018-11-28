#include <cstdio>

using namespace std;

int main()
{
    short a[5][4],b[4],t1,i,j,t,nr,d,q;
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    scanf("%hd",&t);
    for(t1=1;t1<=t;++t1)
    {
        scanf("%hd",&d);
        for(i=1;i<=4;++i)
        for(j=0;j<4;++j)
        scanf("%hd",&a[i][j]);
        b[0]=a[d][0];
        b[1]=a[d][1];
        b[2]=a[d][2];
        b[3]=a[d][3];
        scanf("%hd",&d);
        for(i=1;i<=4;++i)
        for(j=0;j<4;++j)
        scanf("%hd",&a[i][j]);
        nr=0;
        for(i=0;i<4&&nr<=1;++i)
        for(j=0;j<4&&nr<=1;++j)
        if (b[i]==a[d][j])
        {
            ++nr;
            q=i;
        }
        if(nr==1) printf("Case #%hd: %hd\n",t1,b[q]);
        else if(nr==0) printf("Case #%hd: Volunteer cheated!\n",t1);
        else  printf("Case #%hd: Bad magician!\n",t1);
    }
    return 0;
}
