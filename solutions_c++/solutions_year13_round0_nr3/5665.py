#include <cstdio>
#include <algorithm>
#include <math.h>
#define FOR(a,b,c) for(int i=a; i<b; i+=c)

using namespace std;

int ans=0,index=3;
int fairNum[100]={1,4,9};

void isItFair(int sqrt)
{
    int i = sqrt * sqrt,n,least,most;
    n = (int) floor(log10(i));
    if((n%2)==1)
    {
        if(n<2)
        {
            least=i%10;
            most=i/10;
            if(most==least)
            {
                //printf("cek %d %d\n",sqrt,i);
                fairNum[index]=i;
                index++;
            }
        }
    }
    else
    {
        if(n<3)
        {
            //printf("cek %d %d\n",sqrt,i);
            least=i%10;
            most=i/100;
            if(most==least)
            {
                //printf("cek %d %d\n",sqrt,i);
                fairNum[index]=i;
                index++;
            }
        }
    }
}

int main()
{
	int T,cas=1,n,least,most;
	int max, min, indexMax, indexMin;
	scanf("%d",&T);
	FOR(11,31,1)
	{
        n = (int) floor(log10(i));
        //printf("n =%d\n",n);
        if((n%2)==1)
        {
            if(n<2)
            {
                least=i%10;
                most=i/10;
                if(most==least) isItFair(i);
            }
        }
	}
	//FOR(0,index,1)printf("%d\n",fairNum[i]);
	while(T--)
	{
		indexMax=indexMin=-1;
		scanf("%d %d",&min,&max);
		FOR(0,index,1)
		{
            if(indexMin==-1&&fairNum[i]>=min)
                indexMin=i;
            if(fairNum[i]>max) 
            {
                indexMax=i;
                break;
            }
		}
		if(indexMax==-1)indexMax=index;
		if(indexMin!=-1)
            printf("Case #%d: %d\n",cas++,indexMax-indexMin);	
        else
            printf("Case #%d: 0\n",cas++);
	}
}
