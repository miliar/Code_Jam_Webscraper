#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>

int main() {

char *input;
int max;
int sum=0,i=0,j=0,r=0,out=0,n;
char line[1010];  /* declare a char array */

    FILE *file,*opfile;  /* declare a FILE pointer  */
    file = fopen("C:\\Users\\Gourav\\Downloads\\A-large.in", "r");  /* open a text file for reading */
    opfile = fopen("C:\\Users\\Gourav\\Downloads\\A-large.txt", "w+");
    while(fgets(line, sizeof line, file)!=NULL)
    {
         if(j == 0)
         {
        //   t = atoi(strtok(line," "));
           j++;
           continue;
         }
         max = atoi(strtok(line," "));
         input = strtok(NULL," ");
        // printf("%d %s ",max,input);
         sum=0;
         out=0;
         n=max;
	for(i=0;i<=n;i++)
	{   	r=0;
			r=(input[i]-48);
      //   printf(" %d \n",r);
   		sum +=r;
   		if(sum >= n)
   		break;

   		if(sum < i+1)
   	{
    		r=((i+1)-sum);
    		out += r;
    		sum += r;
   	}
   }
   // printf("Case #%d: %d\n",j,out);
    fprintf(opfile,"Case #%d: %d\n",j,out);
    j++;
}
 fclose(file);
 fclose(opfile);
// getch();
 return 0;
}