#include<cstdio>
int main(){
    int i,turn,a,b,c;
    scanf("%d",&turn);
    for(i=1;i<=turn;i++){
        scanf("%d %d %d",&a,&b,&c);
        printf("Case #%d: ",i);
        if(b*c<a || (b*c)%a!=0){printf("RICHARD\n");}
		else if(a==4)
{
if((b>3 && c>2) || (c>3 && b>2))printf("GABRIEL\n");
else printf("RICHARD\n");
}
else if(a==3)
{
if((b>2 && c>1) || (c>2 && b>1))printf("GABRIEL\n");
else printf("RICHARD\n");
}
else if(a==2)
{
if((b>1 || c>1) )printf("GABRIEL\n");
else printf("RICHARD\n");
}
else
printf("GABRIEL\n");
    }
}