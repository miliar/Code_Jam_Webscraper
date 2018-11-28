#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int dW(vector<float>, vector<float>);
int w(vector<float>, vector<float>);
vector<float> insertionSort(int num, vector<float> arreglo);

int main()
{

	ifstream abre("D-large.in");
	ofstream output("output.txt");
	int numCase;

	abre >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		vector<float>bloque1;
		vector<float>bloque2;
		int n;
		
		abre >> n;

		for (int j = 0; j < n; j++)
		{
			float temp;
			abre >> temp;
			bloque1.push_back(temp);
		}

		for (int j = 0; j < n; j++)
		{
			float temp;
			abre >> temp;
			bloque2.push_back(temp);
		}

		vector<float> temp1 = insertionSort(n, bloque1);
		vector<float> temp2 = insertionSort(n, bloque2);



		output << "Case #" << (i + 1) << ": " << dW(temp1, temp2) << " " << w(temp1, temp2) << endl;

	}

	output.close();
	system("pause");
	return 0;
}

int dW(vector<float> b1, vector<float> b2)
{

	int res1 = 0;

	for (int i = 0; i < b2.size(); i++)
	{
		for (int j = 0; j < b1.size(); j++)
		{
			if (b2[i] < b1[j])
			{
				res1++;
				b1.erase(b1.begin() + j);
				break;
			}
		}
	}

	return res1;
}

int w(vector<float> b1, vector<float> b2)
{

	int res2 = 0;

	for (int i = 0; i < b1.size(); i++)
	{
		for (int j = 0; j < b2.size(); j++)
		{
			//cout << b2[j] << " " << endl;
			//cout << b1[i] << " " << endl;
			if (b1[i] < b2[j])
			{

				res2++;
				b2.erase(b2.begin() + j);
				break;
			}
		}
	}

	res2 = b1.size() - res2;

	return res2;
}

vector<float> insertionSort(int num, vector<float> arreglo)
{


	int j;
	float index;
	for (int i = 1; i < num; i++)
	{
		index = arreglo[i];
		j = i - 1;
		while (j >= 0 && arreglo[j] > index)
		{
			arreglo[j + 1] = arreglo[j];
			j--;
		}
		arreglo[j + 1] = index;
	}

	return arreglo;
}