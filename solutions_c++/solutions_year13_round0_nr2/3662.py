#include<stdio.h>

int main()
{
  int t,n,m,i,j,count=0,**arr,k;
  bool flag1=false,flag2=false,ans=true;
  
  FILE *fin=fopen("in.txt","r");
  FILE *fout=fopen("out.txt","w");
  
  fscanf(fin,"%d",&t);
  //scanf("%d",&t);
  
  while(t--)
  {
    fscanf(fin,"%d %d",&n,&m);
    //scanf("%d %d",&n,&m);
    ans=true;
    count++;
    
    arr=new int*[n+1];
    
    for(i=0;i<n;i++)
    {
      arr[i]=new int[m+1];
      for(j=0;j<m;j++)
	fscanf(fin,"%d",&arr[i][j]);
	//scanf("%d",&arr[i][j]);
      
    }
    
    for(i=0;i<n;i++)
    {
      for(j=0;j<m;j++)
      {	
	  //check row for 2
	  flag1=false;
	  flag2=false;
	  
	  for(k=0;k<n;k++)
	  {
	      if(arr[k][j]>arr[i][j])
	      {
		flag1=true;
		break;
	      }
	  }
	  
	  if(flag1==false)
	    continue;
	  
	  else
	  {
	    for(k=0;k<m;k++)
	      if(arr[i][k]>arr[i][j])
	      {
		flag2=true;
		break;
	      }
	  }
	  
	  if(flag1==true&&flag2==true)
	  {
	    fprintf(fout,"Case #%d: NO\n",count);
	    //printf("Case #%d: NO\n",count);
	    ans=false;
	    break;
	  }
      }
      
      if(ans==false)
	  break;
    }
    
      if(ans==true)
	fprintf(fout,"Case #%d: YES\n",count);
	//printf("Case #%d: YES\n",count);
  }
    
    return 0;
}