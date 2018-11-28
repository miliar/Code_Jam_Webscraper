#include <iostream>
#include <cstdio>
using namespace std;



int main()
{
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int num;
	cin>>num;
	unsigned int N[num+1];
	
	for(int case_num = 1; case_num<=num;case_num++)
	cin>>N[case_num];
	
	
	for(int case_num = 1; case_num<=num;case_num++)
	{
		
		bool zero = true, one = true, two = true, three = true, four = true, five = true, six = true, seven = true, eight = true, nine = true;
		unsigned int temp = 0, i = 1;
		
		if(N==0)
		cout<<"Case #"<<case_num<<": INSOMNIA"<<endl;
		else
		{
			while((zero || one || two || three || four || five || six || seven || eight || nine) && i<10000000)
			{
				
				temp = i*N[case_num];
				unsigned long temp_length = temp;
				
				int exp = 1;
				
				while(temp_length)
				{
					temp_length/=10;
					exp*=10;
					
					int temp_digit = (temp % exp)/(exp/10);
					
					switch(temp_digit)
					{
						case 0: zero = false; break;
						case 1: one = false; break;
						case 2: two = false; break;
						case 3: three = false; break;
						case 4: four = false; break;
						case 5: five = false; break;
						case 6: six = false; break;
						case 7: seven = false; break;
						case 8: eight = false; break;
						case 9: nine = false; break;
					}
				}
				
				i++;
			}
			if(i<10000000)
			cout<<"Case #"<<case_num<<": "<<temp<<endl;
			else
			cout<<"Case #"<<case_num<<": INSOMNIA"<<endl;
		}
		
	}
	return 0;
}

