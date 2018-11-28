#include <bits/stdc++.h>
using namespace std;

bool teste(int *dig){
	for(int i = 0; i < 10; i++)
		if(dig[i] == 0)
			return false;

	return true;
}

int main(){
	int casos;
	cin >> casos;
	for (int i = 0; i < casos; ++i)
	{
		int num, ori, cont = 0;
		cin >> num;
		ori = num;
		int dig[12] = {0};

		while(!teste(dig) && cont < 1000){
			int copy = num;
			while(copy){
				dig[ copy%10 ] = 1;
				copy /= 10;
			}
			num += ori;
			cont++;
		}

		if(cont < 1000)
			printf("Case #%d: %d\n", i + 1, num - ori);
		else
			printf("Case #%d: INSOMNIA\n", i + 1);
	}
}