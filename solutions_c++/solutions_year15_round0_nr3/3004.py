#include <iostream>
#include <vector>
using namespace std;

int calc[8][8] = { 
	{ 0, 1, 2, 3, 4, 5, 6, 7 },
	{ 1, 0, 5, 6, 7, 2, 3, 4 },
	{ 2, 5, 1, 4, 6, 0, 7, 3 },
	{ 3, 6, 7, 1, 2, 4, 0, 5 },
	{ 4, 7, 3, 5, 1, 6, 2, 0 },
	{ 5, 2, 0, 7, 3, 1, 4, 6 },
	{ 6, 3, 4, 0, 5, 7, 1, 2 },
	{ 7, 4, 6, 2, 0, 3, 5, 1 }
};

int main(int, char**){
	int t, x, size, n, i, j, k, ii, ij, ik, total, state;
	bool flag;
	string word;

	cin >> t;
	for(x = 1; x <= t; x++){
		cin >> size >> n; cin.ignore();
		cin >> word;
		short * w = new short[size];
		for(i = 0; i < size; i++)
			w[i] = word.at(i) - 'i' + 2;
		total = size * n;
		flag = false;
		if(word.compare("ijk") == 0)
			flag = true;
		else if(total > 3){
			state = i = j = k = ii = ij = ik = 0;
			while(!flag && ii < total - 2){
				switch(state){
					case 0:
						i = calc[i][ w[ii % size] ];
						ii ++;
						if(i == 2){
							j = 0;
							ij = ii;
							state = 1;
						}
					break;
					case 1:
						if(ij > total - 2)
							state = 0;
						else {
							j = calc[j][ w[ij % size] ];
							ij ++;
							if(j == 3){
								k = 0;
								ik = ij;
								state = 2;
							}
							if(j == 0)
								ii = ij;
						}
					break;
					case 2:
						if(ik == total)
							state = 1;
						else {
							k = calc[k][ w[ik % size] ];
							ik ++;
							if(k == 4 && ik == total)
								flag = true;
							if(k == 0)
								ij = ik;
						}
					break;
				}
			}
		}
		if(flag)
			cout << "Case #" << x << ": YES" << endl;
		else
			cout << "Case #" << x << ": NO" << endl;
	}
}