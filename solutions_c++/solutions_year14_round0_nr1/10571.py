#include<cstdio>

using namespace std;

void ins_row(int *row,int c){

  int access_s[]={1,5,9,13},access_e[]={4,8,12,16},discard,temp,temp2,i=1,in=0;

  temp =  access_s[c-1];
  temp2 = access_e[c-1];
     
  while(i<17){
    
      if(i==temp){
        scanf("%d",&row[in++]);
        if(temp<temp2)
	  temp++;
      }
      else
        scanf("%d",&discard);
      i++;
      
     }


}

int compare(int *r1,int *r2,int tc){

  int i=0,j,flag=0,res[4];
  for(i=0;i<4;i++){
    for(j=0;j<4;j++){
     if(r1[i]==r2[j]){
      res[flag++]=r1[i];
  }
  }
  }
    if(flag==1)
      printf("Case #%d: %d\n",tc,res[flag-1]);
    else if(flag>=2)
      printf("Case #%d: Bad magician!\n",tc) ;
    else if(flag==0)
      printf("Case #%d: Volunteer cheated!\n",tc);  
 }

int main(){

  int t,tc=1;
  
  scanf("%d",&t);
  while(t--){
  
    int c[2],row1[4],row2[4];
    scanf("%d",&c[0]);
    ins_row(row1,c[0]);
    scanf("%d",&c[1]);
    ins_row(row2,c[1]);
    /* 
     int x;
     for(x=0;x<4;x++)
      printf("%d ",row1[x]);    
     printf("\t\t");
     for(x=0;x<4;x++)
      printf("%d ",row2[x]);    
    
     printf("\n");
*/
      compare(row1,row2,tc++);
      
  }
  
  return 0;

}
