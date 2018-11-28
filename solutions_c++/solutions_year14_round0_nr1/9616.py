#include<iostream>
#include<string>

int main()
{
	int t = 0;
	std::cin >> t;
	
	for(int c = 1; c <= t; c++)
	{
		int row1;
		int nums1[4] = {0, 0, 0, 0};
		
		std::cin >> row1;
		
		for(int row=0; row < 4; row++)
		{
			for(int col=0; col < 4; col++)
			{	
				int n;
				std::cin >> n;
				
				if(row == row1 - 1)
				{
					nums1[col] = n;
				}
			}
		}
		
		
		int row2;
		int nums2[4] = {0, 0, 0, 0};
		
		std::cin >> row2;
		
		for(int row=0; row < 4; row++)
		{
			for(int col=0; col < 4; col++)
			{	
				int n;
				std::cin >> n;
				
				if(row == row2 - 1)
				{
					nums2[col] = n;
				}
			}
		}
		
		
		int count = 0;
		int v = 0;
		
		for(int i=0; i < 4; i++)
		{
			for(int j=0; j < 4; j++)
			{
				if(nums1[i] == nums2[j])
				{
					count++;
					v = nums1[i];
				}
			}
		}
		
		
		std::cout << "Case #" << c << ": ";
		
		if(count < 1)
			std::cout << "Volunteer cheated!";
		else if(count == 1)
			std::cout << v;
		else if(count > 1)
			std::cout << "Bad magician!";
		
		std::cout << std::endl;
	}
	
	return 0;
}