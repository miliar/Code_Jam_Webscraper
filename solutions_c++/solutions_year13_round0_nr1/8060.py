#include <iostream>
#include <fstream>
using namespace std;

void main(){
	ifstream file_in; ofstream file_out; int n, num, dot, rez; char ch;
	file_in.open("A-small-attempt0.in");
	file_out.open("out.txt");
	file_in >> n;
	char mas[4][4];

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++) {
				file_in >> mas[j][k];
			}
	
		
			
			for (int j = 0; j < 4; j++) {              // Первый шаг проверки
				num = 1;
				dot = 0;
				rez = 0;
				ch = mas[j][0];
				
				if (ch == '.') break;
				if (ch == 'T') ch = mas[j][1];
				for (int k = 1; k < 4; k++) {
					if (mas[j][k] == '.') {
						dot+=1;
						break;
					}
					if (mas[j][k] == 'T') {
						num+=1;
						continue;
					}
					if (mas[j][k] == ch)
						num+=1;
				}
				if (dot > 0) 
					continue;
				if (num == 4) {
					file_out << "Case #" << i << ": " << ch << " won" << endl;
					rez = 1;
					break;
				}
			}
			
			if (rez == 1) continue;

			for (int j = 0; j < 4; j++) {                     // Второй шаг проверки
				num = 1;
				dot = 0;
				ch = mas[0][j];
				if (ch == '.') break;
				if (ch == 'T') ch = mas[1][j];
				for (int k = 1; k < 4; k++) {
					if (mas[k][j] == '.') {
						dot+=1;
						break;
					}
					if (mas[k][j] == 'T') {
						num+=1;
						continue;
					}
					if (mas[k][j] == ch)
						num+=1;
				}
				if (dot > 0) 
					continue;
				if (num == 4) {
					file_out << "Case #" << i << ": " << ch << " won" << endl;
					rez = 1;
					break;
				}
			}

			if (rez == 1) continue;

			num = 1;
			ch = mas[0][0];
			if (ch != '.') {                                        // Третий этап проверки
				for (int j = 1, k = 1; j < 4; j++, k++) {                                
					if (mas[j][k] == '.') break;
					if (mas[j][k] == ch) {
						num+=1;
						continue;
					}
					if (mas[j][k] == 'T')
						num+=1;
				}
				if (num == 4) {
					file_out << "Case #" << i << ": " << ch << " won" << endl;
					rez = 1;
				}
			}

			if (rez == 1) continue;

			num = 1;
			ch = mas[0][3];
			if (ch != '.') {                                        // Четвёртый этап проверки
				for (int j = 2, k = 1; j >= 0; j--, k++) {                                
					if (mas[k][j] == '.') break;
					if (mas[k][j] == ch) {
						num+=1;
						continue;
					}
					if (mas[k][j] == 'T')
						num+=1;
				}
				if (num == 4) {
					file_out << "Case #" << i << ": " << ch << " won" << endl;
					rez = 1;
				}
				if (rez == 1) continue;
				
				num = 0;
				for (int s = 0; s < 4; s++)
					for (int t = 0; t < 4; t++) {
						if (mas[s][t] == '.') {
							num+=1;
						}
					}
				if (num != 0) {
					file_out << "Case #" << i << ": " << "Game has not completed" << endl;
					continue;
				} else {
					file_out << "Case #" << i << ": " << "Draw" << endl;
					continue;
				}


			} else {
				
				num = 0;
				for (int s = 0; s < 4; s++)
					for (int t = 0; t < 4; t++) {
						if (mas[s][t] == '.') {
							num+=1;
						}
					}
				if (num != 0) {
					file_out << "Case #" << i << ": " << "Game has not completed" << endl;
					continue;
				} else {
					file_out << "Case #" << i << ": " << "Draw" << endl;
					continue;
				}

			}
		
	}
	
	cin.get();
	cin.get();
}