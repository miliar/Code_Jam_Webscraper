#include<cstdio>
#include <algorithm>
using namespace std;

int card[4][4];
int arr1[4];

int main()
{
  int i,j,k,t,row,flag,kartu;
  scanf("%i\n",&t);
  for(k=1;k<=t;k++)
  {
  flag=0;     
  scanf("%i\n",&row);
  row=row-1;
  for(i=0;i<4;i++)
  {
        scanf("%i %i %i %i/n",&card[i][0],&card[i][1],&card[i][2],&card[i][3]);
        if(i==row)
        {
         arr1[0]=card[i][0];
         arr1[1]=card[i][1];
         arr1[2]=card[i][2];
         arr1[3]=card[i][3];   
        }
  }
  sort(arr1,arr1+4);
  scanf("%i\n",&row);
  for(i=0;i<4;i++)
  {
        scanf("%i %i %i %i/n",&card[i][0],&card[i][1],&card[i][2],&card[i][3]);
  }
  row=row-1;
  sort(card[row],card[row]+4);
  j=3;
  for(i=3;i>=0;i--)
  {
   if(flag<2)
   {
   while(j>=0)
   {
    if((arr1[i]==card[row][j]))
    {
        kartu=arr1[i];
        flag++;
        break;
    }
    else if(arr1[i]>card[row][j])break;
    j--;    
   }
   }     
  }  
  if(flag==1)printf("Case #%i: %i\n",k,kartu);
  else if(flag>1)printf("Case #%i: Bad magician!\n",k);
  else printf("Case #%i: Volunteer cheated!\n",k); 
  } 
}
