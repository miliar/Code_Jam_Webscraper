#include <iostream>
#include <cstdio>
#include <string>
using namespace std;


int main(void)
{
	int runs;
	scanf("%d", &runs);
	for(int it = 1; it <= runs; it++) {
		char rows[4], cols[4], d[2];

		char temp, arr[4][4];
		for(int i = 0; i<4; i++) {
			for(int j = 0; j<4; j++) {
				cin >> temp;
				arr[i][j] = temp;
			}
		}

		// solve
		for(int i = 0; i<4; i++) {
			cols[i] = arr[0][i];
			rows[i] = arr[i][0]; 
		}
		d[0] = arr[0][0]; 
		d[1] = arr[0][3];

		int completed = 1;
		for(int i = 0; i<4; i++) {
			for(int j = 0; j<4; j++) {
				if(arr[i][j] == 'T')
					continue;

				if(arr[i][j] == '.') {
					completed = 0;
					
					rows[i] = 'Z';
					cols[j] = 'Z';
					if(i == j) d[0] = 'Z';
					if(3-i == j) d[1] = 'Z';

					continue;
				}

				if(rows[i] != 'Z' && arr[i][j] != rows[i]) {
					rows[i] = 'Z';
				}
				if(cols[j] != 'Z' && arr[i][j] != cols[j]) {
					cols[j] = 'Z';
				}
				if(d[0] != 'Z' && i==j && arr[i][j] != d[0])
					d[0] = 'Z';
				if(d[1] != 'Z' && 3-i == j && arr[i][j] != d[1])
					d[1] = 'Z';
			}
		}

		// for(int i = 0; i<4; i++)
		// 	cout << rows[i] << "  " << cols[i] << endl;

		int flag = 0;
		for(int i = 0; i<4; i++) {
			if(rows[i] != 'Z' && rows[i]!='.') {
				flag = 1;
				temp = rows[i];
				break;
			}
			if(cols[i] != 'Z' && cols[i]!='.') {
				flag = 1;
				temp = cols[i];
				break;
			}
		}

		if(!flag) {
			if(d[0] != 'Z' && d[0]!='.') {
				flag = 1;
				temp = d[0];
			}
			if(!flag && d[1] != 'Z' && d[1]!='.') {
				flag = 1;
				temp = d[1];
			}
		}

		if(flag) {
			printf("Case #%d: %c won\n", it, temp);
		}
		else if(completed && !flag) {
			printf("Case #%d: Draw\n", it);
		}
		else if(!completed && !flag) {
			printf("Case #%d: Game has not completed\n", it);
		}



	} /* end while*/
	return 0;
}
