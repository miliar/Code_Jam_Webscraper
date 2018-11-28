//============================================================================
// Name        : CODEJAM_magicPeople.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

using namespace std;

int main() {
	fstream fin("A-small-attempt0.in");
	fstream fout("out.txt");

	int n, count;
	int tour1[4][4], tour2[4][4], ans1, ans2;
	bool magicWrong, manCheat, ok;
	fin >> n;

	for(int i = 0; i < n; i++){
		magicWrong = false;
		manCheat = true;
		count = 0;

		fin >> ans1;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fin >> tour1[j][k];
			}
		}
		fin >> ans2;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fin >> tour2[j][k];
			}
		}
		////////////
		/*fout << ans1 << endl;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fout << tour1[j][k] << " ";
			}
			fout << endl;
		}
		fout << ans2 << endl;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				fout << tour2[j][k] << " ";
			}
			fout << endl;
		}*/
		////////Врет ли человек
		ok = false;
		for(int z = 0; z < 4; z++){

			for(int j = 0; j < 4; j++){
				//fout << "AAA " << tour1[ans1-1][z] << " = " << tour2[ans2-1][j] << " BBB\n";
				if(tour1[ans1-1][z] == tour2[ans2-1][j]){
					manCheat = false;
					break;
				}
			}
		}


		if(manCheat){
			fout << "Case #" << i + 1 << ": Volunteer cheated!\n";
			continue;
		}
		//if(manCheat) break;
		////////Врет ли волшебник
		ok = false;
		for(int z = 0; z < 4; z++){

			for(int j = 0; j < 4; j++){
				if(tour1[ans1-1][z] == tour2[ans2-1][j]){
						count++;
				}
			}

			if(count > 1)
				magicWrong = true;

		}

		if(magicWrong){
				fout << "Case #" << i + 1 << ": Bad magician!\n";
				continue;
		}
        ////Никто не ошибся - ищем ответ
		ok = false;
		for(int z = 0; z < 4; z++){
			for(int k = 0; k < 4; k++){
				if(tour1[ans1-1][z] == tour2[ans2-1][k]){
					ok = true;
					fout << "Case #" << i + 1 << ": " << tour1[ans1-1][z] << "\n";
					break;
				}
			}
			if(ok)
				break;
		}

	}

    fin.close();
    fout.close();

	return 0;
}
