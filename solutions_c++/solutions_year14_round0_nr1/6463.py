/*Magic Trick
    By Sonali Saxena
*/


#include <stdio.h>
#include<iostream>
#include<math.h>
int main()
{
   FILE *file_read,*file_write;file_read = fopen("input.in", "r");
   file_write = fopen("output.in", "w");
    int t,n,r1,r2,i,j,a[17],b[17],count1=0,ans=0;
   fscanf(file_read ,"%d",&t);
   n=t;
    while(!feof(file_read)&& t--)
    {

fscanf(file_read ,"%d",&r1);
    for(i=1;i<=16;i++)
        fscanf(file_read,"%d",&a[i]);
    fscanf(file_read ,"%d",&r2);
            for(i=1;i<=16;i++)
                fscanf(file_read,"%d",&b[i]);
            count1=0;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)                {
    if(a[i+4*r1-4]==b[j+4*r2-4])
        {
        count1++;
    ans=b[j+4*r2-4];
}                }
}            if(count1==0)
    fprintf(file_write,"Case #%d: Volunteer cheated! \n",n-t);            else if(count1>1)
fprintf(file_write,"Case #%d: Bad magician! \n",n-t);
    else
    fprintf(file_write,"Case #%d: %d \n",n-t,ans);}
fclose(file_read);  fclose(file_write);
   return 0;
}
