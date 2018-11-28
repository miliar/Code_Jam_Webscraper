#include<iostream>
int main()
{
	int T;
	std::cin>>T;
	int n=T;
	while(T--)
	{
		int r1;
		std::cin>>r1;
		int d1[4][4];
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				std::cin>>d1[i][j];
		
		int r2;
		std::cin>>r2;
		int d2[4][4];
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				std::cin>>d2[i][j];
		
		int count=0;
		int x,y;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
			{
// 				std::cout<<d1[r1-1][i]<<' '<<d2[r2-1][j]<<' '<<i<<' '<<j<<std::endl;
				if(d1[r1-1][i]==d2[r2-1][j])
				{
					x=i;
					count++;
				}
			}
		if(count==1)
			std::cout<<"Case #"<<n-T<<": "<<d1[r1-1][x]<<std::endl;
		else if(count>1)
			std::cout<<"Case #"<<n-T<<": "<<"Bad magician!\n";
		else if(count==0)
			std::cout<<"Case #"<<n-T<<": "<<"Volunteer cheated!\n";
	}
}