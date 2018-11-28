#include<algorithm>
#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int t,mote;
int n,arr[1000001],k=1;;
scanf("%d",&t);
while(t--)
{
  scanf("%d%d",&mote,&n);
  for(int i=0;i<n;i++)
  {
	scanf("%d",&arr[i]);
  }
  sort(arr,arr+n);
  int prescnt=0,ans=n,flag=0;
  for(int i=0;i<n;i++)
  {
	if(mote>arr[i])
        {mote+=arr[i];flag=0;
	continue;
	}
	else
  	{
	flag=1;
	ans=min(ans,prescnt+n-i);
	int cnt=0;
	while(mote<=arr[i])
	{	
		mote=mote+mote-1;
		cnt++;
		if(cnt>ans) break;
	}
	if(ans<cnt)
	break;
	else {prescnt+=cnt;
	mote+=arr[i];
//	ans=min(ans,prescnt+n-i);
	}
	}
	
  }
  if(flag==0)
  printf("Case #%d: %d\n",k++,prescnt);
 else
  printf("Case #%d: %d\n",k++,ans);
}
}
