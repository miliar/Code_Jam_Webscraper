#include <iostream>
#include <vector>

using namespace std;

int main() {
	int m[4][4];
	int v[16];
	int n,l;
	int c = 1;
	vector<int> card;
	
	cin >> n;
	while (n--)
	{
		
		for(int i = 0; i < 16; i++)
			v[i] = 0;
			
		for(int k = 0; k < 2; k++)
		{
			cin >> l;
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; j++)
					cin >> m[i][j];
			for(int i = 0; i < 4; i++)
			{
				v[m[l-1][i]-1] += 1;
			}
		}
		
		for(int i = 0; i < 16; i++)
		{
			/*cout << "i = " << i << endl;
			cout << "v[i] = " << v[i] << endl;*/
			if(v[i] == 2)
				card.push_back(i+1);
		}
		if (card.size() == 1)
			cout << "Case #" << c <<": " << card[0] << endl;
		else if (card.size() > 1)
			cout << "Case #" << c <<": Bad magician!" << endl;
		else
			cout << "Case #" << c <<": Volunteer cheated!" << endl;
		c++;
		card.clear();

			
	}
	
	return 0;
}