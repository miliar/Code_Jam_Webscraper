#include<cstdio>
int main(){
int i,turn,a,b,c;
scanf("%d",&turn);
for(i=1;i<=turn;i++){
scanf("%d %d %d",&a,&b,&c);
printf("Case #%d: ",i);
if((b*c)%a){
printf("RICHARD\n");
}else{
if(a<=2){
printf("GABRIEL\n");
}else if(a==3){
if(b*c==3) printf("RICHARD\n");
else printf("GABRIEL\n");
}else{
if(b*c==4) printf("RICHARD\n");
if(b*c==8) printf("RICHARD\n");
if(b*c==12) printf("GABRIEL\n");
if(b*c==16) printf("GABRIEL\n");
}
}
}
}

