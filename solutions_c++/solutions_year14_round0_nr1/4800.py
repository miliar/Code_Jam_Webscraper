#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>

#define INPUT "A.in"
#define OUTPUT "A.out"


int main()
{

   int cases;
   int row,deck[2][4],vv[16];

   freopen(INPUT,"r",stdin);
   freopen(OUTPUT,"w", stdout);

   std::cin  >> cases;

   

   for(int i=0;i<cases;++i)
   {
	for(int z=0;z<16;++z)
		vv[z] = 0;

	for(int j=0;j<2;++j){
	
	std::cin >> row;

		for(int k=0;k<4;++k)
		{
		  for(int l=0;l<4;++l)
		  {
			int temp;
			std::cin >> temp;
			if(k == row-1)
			 deck[j][l] = temp;

		  }

		}
 
	}

	for(int j=0;j<2;++j)
	{
		
		for(int k=0;k<4;++k)
		{
		    vv[deck[j][k]-1]++;
		}

	}

	int two = 0;

	for(int o=0;o<16;++o)
	{
		
		if(vv[o]==2)
		 two++;

	}

	std::cout << "Case #" << i+1 << ": ";
	if(two==0)
		std::cout << "Volunteer cheated!";
	else if(two==1){
		for(int o=0;o<16;++o)
			if(vv[o]==2)
				std::cout << o+1;
	}
	else
		std::cout << "Bad magician!";

	std::cout << std::endl;

   }


   return 0;

}
