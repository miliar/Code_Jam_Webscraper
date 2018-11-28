#include <conio.h>
#include <iostream>
using namespace std;

/*int secondsToConsumeHalf(int counter)
{
    int min=counter,splitCount,splitFirstHalf,splitSecondHalf,splitCost=0;
    if (counter > 3 )
    {
       //cout <<"\nTrying split combinations : "<<counter/2<<" AND "<<(counter-(counter/2));
       
       splitFirstHalf=secondsToConsume(counter/2);
       if (splitFirstHalf < (counter/2))
       {
          splitCost++; // splitCost
       }
       splitSecondHalf=secondsToConsume(counter-(counter/2));
       if (splitSecondHalf < (counter-(counter/2)))
       {
          splitCost++; // splitCost
       }
    //cout <<"\n FIRST HALF : "<<splitFirstHalf <<" SECOND HALF : "<<splitSecondHalf<<" SPLIT COST : "<<splitCost;
    splitCount=max(splitFirstHalf,splitSecondHalf) + splitCost + 1;
    min=min<splitCount?min:splitCount;
    //cout <<"\nWorking for : "<< counter<<">>>><<<< SplitCount : "<< splitCount <<">>>>><<<<<<< min : "<<min;
    return min;
    }
    else
        return counter;
}
*/
int timeToConsume(int diners,int pancakes[1000],int maxAttempt)
{
    int maxTime=pancakes[diners-1],timeConsumed,minTimeConsumed=maxTime,*splitPancakes;
    if (maxAttempt == 0)
       return maxTime;
    if (maxTime <= 2)
            return maxTime;
    for (int i=1; i <= maxTime/2;i++)
    {
        splitPancakes=new int[diners+1];
        memcpy(splitPancakes,pancakes,diners*sizeof(int));
        splitPancakes[diners]=i;
        splitPancakes[diners-1]-=i;
        sort(splitPancakes,splitPancakes+diners+1);
//        cout <<endl;
//        for (int j=0;j<diners+1; j++)
//            printf("%d,",splitPancakes[j]);
        timeConsumed=timeToConsume(diners+1,splitPancakes,maxAttempt-1)+1;
        minTimeConsumed=minTimeConsumed<timeConsumed?minTimeConsumed:timeConsumed;
    }
    return minTimeConsumed;
}

int main ()
{
    int cases,diners,pancake[1000],max,consumeCost[9],i;
    scanf("%d",&cases);
    for (int tCase=1; tCase<=cases;tCase++)
    {
        scanf ("%d",&diners);
        for (i=0;i<diners;i++)
        {
         scanf("%d",&pancake[i]);
         max= (max > pancake[i] ? max:pancake[i]);
        }
        sort(pancake,pancake+diners);
        cout <<"Case #"<<tCase<<": "<<timeToConsume(diners,pancake,pancake[diners-1])<<endl;
    }    
    return 0;
}
    
