#include<stdio.h>
#include<math.h>
int palindrom(int a);
int patrat(int a);
int palindrom(int a)
{
    int x,c=0,u;
    x=a;
    while (x!=0){
        u=x%10;
        c=c*10+u;
        x=x/10;
    }
    if (c==a) return 1;
    else return 0;
}


int patrat(int a)
{double x=sqrt(a);
    if (x==(int)(x)) return (int)(x);
    else return 0;
}

int verif(int a){
if ((patrat(a)!=0)&&(palindrom(a)==1)) if (palindrom(patrat(a))==1) return 1;
return 0;
    }
int main()
{
    FILE *f,*fo;
    f=fopen("input.txt","r");
    fo=fopen("output.txt","w");
    int n,a,b,i,nr,j;
    fscanf(f,"%d",&n);
    for(i=0;i<n;i++){
        fscanf(f,"%d",&a);
        fscanf(f,"%d",&b);
        nr=0;
        for (j=a;j<=b;j++){
            if (verif(j)==1) nr=nr+1;
        }
        fprintf(fo,"Case #%d: %d\n",i+1,nr);

    }


}
