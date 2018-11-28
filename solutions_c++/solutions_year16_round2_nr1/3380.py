#include <iostream>
#include <cstring>
using namespace std;
int t,i,n,c;
int main()
{	
	ios::sync_with_stdio(0);
	cin>>t;
	c = 1;
	while(t)
	{
		int a[26] = {0};
		string s;
		cin>>s;
		n = s.length();
		for (i = 0; i < n; ++i)
			a[s[i]-65]++;		
		int number[11] = {0};
		while(a[25])
		{
			if(a[25])
			{
				if(a[4])
				{
					if(a[17])
					{
						if(a[14])
						{
							number[0]++;
							--a[25];
							--a[4];
							--a[17];
							--a[14];
								
						}
					}
				}
			}
		}
		while(a[22])
		{
			if(a[19])
			{
				if(a[22])
				{
					if(a[14])		
					{
						number[2]++;
						--a[22];
						--a[19];
						--a[14];
							
					}
					
				}
			}

		}
		
		while(a[20])
		{
			if(a[5])
			{
				if(a[14])
				{
					if(a[20])
					{
						if(a[17])	
						{
								number[4]++;
								--a[5];
								--a[14];
								--a[20];
								--a[17];
								
						}
					}
				}
			}
		}

		while(a[23])
		{
			if(a[18])
			{
				if(a[8])
				{
					if(a[23])						
					{
							number[6]++;
							--a[18];
							--a[8];
							--a[23];
								
					}
				}
			}
		}

		while(a[6])
		{
			if(a[4])
			{
				if(a[8])
				{
					if(a[6])
					{
						if(a[7])
						{
							if(a[19])
							{
								number[8]++;
								--a[4];
								--a[8];
								--a[6];
								--a[7];
								--a[19];	
							}
						}
					}
				}
			}
		}

		while(a[14])
		{
			if(a[14])
			{
				if(a[13])
				{
					if(a[4])
				
					{
						number[1]++;
						--a[14];
						--a[13];
						--a[4];							
					}
				}
			}
		}

		while(a[7])						
		{
			if(a[19])
			{
				if(a[7])
				{
					if(a[17])
					{
						if(a[4])
						{
							if(a[4]>1)
							{
								number[3]++;
								--a[19];
								--a[7];
								--a[17];
								--a[4];
								--a[4];	
							}
						}
					}
				}
			}

		}	
		

		while(a[5])
		{
			if(a[5])
			{
				if(a[8])
				{
					if(a[21])
					{
						if(a[4])
						{
							number[5]++;
							--a[5];
							--a[8];
							--a[21];
							--a[4];	
						}
					}
				}
			}

		}
		

		while(a[18])
		{	
			if(a[18])
			{
				if(a[4])
				{
					if(a[21])
					{
						if(a[4]>1)
						{
							if(a[13])	
							{
									number[7]++;
									--a[18];
									--a[4];
									--a[21];
									--a[4];
									--a[13];
							}
						}
					}
				}
			}

		}

		while(a[8])
		{	

			if(a[13])
			{
				if(a[8])
				{
					if(a[13]>1)
					{
						if(a[4])	
						{
								number[9]++;
								--a[13];
								--a[8];
								--a[13];
								--a[4];
							
						}
					}
				}
			}
		}
		
		cout<<"Case #"<<c<<": " ;
		++c;
		for (i = 0; i < 10; ++i)
		{
			while(number[i])
			{
				cout<<i;
				--number[i];
			}
		}
	cout<<endl;
	--t;
	}

	return 0;
}