#include<iostream>
#include<fstream>

using namespace std;

int main ()
{
	ifstream file ("A-large.in");
	
	int broj_pokusaja,i=0,j=0,suma,tocka,pobjeda;
	
	int matrica [4][4];
	char c;

	file >> broj_pokusaja;
	//cout << broj_pokusaja;

	for(int k = 0; k<broj_pokusaja;k++)
	{	
		if(k>0 && k<broj_pokusaja)
			cout <<endl;
		int pobjeda = 3; // 1 - x , 2 - o, 3 - draw, 4- not finished
		int tocka = 0;

		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				file >> c;

				if(c == '\n') continue;
				if(c=='X')
					matrica[i][j]=1;
				if(c=='O')
					matrica[i][j]=-1;
				if(c=='T')
					matrica[i][j]=10;
				if(c=='.')
					matrica[i][j]=0;
			}


	
		for(i=0;i<4;i++)
		{
			suma=0;
			for(j=0;j<4;j++)
			{
				suma+=matrica[i][j];
				if(matrica[i][j] == 0) tocka++;
			}

			if(suma == 13 || suma == 4)
			{
				pobjeda = 1;
				break;
			}

			if(suma == -4 || suma == 7)
			{
				pobjeda = 2;
				break;
			}

			if(tocka >0)
				pobjeda = 4;

		}

		for(j=0;j<4;j++)
		{
			if(pobjeda < 3) break;

			suma=0;
			
			for(i=0;i<4;i++)
			{
				suma+=matrica[i][j];
				if(matrica[i][j] == 0) tocka++;
			}

			if(suma == 13 || suma == 4)
			{
				pobjeda = 1;
				break;
			}

			if(suma == -4 || suma == 7)
			{
				pobjeda = 2;
				break;
			}

			if(tocka >0)
				pobjeda = 4;

		}

		suma = 0;
		tocka = 0;
		j=0;

		for(i = 0;i<4;i++)
		{
			if(pobjeda < 3) break;
			suma+=matrica[i][j];
			if(matrica[i][j++] == 0) tocka++;
		}
			
		if(suma == 13 || suma == 4)
			pobjeda = 1;

		else if(suma == -4 || suma == 7)
			pobjeda = 2;

		else if(tocka >0)
			pobjeda = 4;
		

		suma = 0;
		tocka = 0;
		j=3;
		for(i = 0;i<4;i++)
		{	
			if(pobjeda < 3) break;
			suma+=matrica[i][j];
			if(matrica[i][j--] == 0) tocka++;
		}
		
		if(suma == 13 || suma == 4)
			pobjeda = 1;
		
		else if(suma == -4 || suma == 7)
			pobjeda = 2;
			
		else if(tocka >0 && pobjeda >=3)
			pobjeda = 4;
	

		switch(pobjeda){
			case 1: cout << "Case #" << k+1 << ": X won"; continue;
			case 2: cout << "Case #" << k+1 << ": O won"; continue;
			case 3: cout << "Case #" << k+1 << ": Draw"; continue;
			case 4: cout << "Case #" << k+1 << ": Game has not completed"; continue;
		}

		
	}
}
