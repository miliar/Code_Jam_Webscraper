#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>
#include<string>
#define REP(it,end) for (int it = 1; it <= (end); it++)
#define FOR(it,begin,end) for (int it = (begin); it <= (end); it++)
#define ROF(it,begin,end) for (int it = (begin); it >= (end); it--)
using namespace std;

int ans[17];
int a[6][6];

int main()
{int k,row,t,i,j,con,numchose,timuno=0;
 freopen("A-small-attempt3.in","r",stdin);
 FILE *fp=fopen("ans.out","w");
 //FILE *fpc=fopen("in.in","w");
 scanf("%d",&t);
 while(t--)
 {memset(ans,0,sizeof(ans));
  con=0;
  timuno++;
 // fprintf(fpc,"case#%d :\n",timuno);
 for(k=0;k<2;k++)
 {scanf("%d",&row);
 // fprintf(fpc,"%d\n",row);
  for(i=1;i<=4;i++)
   {for(j=1;j<=4;j++)
    {scanf("%d",&a[i][j]);
   //  fprintf(fpc,"%d ",a[i][j]);
    }
   //  fprintf(fpc,"\n");
   }
   for(i=1;i<=4;i++)ans[a[row][i]]++;
 }
 for(k=1;k<=16;k++)if(ans[k]==2){con++;numchose=k;}
 if(con==1)fprintf(fp,"Case #%d: %d\n",timuno,numchose);
 else if(con>1)fprintf(fp,"Case #%d: Bad magician!\n",timuno);
 else if(con==0)fprintf(fp,"Case #%d: Volunteer cheated!\n",timuno);
 }
 return 0;
}
