#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <math.h>

int isPalindrome(long long unsigned num);

int main()
{

// get the number of test cases
unsigned int testcase = 0;

static const char filename[] = "C-large-1.in";
//static const char filename[] = "C-small-attempt0.in";
//static const char filename[] = "A-large.in";
//A-large-practice.in
//static const char filename[] = "A-large-practice.in";

FILE *file = fopen ( filename, "rt" );

static const char filename1[] = "Out.txt";
FILE *file1 = fopen ( filename1, "wt" );

//static const char filename2[] = "In1.txt";
//FILE *file2 = fopen ( filename2, "wt" );

//static const char filename3[] = "In2.txt";
//FILE *file3 = fopen ( filename3, "wt" );


unsigned int counter =0;
printf("karthikeyan: file=%x\n", file);
// get the number of elements
unsigned int n=0;

char line[300];
char out[100];
unsigned int i=0 , j=0, max=0;

long long unsigned int count = 0, temp=0;
long long unsigned int low=0, high=0;
long long unsigned int ll=0, hh=0;
long double lld=0, hhd=0;
long long unsigned int v1[1000];
printf("size of long double=%d\n",sizeof(long double));
int result = 0;
//             scanf("%d", &j);             
             

if (file)
{
                  ll = 1;
                  hh = 100000000;         
				  // find all palindromes in this limit and store
                  for(count=ll; count<=hh; count++)
                  {
                       if(isPalindrome(count))
                       {
					       if(isPalindrome(count*count))
						   {
                               printf("karhtikeyan: found a palindrome!!!!!!! %llu\n", count);
						       v1[max] = count;
						       max++;
						   }
                       }					   
                  }
             // test case
             fgets(line, 10, file);
          	 sscanf (line, "%u", &testcase);
             printf("karthikeyan: size of testcase =%d\n", testcase);
             //scanf("%d", &j);             
             memset(line, '0', 10);
             
             for(counter=1; counter<=testcase; counter++)
             {
                  result = 0;
                  memset(line, '0', 300);                        
                  fgets(line, 300, file);
    	     	  sscanf(line,"%llu %llu",&low,&high);
                  //scanf("%d", &j);             
                  // find squareroot 
                  //ll = ceil(sqrtl(low));
				  //hh = floor(sqrtl(high));
   				  printf("karhtikeyan: low=%llu high=%llu\n",low,high);
                  lld = sqrtl((long double)low);
				  hhd = sqrtl((long double)high);
   				  printf("karhtikeyan: lld=%f hhd=%f\n",lld,hhd);
                  ll = ceill(lld); 
                  hh = floorl(hhd);
				  printf("karhtikeyan 1: ll=%llu hh=%llu\n",ll,hh);
				  //scanf("%d", &j);
                  for(i=0;i<max;i++)
                  {
                      if((v1[i]>=ll)&&(v1[i]<=hh))
                      {
                         result++; 
                      } 
                  }
                  printf("result=%d\n", result);
                  sprintf(out,"Case #%u: %d\n",counter,result);
                  fputs(out, file1);
               //scanf("%d", &j);
             
            } // for loop

}

fclose(file);
fclose(file1);
//fclose(file2);
//fclose(file3);

//scanf("%d", &j);

}


int isPalindrome(long long unsigned num)
{

char s[100] = {0};
int size = 0;
int count = 0;
int palindrome = 1;
sprintf(s,"%llu",num);
size = strlen(s);
//printf("size=%d num=%llu string=%s\n",size, num, s);
while(size > count)
{
   if(s[size-1] != s[count])
   {
      palindrome = 0;
      break;
   }
   size--;
   count++;
}

return palindrome;
}
