#include <iostream>
# include <string.h>
#include <stdio.h>
using namespace std;

int main()
{

    FILE *f;
    if((f=fopen("lol.txt","r"))==NULL)
    {
        printf("er.\n");
//        exit(1);
    }

    FILE *fp;

    fp=fopen("lolo.txt","w+");
int T=0;
    char ch;
while((ch=fgetc(f))!='\n')
     {if(ch>='0'&&ch<='9')
               T=T*10+ch-'0';

     }
     int N=0,M=0;
     int i=0,j=0;
while((ch=fgetc(f))!='\n')
     {

         if(ch>='0'&& ch<='9' && i==0)
               N=N*10+ch-'0';
               else if(ch==' ')
               i++;
               else if(i==1)
               M=M*10+ch-'0';

     }
int **x;
int a=0;
/*
x=new int*[N];
for(i=0;i<N;i++)
x[i]=new int[M];
for(i=0;i<N;i++)
{
for(j=0;j<M;j++)
{
    x[i][j]=0;
}

}
i=0;
j=0;
*/
int p=0, lol=0,lolo=0, sum=0,sum1=0,sumM=0,sumL=0,kl=0,index=0,q=0,u=0;
int count=0;
int *d,*d1;

//while((ch=fgetc(f))!=EOF)
for(int k=0;k<T;k++)
{
    x=new int*[N];
for(i=0;i<N;i++)
x[i]=new int[M];

d=new int[N];
d1=new int[M];
for(i=0;i<N;i++)
for(j=0;j<M;j++)
    {x[i][j]=0;
    d1[j]=0;
    d[i]=0;
    }
i=0;
j=0;
while(kl!=N)
     {
         ch=fgetc(f);
         if(ch>='0' && ch<='9')
               a=a*10+ch-'0';
         if(ch==' ' || ch=='\n')
         {
             x[i][j]=a;
             a=0;
             j++;
         }
         if(j==M)
         {
             i++;
             j=0;
             kl++;
         }
         if(kl==N)
        {
            if(M>1 && N>1)
            {
            i=0;
            j=0;
            q=0;
            u=0;
            while(q<N)
            {
                for(u=0;u<M;u++)
            if((x[i][u]>x[i][j] && x[q][j]>x[i][j]) || (x[i][M-1-u]>x[i][M-1] && x[q][M-1]>x[i][M-1]) || (x[N-1-q][j]>x[N-1][j] && x[N-1][u]>x[N-1][j]) || (x[N-1][M-1-u]>x[N-1][M-1] && x[N-1-q][M-1]>x[N-1][M-1]))
            {
                index++;
            }
            q++;
            }




            j=0;
            q=0;
            u=0;


            while(q<N)
            {
                for(u=0;u<M;u++)
            for(i=1;i<N-1;i++)
            {
                if((x[q][j]>x[i][j] && x[i][u]>x[i][j]) || (x[i][u]>x[i][j] && x[N-q-1][j]>x[i][j]))
                    index++;
            }
            q++;
            }


            q=0;
            u=0;
            j=M-1;


 while(q<N)
            {
                for(u=0;u<M;u++)
            for(i=1;i<N-1;i++)
            {
            if((x[q][j]>x[i][j] && x[i][u]>x[i][j]) || (x[i][u]>x[i][j] && x[N-q-1][j]>x[i][j]))
                    index++;
            }
            q++;
            }



            q=0;
            u=0;
            i=0;



             while(q<N)
            {
                for(u=0;u<M;u++)
            for(j=1;j<M-1;j++)
            {
                if((x[i][u]>x[i][j] && x[q][j]>x[i][j]) || (x[q][j]>x[i][j]&& x[i][M-u-1]>x[i][j]))
                index++;
            }
            q++;
            }



            q=0;
            u=0;
            i=N-1;



            while(q<N)
            {
                for(u=0;u<M;u++)
            for(j=1;j<M-1;j++)
            {
                if((x[i][M-1-u]>x[i][j] && x[N-1-q][j]>x[i][j]) || (x[N-1-q][j]>x[i][j]&& x[i][u]>x[i][j]))
                index++;
            }
            q++;
            }



            q=0;
            u=0;



             while(q<N)
            {
                for(u=0;u<M;u++)
             for(i=1;i<N-1;i++)
            for(j=1;j<M-1;j++)
            {
                if((x[N-1-q][j]>x[i][j] && x[i][u]>x[i][j]) || (x[i][u]>x[i][j] && x[q][j]>x[i][j]) || (x[q][j]>x[i][j] && x[i][M-1-u]>x[i][j]) || (x[i][M-1-u]>x[i][j] && x[N-1-q][j]>x[i][j]))
                   index++;
            }
            q++;
            }
           /* if(index==0)
{
fprintf(fp,"Case #%d: YES\n",count+1);
}
count++;
index=0;*/
            }
            /*
else if(M==1 || N==1)
{
    fprintf(fp,"Case #%d: NO\n",count+1);
    count++;
}*/
            q=0;
            u=0;

if(index==0 || M==1 || N==1)
{
fprintf(fp,"Case #%d: YES\n",count+1);
}
//cout<<"case"<<count<<"YES";
else {fprintf(fp,"Case #%d: NO\n",count+1);}
//cout<<"case"<<count<<"NO";
sumM=0;sumL=0;
count++;
index=0;
        }

     }
    // while(kl!=N);
   //  while((ch=fgetc(f))!=EOF);
     for(int i=0;i<N;i++)
       {
          delete x[i];
       }
       delete x;
       delete d;
       delete d1;
     i=0;
j=0;
N=0;
M=0;
kl=0;
//cout<<ch<<"loooooooool";
//ch=fgetc(f);
//cout<<ch<<"loooooooool";
    while((ch=fgetc(f))!='\n')
     {

         if(ch>='0'&& ch<='9' && i==0)
               N=N*10+ch-'0';
               else if(ch==' ')
               i++;
               else if(i==1)
               M=M*10+ch-'0';

     }
}
cout<<"lol";
    fclose(f);
fclose(fp);

//or(i=0;i<6;i++)
   // printf("%s",c[i]);
//printf("%s",c[0]);

    return 0;
}
