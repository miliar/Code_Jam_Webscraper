#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector <int> tablica[101];
int ilosc[2501];

void Sortowanie( vector<int> tab[], int size, int k)
{
	int j;
	vector <int> temp;

	for( int i = 1; i < size; i++ )
	{
		temp = tablica[ i ];

		for( j = i - 1; j >= 0 && tablica[ j ][ k ] > temp[ k ]; j-- )
			tab[ j + 1 ] = tab[ j ];

		tablica[ j + 1 ] = temp;
	}
}

int main(){
	
	int z;
	cin >> z;
	
	for(int p = 1; p <= z; p++){
		int N;
		cin >> N;
		
		for(int i = 0; i <= 2500; i++)
			ilosc[i] = 0;
		for(int i = 0; i < 2 * N - 1; i++){
			for(int j = 1; j <= N; j++){
				int a;
				cin >> a;
				tablica[i].push_back(a);
				ilosc[a]++;
			}
		}
		
		vector <int> wynik;
		
		for(int i = 1; i<= 2500; i++)
		{
			if(ilosc[i] % 2 == 1)
				wynik.push_back(i);
		}
		sort(wynik.begin(), wynik.end());
		
		cout << "Case #" << p << ": ";
		
		for(int i = 0; i < (int)wynik.size(); i++){
			cout << wynik[i] << " ";
		}
		cout << endl;
	}
	
	return 0;
}
