#include <iostream>

using namespace std;

int main()
{
	int numTestes;
	cin>>numTestes;
	
	int *cartas = new int[17];
	int id = 1;

	while(numTestes--)
	{

		for(int i = 0; i<18; i++)
			cartas[i] = 0;

		int resp1;
		cin>>resp1;

		int value = (resp1-1) * 4;

		for(int i =0; i<16; i++)
		{
			int carta;
			cin>>carta;

			if(i>=value && i<(value+4))
				cartas[carta] = 1;
		}
		
		int resp2;
		cin>>resp2;
	
		int value2 = (resp2-1) * 4;

		for(int i =0; i<16; i++)
		{
			int carta;
			cin>>carta;

			if(i>=value2 && i<(value2+4))
				cartas[carta]++;
		}


		int resp=0;
		int valid = 0;

		for(int i =1; i<18; i++)
		{
			if(cartas[i] ==2)
			{
				resp = i;
				valid++;
			}		
		}		

		if(valid == 1)
			cout<<"Case #"<<id++<<": "<<resp<<endl;
		else if(!valid)
			cout<<"Case #"<<id++<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<id++<<": Bad magician!"<<endl;
		
	}	

	return 0;
}

