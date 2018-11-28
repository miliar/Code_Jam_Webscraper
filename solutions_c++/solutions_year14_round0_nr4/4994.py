#include <iostream>
#include<algorithm>
using namespace std;

int main() {
	int T,N,i,KN,NN,j,P,Q,NN1=0,ct=0,m=1,n=0;
	double Naomi[10],Ken[10];
	cin>>T;
	while(T--)
	{
		++ct;
		cin>>N;
		for(i=0;i<N;i++)
			cin>>Naomi[i];
		for(i=0;i<N;i++)
			cin>>Ken[i];
		std::sort(Naomi,Naomi+N);
		std::sort(Ken,Ken+N);
		if(N==1)
		{
			if(Naomi[0]>Ken[0])
				printf("Case #%d: %d %d\n",ct,m,m);
				else
				printf("Case #%d: %d %d\n",ct,n,n);
		}
		else
		{
		for(i=0;i<N;i++)
		{
			NN1=0;
			P=N-i;
			Q=i;
			for(j=i;j<N;j++)
			{
				//printf("tt %lf %lf ll ",Naomi[j],Ken[j+i]);
				if(Naomi[j]>Ken[j-i])
				{
					NN1++;
					//Q++;
				}
				Q++;
			}
			//printf("NN=%d ",NN1);
			if(NN1==N-i)
				break;
		}
		KN=j=0;
		NN=0;
		for(i=0;i<N;i++)
		{
			while(j<N)
			{
				if(Ken[j]>Naomi[i])
				{
					//printf("%lf %lf\n",Naomi[i],Ken[j]);
					KN++;
					j++;
					break;
				}
				j++;
			}
			
		}
		printf("Case #%d: %d %d\n",ct,NN1,N-KN);
		}
	}
	return 0;
}