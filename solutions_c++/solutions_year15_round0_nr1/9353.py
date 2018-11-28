#include<stdio.h>
#include<string.h>

using namespace std;

int main(){

 freopen("A-large.in","r",stdin);
 freopen("3.out","w",stdout);

 int sum=0;
 int roundnumber=0;
 int caseno=1;
 int testcases;
 int ans;
 char str[1500];
 scanf("%d",&testcases);
 while(testcases--){
     sum = 0;
     ans = 0;
     scanf("%d",&roundnumber);
     scanf("%s",str);
     int size = strlen(str);
     for(int i=0;i<size;i++){
     
     int iPeoples = str[i]-'0';
     if(i==0){
       sum = sum + iPeoples; 
     }else{
       if(sum >= i){ sum = sum + iPeoples;  }
       else{ ans = ans+1; sum = sum+1+iPeoples;  }
      } 
     
     }
  
 printf("Case #%d: %d\n",caseno,ans);
 caseno++;
    
  
 } 
 return 0;

}



