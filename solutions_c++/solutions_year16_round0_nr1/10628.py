#include<iostream>

#include<cstdio>



using namespace std;



int main()

{

	int n;

	long long int m;

	

	
	scanf("%d",&n);
//	while(scanf("%d",&n)==1)

	//{

		for(int i=0;i<n;i++)

		{

			scanf("%lld",&m);

			if(m==0)

			{

				printf("Case #%d: INSOMNIA\n",i+1);//break;
				continue;
			}

			

			int u=1;

			int mark=0;

			int r[10]={0};

//			if(m/10==0)

//			{

//				r[m]++;

//			}

			while(1)

			{

				int y=m;

				y=y*u;

				//m=y;

				

				if(mark==1)

				{

					break;

				}

				

				if(y/10==0)

			{

				r[y]++;

			}

				

				while(y/10>0)

				{

					r[y%10]++;

					y=y/10;

					

					if(y/10==0)

					{

						r[y]++;	

					}

					

					int c=0;

					for(int t=0;t<=9;t++)

					{

						if(r[t]!=0)

						{

							c++;

						}

					}

				

					if(c==10)

					{

						printf("Case #%d: %lld\n",i+1,m*(u));mark=1;

						break;

					}

				

					else

					{

						c=0;

					} 

					

					 

				}u++;	

			}

		}

//	}

}

 
