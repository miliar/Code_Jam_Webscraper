//deceitful war

#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	 int t;
	 scanf("%d",&t);
	 double S[10000],S1[10000];double T[100000],T1[100000];
	 
	 int count=1;
	 while(t--)
	 {
			int a,i,j;
			scanf("%d",&a);
			
			for(i=0;i<a;i++)
		{	scanf("%lf",&S[i]);
	       	S1[i]=S[i];
	    }
			
			for(i=0;i<a;i++)
		{	scanf("%lf",&T[i]);
			T1[i]=T[i];
		}
			
			sort(S1,S1+a);
		   sort(T1,T1+a);
		   sort(S,S+a);
		   sort(T,T+a);
			int win=0,win1=0;
			
			for(i=0;i<a;i++)
			{
				for(j=0;j<a;j++)
				{
					if((S[i]<T[j])&&(S[i]!=-1)&&(T[j]!=-1))
					{
						//printf("%f  %f",S[])
						T[j]=-1;
						S[i]=-1;
						win++;
					}
					if((S1[i]>T1[j])&&(S1[i]!=-1)&&(T1[j]!=-1))
					{//printf("%f  %f\n",S1[i],T1[j]);
						win1++;
					  T1[j]=-1;
					  S1[i]=-1;
					}
				}
			}
			
			
		
			
			
			
			
	 printf("Case #%d: %d %d\n",count,win1,a-win);
			count++;

	}
	system("pause");
}

