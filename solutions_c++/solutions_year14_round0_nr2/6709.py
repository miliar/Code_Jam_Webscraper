/*MAGICAN
#include<iostream>

int main()
{
	std::ios_base::sync_with_stdio(false);

	unsigned int localRow;
	unsigned int localTests;
	unsigned int localAcctualNumber;

	unsigned int localResult;

	std::cin>>localTests;

	unsigned int localTab[16+1];

	for(unsigned int i=0;i<localTests;++i)
	{
		memset(localTab,0,sizeof(localTab));
		

		for(unsigned int z=0;z<2;++z)
		{
			std::cin>>localRow;

			--localRow;

			for(unsigned int x=0;x<4;++x)
			{
				for(unsigned int y=0;y<4;++y)
				{
					std::cin>>localAcctualNumber;

					if(x==localRow)
						++localTab[localAcctualNumber];
				}
			}
		}



		localResult=0;

		for(unsigned int x=1;x<17;++x)
		{
			if(localTab[x]>1)
			{
				if(localResult==0)
					localResult=x;
				else
				{
					localResult=999;
					break;
				}
			}
		}

		std::cout<<"Case #"<<i+1<<": ";

		if(localResult&&localResult!=999)
			std::cout<<localResult;
		else if(localResult==999)
			std::cout<<"Bad magician!";
		else
			std::cout<<"Volunteer cheated!";

		std::cout<<std::endl;
	}

	return 0;
}
*/

#include<iostream>

int main()
{
	std::ios_base::sync_with_stdio(false);

	unsigned int localTests;
	double localC,localF,localX;

	double localResult;
	double localVariant1,localVariant2;
	double localAcctualProduting;

	std::cin>>localTests;

	for(unsigned int i=0;i<localTests;++i)
	{
		localResult=0.0;
		localAcctualProduting=2.0;

		std::cin>>localC;
		std::cin>>localF;
		std::cin>>localX;

		while(true)
		{

			localVariant1=localX/localAcctualProduting;
			localVariant2=localC/localAcctualProduting+(localX/(localAcctualProduting+localF));
	
			if(localVariant1<localVariant2)
			{
				localResult+=localVariant1;
				break;
			}
			else
			{
				localResult+=localC/localAcctualProduting;

				localAcctualProduting+=localF;
			}
		}

		printf("Case #%d: %.7f\n",i+1,localResult);
		//std::cout<<"Case #"<<i+1<<": "<<localResult<<std::endl;
	}

	return 0;
}