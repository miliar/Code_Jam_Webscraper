#include<stdio.h>
#include<string.h>
char mult(char a,char b,int *sign){
 char ans;
 if(a=='1')
  return b;
 else if(b=='1') 
  return a;
 switch(a){
  case 'i': 
       if(b=='i'){
        ans='1';
        *sign=*sign * -1;
       }
       else if(b=='j')
        ans='k';
       else{
        ans='j';
        *sign=*sign * -1;
       }
       break;
   case 'j': 
       if(b=='j'){
        ans='1';
        *sign=*sign * -1;
       }
       else if(b=='k')
        ans='i';
       else{
        ans='k';
        *sign=*sign * -1;
       } 
       break;
   case 'k': 
       if(b=='k'){
        ans='1';
        *sign=*sign * -1;
       }
       else if(b=='i')
        ans='j';
       else{
        ans='i';
        *sign=*sign * -1;
       }
   }  
   return ans; 
}      
char s[10009],s2[10002];
int main(){
    int t,l,i,x,z,sign=-1;
    char target,tmp;
   // printf("%c",mult('k','i',&sign));
    //printf(" %d\n",sign);
    scanf("%d",&t);
    for(z=1;z<=t;z++){
     scanf("%d %d",&l,&x);
     scanf("%s",s);
     strcpy(s2,s);
     while(--x)
      strcat(s,s2);
     target='i';
     sign=1;
     //printf("%s\n",s);
     for(i=0,tmp='1';s[i];i++){
      tmp=mult(tmp,s[i],&sign);
      //printf("i=%d, tmp= %c, sign=%d\n",i,tmp,sign);
      if(tmp==target&&sign==1){
       tmp='1';
       if(target=='i'){
        target='j'; 
       // printf("i found at index %d\n",i);
       }
       else if(target=='j'){
        target='k';
        //printf("j found at index %d\n",i);
       }
       else if(target=='k'){
        target='1';
        //printf("k found at index %d\n",i);
       }
       else{
        target='1';
        //printf("1 found at index %d\n",i);
       }
       continue;
      } 
     }
     if(tmp==target&&target=='1'&&sign==1)
      printf("Case #%d: YES\n",z); 
     else
      printf("Case #%d: NO\n",z); 
    }
    return 0;
}
      
      
      
     
    
