#include<stdio.h>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
#include<memory.h>
using namespace std;

int calcWorstPlace(int teamId,int size,bool used[],int n)
{
	int teamIdFound=-1;
	if(size==0)
		return 0;
	for(int i=0;i<teamId;i++)
	{
		if(!used[i])
		{
			teamIdFound=i;
			used[i]=true;
			break;
		}
	}
	if(teamIdFound==-1)
	{
		return 0;
	}

	int curPlace=size/2;
	bool winnerFound=false;
	for(int i=teamId-1;i>=0;i--)
	{
		if(!used[i])
		{
			if(!winnerFound)
			{
				winnerFound=true;
				used[i]=true;
			}
			else {
				winnerFound=false;
			}
		}
	}
	return curPlace+calcWorstPlace(teamId,size/2,used,n);
}


int calcBestPlace(int teamId,int size,bool used[],int n)
{
	int teamIdFound=-1;
	if(size==0)
		return 0;
	for(int i=teamId+1;i<n;i++)
	{
		if(!used[i])
		{
			teamIdFound=i;
			used[i]=true;
			break;
		}
	}
	if(teamIdFound==-1)
	{
		return size-1;
	}
	int curPlace=0
		;
	bool looserFound=false;
	for(int i=teamId+1;i<n;i++)
	{
		if(!used[i])
		{
			if(!looserFound)
			{
				looserFound=true;
				used[i]=true;
			}
			else {
				looserFound=false;
			}
		}
	}
	return curPlace+calcBestPlace(teamId,size/2,used,n);
}
int main()
{
  int t;
  freopen("D:\\gcj\\B-small-attempt0.in","r",stdin);
  freopen("D:\\gcj\\output.txt","w",stdout);
  scanf("%d",&t);
  for(int tt=0;tt<t;tt++)
  {
	  int n,p;
	  scanf("%d %d",&n,&p);
	  int guaranteed=-1;
	  int possible =-1;
	  for(int i=0;i<(1<<n);i++)
	  {
		  bool used[1026];
		  memset(used,0,sizeof(used));
		  int best=calcBestPlace(i,(1<<n),used,(1<<n))+1;
		  if(best<=p && (possible==-1 || i>possible))
		  {
			  possible=i;
		  }
		  memset(used,0,sizeof(used));
		  int worst=calcWorstPlace(i,(1<<n),used,(1<<n))+1;
		  if((worst <= p ) && (guaranteed==-1 || i>guaranteed))
		  {
			  guaranteed=i;
		  }
	  }
	  printf("Case #%d: %d %d\n",tt,guaranteed,possible);
  }
}