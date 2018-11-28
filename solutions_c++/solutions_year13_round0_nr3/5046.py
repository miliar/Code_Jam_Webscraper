#include<stdio.h>
#include<math.h>
int A,B;
bool isPalindrome(int x)
{	
  if (x < 0) return false;
  
  int div = 1;
  while (x / div >= 10) {
    div *= 10;
  }        
  while (x != 0) {
    int l = x / div;
    int r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}
bool isSquare(int x,int *root)
{
	int y=(int) pow(x,0.5);
	if(y*y==x)
	{
		*root=y;
		return 1;
	}
	else return 0;
}
int num_of_fair_and_square()
{
	int i,count=0;int root;
	for(i=A;i<=B;i++)
	{
		if(isSquare(i,&root))
		{
			if(isPalindrome(i) && isPalindrome(root))
				count++;
		}
	}
	return count;
}
int main()
{
	FILE *fin=fopen("C-small-attempt0.in","r");
	FILE *fout=fopen("C-small-attempt0.out","w");
	int T,t;
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf(fin,"%d",&A);
		fscanf(fin,"%d",&B);
		fprintf(fout,"Case #%d: %d\n",t,num_of_fair_and_square());
	}
	return 0;
}
