#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

char t[8][11];
int ssn[80];
int ssl[80];
int nbss;
bool has_ss[8][80];
int n;
int m;

int serv[8];
int scores[400];


bool samess(int a, int b, int len)
{
  for(int i = 0; i < len; i++)
    if(t[a][i]==0 || t[b][i]==0 || t[a][i]!=t[b][i])
      return false;
  return true;
}

void makess()
{
  for(int i = 0; i < m; i++)
    {
      int len=1;
      while(t[i][len-1]!=0)
	{
	  bool isnew=true;
	  for(int j=0;j<nbss;j++)
	    if(ssl[j]==len && samess(ssn[j],i,len))
	      {isnew=false;has_ss[i][j]=true;}
	  if(isnew)
	    {
	      ssn[nbss]=i;
	      ssl[nbss]=len;
	      has_ss[i][nbss]=true;
	      nbss++;
	    }
	  len++;
	}
    }
  return;
}


void parcours(int k)
{
  if(k==m)
    {
      int score=0;
      /*
      for(int i = 0; i < m; i++)
	printf("%d",serv[i]);
      printf("--\n");
      */
      bool empty[4];
      for(int i=0;i<n;i++)empty[i]=true;
      for(int i=0;i<m;i++)
	empty[serv[i]]=false;
      for(int i=0;i<n;i++)
	if(empty[i])
	  return;

      for(int se=0;se<n;se++)
	{
	  score++;//empty string
	  for(int ss=0;ss<nbss;ss++)
	    {
	      bool gotit=false;
	      for(int i=0;i<m;i++)
		if(serv[i]==se&&has_ss[i][ss])
		  gotit=true;
	      if(gotit)
		score++;
	      //printf("%d",gotit);
	    }
	  //printf("\n");
	}
      scores[score]++;		
    }
  else
    {
      for(int i = 0;i<n;i++)
	{
	  serv[k]=i;
	  parcours(k+1);
	}
    }
  return;
}

int main()
{
  int nb_cas;
  scanf("%d",&nb_cas);
  for(int cas = 1; cas <= nb_cas; cas++)
    {
      printf("Case #%d: ",cas);
      for(int i=0;i<8;i++)
	for(int j=0;j<80;j++)
	  has_ss[i][j]=false;
      for(int i=0;i<400;i++)
	scores[i]=0;
      scanf("%d%d",&m,&n);
      for(int i=0;i<m;i++)
	scanf("%s",t[i]);
      nbss=0;
      makess();
      parcours(0);
      int ma=399;
      while(scores[ma]==0)ma--;
      printf("%d %d\n",ma,scores[ma]);
      /*printf("nbss %d\n",nbss);
      for(int i = 0;i<nbss;i++)
	{
	for(int j=0;j<ssl[i];j++)
	  printf("%c",t[ssn[i]][j]);
	printf("\n");
	}
      for(int i = 0; i < m; i++)
	{
	  for(int j = 0; j < nbss; j++)
	    printf("%d",has_ss[i][j]);
	  printf("\n");
	}
      */
    }
  return 0;
}
