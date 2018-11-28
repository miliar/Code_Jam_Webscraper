#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>


int main(int argc, char *argv[])
{
FILE* fichier1 = NULL;
fichier1 = fopen("B-small-attempt2.in", "r+");

FILE* fichier2 = NULL;
fichier2 = fopen("B-small-attempt2.out", "w+");


int test=0;
int m=0;
int n=0;
int c=0;
int i=0;
int j=0 ,r=0;
int  **t;
int **t2;
int f=0;



       fscanf(fichier1,"%d",&test);


       fgetc(fichier1);




       for( r=0;r<test;r++)
       {


         c=0;
       fscanf(fichier1,"%d",&m);

       fgetc(fichier1);

       fscanf(fichier1,"%d",&n);


        fgetc(fichier1);

        t=(int**) malloc (sizeof(int*)*m);
        for (i=0; i<m; i++)
        t[i]=(int*) malloc (sizeof(int)*n);



        t2=(int**) malloc (sizeof(int*)*m);
        for (i=0; i<m; i++)
        t2[i]=(int*) malloc (sizeof(int)*n);





        if(m==1 || n==1)
        {
            for( i=0; i<m;i++)
               {
                       for(j=0; j<n;j++)
                       {

                            fscanf(fichier1,"%d",&t[i][j]);
                                fgetc(fichier1);

                                           }



             }
            c=0;
        }
        else
        {


               for( i=0; i<m;i++)
               {
                       for(j=0; j<n;j++)
                       {

                            fscanf(fichier1,"%d",&t[i][j]);
                                fgetc(fichier1);

                                           }



             }






            for( i=0; i<m;i++)
               {
                       for(j=0; j<n;j++)
                       {

                            t2[i][j]=2;

                                           }



             }


           for(j=0; j<n;j++)
           {

                f=0;
                for(i=0;i<m-1;i++)
                {

                    if(t[i][j]!=t[i+1][j])
                    {
                         f=1;
                         break;
                    }


                }

                if(f==0)
                    {
                for(i=0;i<m;i++)
                {
                    t2[i][j]=t[0][j];
                }
                    }
           }


            f=0;
           for(i=0; i<m;i++)
           {

                f=0;
                for(j=0;j<n-1;j++)
                {

                    if(t[i][j]!=t[i][j+1])
                       {
                         f=1;
                            break;
                    }

                }

                if(f==0)
                {

                for(j=0;j<n;j++)
                {
                    t2[i][j]=t[i][0];
                }
                }

           }


            for( i=0; i<m;i++)
               {
                       for(j=0; j<n;j++)
                       {

                            if(t[i][j]!=t2[i][j])
                            {
                                c=1;
                                break;
                                break;
                            }

                                           }



             }





        }



               if(c==1)
               {
                         fprintf(fichier2,"Case #%d: NO\n",r+1);
                         }

               else
               {
                         fprintf(fichier2,"Case #%d: YES\n",r+1);
                         }







         }


return 0;
}
