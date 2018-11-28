#include <cstdlib>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

void findintersect(int *var, int *temp, int m, int n, int t)
{
  int i=0,j=0,count=0,value;
  while(i<m&&j<n)
  {
    if(var[i]<temp[j])
      i++;
    else if(temp[j]<var[i])
      j++;
    else 
    {
        count++;
        value=var[i];
        i++;
        j++;
    }
  }
  if(count==1){
	printf("Case #%d: %d\n",t,value);
        
  } 
  else if(count==0){ printf("Case #%d: Volunteer cheated!\n",t);
  }
  else
  {
      printf("Case #%d: Bad magician!\n",t);
  }
}

int cmp(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}

void magic_game(int arr[4][4],int brr[4][4], int x,int y, int t){
    int var[4],temp[4],i;
    for(i=0;i<4;i++){
        var[i]=arr[x-1][i];
        temp[i]=brr[y-1][i];
    }
    qsort(var,4,sizeof(int),cmp);
    qsort(temp,4,sizeof(int),cmp);
    
    findintersect(var,temp,4,4,t);
}

int main(int argc, char** argv) {
   
    int arr[4][4];
    int brr[4][4];
    int t,x,y,i,j,k,p,q;
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d",&x);
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                scanf("%d",&arr[j][k]);
				}
            }
        scanf("%d",&y);
        for(p=0;p<4;p++){
            for(q=0;q<4;q++){
                scanf("%d",&brr[p][q]);
            }
        }
        magic_game(arr,brr,x,y,i+1);
    }
return 0;
}
