#include <iostream>

using namespace std;

int main(void)
{
	int t;

	//Lendo a quantidade de casos de teste
	cin >> t;
	int arr1[4][4],arr2[4][4];
	int answer1, answer2;
	int cards,choosed;

	//Lendo e calculando cada caso de teste
	for(int qtd=1 ; (qtd<=t) ; qtd++)
	{
		cards=0;

		cin >> answer1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> arr1[i][j];

		cin >> answer2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> arr2[i][j];

		for(int i1=0;i1<4;i1++)
			for(int i2=0;i2<4;i2++)
				if(arr1[answer1-1][i1] == arr2[answer2-1][i2])
				{
					cards++;
					choosed=arr1[answer1-1][i1];
					continue;
				}

		if(cards==1)
			cout << "Case #" << qtd << ": " << choosed << endl;
		else if(cards>1)
			cout << "Case #" << qtd << ": Bad magician!" << endl;
		else
			cout << "Case #" << qtd << ": Volunteer cheated!" << endl;

	}
	return 0;
}
