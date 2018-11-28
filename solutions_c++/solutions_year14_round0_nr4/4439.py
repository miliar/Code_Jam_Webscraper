#include<cstdio>
#include<iostream>
#include<vector>
#include <algorithm>
#include<deque>
   using namespace std;
  int main()
{
	double a[1200],b[1200];
	deque<double> A,B;
	int N,i,tn,t,score,j;
	scanf("%d",&tn);
	for(int k=1;k<=tn;k++)
	{
		scanf("%d",&N);
		for(i=0;i<N;i++)
		  scanf("%lf",&a[i]);
		for(i=0;i<N;i++)
		  scanf("%lf",&b[i]);
		sort(&a[0],&a[0]+N);
		sort(&b[0],&b[0]+N);
		for(i=0;i<N;i++)
		{A.push_back(a[i]);
		 B.push_back(b[i]);}
		score=0;
		while(!A.empty())
		{
			if(A.front()>B.front())
			{score++;
			 A.pop_front();
			 B.pop_front();}
			else
			{A.pop_front();
			 B.pop_back();}
		}
		printf("Case #%d: %d ",k,score);
                for(i=0,j=0,score=0;i<N;i++)
		{
	           while(j<N&&a[i]>b[j])
		    j++;
		   if(j!=N)
		   {j++;
		    score++;}
		   if(j==N)
			   break;
		}
		cout<<N-score<<endl;
	}
	return 0;
}
