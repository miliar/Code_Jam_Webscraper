#include<iostream>
#include<algorithm>




using namespace std;




void main()
{

	int T=0;


	int A=0,B=0,K=0;
	int count=0;

	scanf("%d",&T);

	for(int i=1;i<=T;i++)
	{
		count=0;
		cin>>A>>B>>K;

		for(int ck=0;ck<A;ck++)
		{
			for(int ck1=0;ck1<B;ck1++)
			{
				if((ck&ck1)<K)
				{
					
					count++;
					///if(ck!=ck1)
						//count++;

				}
				
			}//innr for ck1

		}//ck

		cout<<"Case #"<<i<<": "<<count<<endl;

	}//T


	//system("pause");
}