#include <cstdio>
#include <string>
#define fori(l,nnn) for(int l=1;l<=(nnn);l++)
using namespace std;


int main(int argc, char **argv) {
	int nada;
    int I,IT;
	int i,j;
	int r,t,p,CC,x;
	scanf("%d", &IT);  
    I=1;
    while(I<=IT){
       scanf("%d %d", &r, &t); 
       x=1;p=0;
       CC=0;
       do{
            p=p+2*r+x;
            x=x+4;
            CC++;
       }while(p<t);
       if(p==t) ;
       else CC--;
       
       printf("Case #%d: %d\n",I,CC);
       //printf("Case #%d: %d\n",I,2*I+1);
       I++;
    }
    
   
	return 0;
}

