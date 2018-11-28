
//C++ program : To check whether a given number is palindrome or not
#include<stdio.h>
#include<math.h>
#include<memory.h>
#include<string.h>
int main()
{    
int A,B;
     long long int n,i,j,snum, si,num, rev=0,srev=0,digit,counter=0;
char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
fscanf(fp, "%lld", &n);
for(j=1;j<=n;j++)
{
counter=0;
fscanf(fp, "%d", &A);
fscanf(fp, "%d", &B);

for(i=ceilf(sqrt(A));i<=floorf(sqrt(B));i++)
{
	num=i;
     do
     {
	digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
 	if(i==rev)    
		{
		si=i*i;
		snum=si;
    			 do
    				 {
					digit = snum%10;
    				     srev = (srev*10) + digit;
    				     snum = snum/10;
   				  }while (snum!=0);
		if (si==srev) 
		counter=counter+1;
		}
rev=0;srev=0;
}
fprintf(ofp, "Case #%lld: %lld\n",j,counter);
}
return 0;
}
