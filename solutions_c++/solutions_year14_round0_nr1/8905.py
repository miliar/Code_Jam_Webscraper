#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int qtd, a, b, aux, count, resp1;
	vector<int> resp;
	cin >> qtd;

	for(int k = 1; k <= qtd ; k++)
	{
		resp.clear();
		count = 0;

		cin >> a;

		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
			{
				cin >> aux;

				if(i == a-1)
					resp.push_back(aux);
			}

		cin >> b;

		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
			{
				cin >> aux;

				if(i == b-1)
					for(unsigned int x = 0; x < resp.size(); x++)
						if(resp[x] == aux)
						{
							resp1 = aux;
							count++;
						}
			}

		cout << "Case #" << k << ": ";

		if(count == 1)
			cout << resp1 << "\n";

		else if(count == 0)
			cout << "Volunteer cheated!\n";

		else
			cout << "Bad magician!\n";

	}

	return 0;
}