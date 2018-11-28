#include<stdio.h>
#include<string.h>
#include<math.h>


int isFair(long int num) {
		long reversed = 0, n = num;
		while (n > 0) {
			reversed = reversed * 10 + n % 10;
			n /= 10;
		}
		return num == reversed;
}
int isSquareOfFair( int num) {
		 int sqrt1 = ( int) sqrt((double)num);
		if(sqrt1*sqrt1 != num) return false;
		return isFair(sqrt1);
}



	 long int getValue(long int A, long int B) {
		long int c = 0;
		for(long int i = A; i<= B; ++i) {
			if(isFair(i) && isSquareOfFair(i)) c++;
		}
		return c;
	}
int main()
{
    int i,t,n,j,result;
    FILE *fp;
    fp = fopen("c:\\b.in", "r");
    fscanf(fp," %d",&t);
    
    for(j=1;j<=t;j++)
    {         
        long int a,b;
		fscanf(fp," %ld",&a);
		fscanf(fp," %ld",&b);
              
        printf("Case #%d: %d\n",j,getValue(a,b));
             
    }
   
	 fclose(fp);
}