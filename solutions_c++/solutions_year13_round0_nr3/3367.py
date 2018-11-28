#include<stdio.h>
#include<math.h>
#include<string.h>

bool ispalin(int);

int main()
{
    int t;
    int a,b,count=0,i,sq,total=0,l,h;
    
    FILE* fin=fopen("C-small-attempt0.in","r");
    FILE* fout=fopen("out.txt","w");
    
    fscanf(fin,"%d",&t);
    
    while(t--)
    {
      total++;
      count=0;
      fscanf(fin,"%d %d",&a,&b);
      
      //printf("%d to %d\n",(int)sqrt(a),(int)sqrt(b)+1);
      
      l=(int)sqrt(a);
      h=(int)sqrt(b);
      
      if(l*l!=a)
	l++;
      
      //printf("l= %d and h= %d\n",l,h);
      
      for(i=l;i<=h;i++)
      {
	if(ispalin(i))
	{
	  sq=i*i;
	  count+=ispalin(sq);
	}
      }
      
      fprintf(fout,"Case #%d: %d\n",total,count);
    }
    
    return 0;
}

bool ispalin(int sq)
{
    char s[10],s1[10];
    int k=0,i;
    
    while(sq!=0)
    {
	s[k++]=sq%10;
	sq/=10;
    }
    
    s[k]='\0';
    
    for(i=0;i<k;i++)
    {
      if(s[i]!=s[k-i-1])
	return false;
    }
    
    return true;
}