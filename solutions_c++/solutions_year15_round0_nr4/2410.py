#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){

	int T,X,R,C,count,total,j,k;
	bool **arr;

	ofstream fout("Small Output2.txt");
	//ifstream fin("Input.txt");
	ifstream fin("small2.in");
	
	fin >> T;

	for (int i = 0; i < T; i++){
		fin >> X;
		fin >> R;
		fin >> C;

		if (R == 1 && C == 1){
			if (X==1)
				fout << "Case #" << i + 1 << ": GABRIEL" << endl;
			else
				fout << "Case #" << i + 1 << ": RICHARD" << endl;
		}
		else{
			int temp = X / 2;
			temp = X - temp;
			if (((R >= temp && C >= temp + 1) || (R >= temp + 1 && C >= temp)) && ((R*C) % X == 0) && (R >= X || C >= X)){

				if (X == 4){
					if (R*C < 12)
						fout << "Case #" << i + 1 << ": RICHARD" << endl;
					else
						fout << "Case #" << i + 1 << ": GABRIEL" << endl;
				}
				else
					fout << "Case #" << i + 1 << ": GABRIEL" << endl;
			}
			else
				fout << "Case #" << i + 1 << ": RICHARD" << endl;

		}
		//cout << X << "  " << R << "  " << C << endl << endl;
		
	}
	system("pause");
	return 0;
}