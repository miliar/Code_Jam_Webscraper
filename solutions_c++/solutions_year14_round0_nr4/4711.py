#include<iostream> 
#include<conio.h> 
using namespace std;
float wtNaomi[1000],wtKen[1000];
int stoneCount,i;
int getSmallerElements(float wtChosen, int winCounter,float wtArray[])
{
       int greater=0;
       for (i=0;i<stoneCount;i++)
       {
           if ( wtArray[i] < wtChosen )
              //{printf("Found greater for check of %f and %f while winCounter was %d\n",wtChosen,wtArray[i],winCounter);
              greater++;
       }
       //printf("-----Greater found to be %d, while counter was %d -----",greater,winCounter);
       if (greater >= (winCounter+1))
          return 1;
       else
           return 0;
}
int main ()
{
    int i,j,winWarKen=0,winDWarNaomi=0;
    char newline;
    float tmp;
    int counter=0;
    int testCases,tCase;
    scanf("%d",&testCases);
    for (tCase=1;tCase<=testCases;tCase++)
    {
     winWarKen=0;
     winDWarNaomi=0;
     scanf("%d",&stoneCount);
     counter=0;
     do
     {
        scanf( "%f%c", &wtNaomi[counter++], &newline );
     } while( counter < stoneCount);
     for (i = 0; i < stoneCount; ++i)
     {
         for (j = i + 1; j < stoneCount; ++j)
         {
            if (wtNaomi[i] > wtNaomi[j])
            {
                tmp = wtNaomi[i];
                wtNaomi[i] = wtNaomi[j];
                wtNaomi[j] = tmp;
            }
         }
     }
     counter=0;
     do
     {
        scanf( "%f%c", &wtKen[counter++], &newline );
        //printf( "\n%d element for Ken is %f",counter,wtKen[counter-1]);
     } while( counter < stoneCount);
     for (i = 0; i < stoneCount; ++i)
     {
        for (j = i + 1; j < stoneCount; ++j)
        {
            if (wtKen[i] > wtKen[j])
            {
                tmp = wtKen[i];
                wtKen[i] = wtKen[j];
                wtKen[j] = tmp;
            }
        }
     }
     for (i=0;i<stoneCount;i++)
     {
          //printf("Element for Naomi: %f\tElement for Ken: %f\n",wtNaomi[i], wtKen[i]);
          winDWarNaomi+=getSmallerElements(wtNaomi[i],winDWarNaomi,wtKen);
          winWarKen+=getSmallerElements(wtKen[i],winWarKen,wtNaomi);    
     }
    printf("Case #%d: %d %d\n",tCase,winDWarNaomi,(stoneCount-winWarKen));
    }
    //getch();
    return(0);
}
