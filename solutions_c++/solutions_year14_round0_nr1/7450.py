#include<stdio.h>
#define SIZE 16
#define FACT 4
int main()
{
    int n,m,num,m1;
    int tc1;
    FILE *fp, *fp2;
    //fp = fopen("C-small-attempt0.in", "r");
    fp2 = fopen("ans3.txt", "w");
    scanf("%d",&tc1);
    int tc=1;
    printf("%d",tc1);
    while(tc<=tc1)
    {
                  //printf("%d",tc);
                  int a[FACT],f=0;
               scanf("%d",&m1);
               for(int i=0;i<16;i++)
               {
                       if(i==FACT*(m1-1))
                       {
                                        for(int j=0;j<4;j++)
                                        scanf("%d",&a[j]);
                                        i=i+3;
                       }
                       else
                       scanf("%d",&n);
               }
               scanf("%d",&m);

               for(int i=0;i<16;i++)
               {
                       if(i==FACT*(m-1))
                       {
                                        for(int j=0;j<4;j++)
                                       {
                                                 scanf("%d",&n);
                                                 if(a[0]==n||a[1]==n||a[2]==n||a[3]==n)
                                                 {
                                                           
                                                            if(f==0)
                                                            {f=1;
                                                            num=n;}
                                                            else
                                                            f=2;
                                                 }
                                                 
                                       }
                                              i=i+3;   
                       }
                       else
                       scanf("%d",&n);
               }
              if(f==2)
               {
                      fprintf(fp2,"Case #%d: Bad magician!\n",tc);
               }
               else if(f==1)
               {
                    fprintf(fp2,"Case #%d: %d\n",tc,num); 
                }
                else
                    fprintf(fp2,"Case #%d: Volunteer cheated!\n",tc);
               tc++;
               }
               printf("Over");
               return 0;
}
