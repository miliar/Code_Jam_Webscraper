/*input
5
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
TWOSEVEN
ONETWOTHREEFOURFIVESIXSEVENEIGHTNINEZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINEZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINEZERO
*/

#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
	
	
	int test;
	cin>>test;
	int ctr = 1;
	while(test--)
	{
		cout<<"Case #"<<ctr++<<": " ;
		
		int arr[150] = {0};
		string s;
		cin>>s;
		// cout<<">>>"<<s<<"<<<\n";
		for (int i = 0; i < s.length(); ++i)
		{
			arr[s[i]]++;	
		}	
		int nums[11] = {0};
		//check zero
		while(arr['Z'])
		{
			if(arr['Z'])
			{
				if(arr['E'])
				{
					if(arr['R'])
					{
						if(arr['O'])
						{
							nums[0]++;
							arr['Z']--;
							arr['E']--;
							arr['R']--;
							arr['O']--;
								
						}
					}
				}
			}
		}
		while(arr['W'])
		{
			if(arr['T'])
			{
				if(arr['W'])
				{
					if(arr['O'])		
					{
						nums[2]++;
						arr['T']--;
						arr['W']--;
						arr['O']--;
							
					}
					
				}
			}

		}
		
		while(arr['U'])
		{
			if(arr['F'])
			{
				if(arr['O'])
				{
					if(arr['U'])
					{
						if(arr['R'])	
						{
								nums[4]++;
								arr['F']--;
								arr['O']--;
								arr['U']--;
								arr['R']--;
								
						}
					}
				}
			}
		}

		while(arr['X'])
		{
			if(arr['S'])
			{
				if(arr['I'])
				{
					if(arr['X'])						
					{
							nums[6]++;
							arr['S']--;
							arr['I']--;
							arr['X']--;
								
					}
				}
			}
		}

		while(arr['G'])
		{
			if(arr['E'])
			{
				if(arr['I'])
				{
					if(arr['G'])
					{
						if(arr['H'])
						{
							if(arr['T'])
							{
								nums[8]++;
								arr['E']--;
								arr['I']--;
								arr['G']--;
								arr['H']--;
								arr['T']--;	
							}
						}
					}
				}
			}
		}

		while(arr['O'])
		{
			if(arr['O'])
			{
				if(arr['N'])
				{
					if(arr['E'])
				
					{
						nums[1]++;
						arr['O']--;
						arr['N']--;
						arr['E']--;
						
							
					}
				}
			}
		}

		while(arr['H'])	
					
		{
			if(arr['T'])
			{
				if(arr['H'])
				{
					if(arr['R'])
					{
						if(arr['E'])
						{
							if(arr['E']>1)
							{
								nums[3]++;
								arr['T']--;
								arr['H']--;
								arr['R']--;
								arr['E']--;
								arr['E']--;	
							}
						}
					}
				}
			}

		}	
		

		while(arr['F'])
		{
			if(arr['F'])
			{
				if(arr['I'])
				{
					if(arr['V'])
					{
						if(arr['E'])
						{
							nums[5]++;
							arr['F']--;
							arr['I']--;
							arr['V']--;
							arr['E']--;	
						}
					}
				}
			}

		}
		

		while(arr['S'])
		{	
	
			


			if(arr['S'])
			{
				if(arr['E'])
				{
					if(arr['V'])
					{
						if(arr['E']>1)
						{
							if(arr['N'])	
							{
									nums[7]++;
									arr['S']--;
									arr['E']--;
									arr['V']--;
									arr['E']--;
									arr['N']--;
							}
						}
					}
				}
			}

		}

		while(arr['I'])
		{	

			if(arr['N'])
			{
				if(arr['I'])
				{
					if(arr['N']>1)
					{
						if(arr['E'])	
						{
								nums[9]++;
								arr['N']--;
								arr['I']--;
								arr['N']--;
								arr['E']--;
							
						}
					}
				}
			}
		}
		

		for (int i = 0; i < 10; ++i)
		{
			while(nums[i])
			{
				cout<<i;
				nums[i]--;
			}
		}
	cout<<endl;
	}

	return 0;
}