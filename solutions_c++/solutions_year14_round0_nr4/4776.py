#include<stdio.h>


int score(float arr1[],float arr2[],int nb)
{
 int i,j,score;
 i=j=score=0;
 for(i=0;i<nb;i++)
 {
  if(arr1[i] > arr2[j])
  {
   score++;
   j++;
  }
 }
 return score;
}

void sort(float array[],int n)
{
float swap;
for (int c = 0 ; c < ( n - 1 ); c++)
  {
    for (int d = 0 ; d < n - c - 1; d++)
    {
      if (array[d] > array[d+1])
      {
	swap       = array[d];
	array[d]   = array[d+1];
	array[d+1] = swap;
      }
    }
  }
}

void main()
{
 FILE *f1, *f2;
 f1 = fopen("C.in","r");
 f2 = fopen("Coutput.txt","w");
 int t,nb,y,z;
 float arr1[10],arr2[10];
 fscanf(f1,"%d",&t);
 for(int i=0;i<t;i++)
 {
  fscanf(f1,"%d",&nb);
  for(int j=0;j<nb;j++)
   fscanf(f1,"%f",&arr1[j]);
  for(j=0;j<nb;j++)
   fscanf(f1,"%f",&arr2[j]);
  sort(arr1,nb);
  sort(arr2,nb);

  y=score(arr1,arr2,nb);
  z=nb-score(arr2,arr1,nb);

  fprintf(f2,"Case #%d: %d %d\n",i+1,y,z);


 }
 fclose(f1);
 fclose(f2);
}