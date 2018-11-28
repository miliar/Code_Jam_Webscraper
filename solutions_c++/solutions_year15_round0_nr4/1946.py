#include<stdio.h>
int main(){
    int t,x,r,c,z;
    scanf("%d",&t);
    for(z=1;z<=t;z++){
     printf("Case #%d: ",z);
     scanf("%d %d %d",&x,&r,&c);
     if(x<3){
      printf((r*c%x)?"RICHARD\n":"GABRIEL\n");
     }
    /* else if(x==3){
      if((r<3&&c<3)||(r<2||c<2)||(r*c%3))
       printf("RICHARD\n");
      else
      printf("GABRIEL\n");
     }
     else if(x==4){
      if((r<4&&c<4)||(r<3||c<3)||(r*c%4))
       printf("RICHARD\n");
      else
      printf("GABRIEL\n");
     }
     */
     else if(x<=4){
          if(((r%x==0)||(c%x==0))&&(r>=(x-1)&&c>=(x-1)))
           printf("GABRIEL\n");
          else
           printf("RICHARD\n");
     }
    }
    return 0;
}
