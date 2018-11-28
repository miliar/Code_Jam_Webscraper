#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string pripad(int h, int w, int** radky);

int main() {
	ifstream myReadFile;
	myReadFile.open("input.in");
	ofstream myWriteFile;
	myWriteFile.open("output.out");
	string output;
	if (myReadFile.is_open()) {
		myReadFile >> output;
		int pocet_pripadu = atoi(output.c_str());
		//pocet_pripadu = 4;
		cout << pocet_pripadu<<"\n";
		for (int i = 1;i<=pocet_pripadu;i++) {
			myReadFile >> output;
			int h = atoi(output.c_str());
			myReadFile >> output;
			int w = atoi(output.c_str());
			int** radky;
			radky = new int*[h];
			for (int j = 0;j<h;j++) {
				int* radek;
				radek = new int[w];
				for (int l = 0;l<w;l++) {
					myReadFile >> output;
					radek[l] = atoi(output.c_str());
				}
				radky[j] = radek;
			}
			string reseni = pripad(h, w, radky);
			cout<<"Case #"<<i<<": "<<reseni<<"\n";
			myWriteFile<<"Case #"<<i<<": "<<reseni<<"\n";
		}
	}
	myReadFile.close();
	myWriteFile.close();
	cin>>output;
	return 0;
}

string pripad(int h, int w, int** radky) {
	string navrat = "YES";
	int posekatelnych = 0;
	bool** ok;
	ok = new bool*[h];
	for (int j = 0;j<h;j++) {
		ok[j] = new bool[w];
		for (int i = 0;i<w;i++) {
			ok[j][i]=false;
		}
	}
	// proverovani jednotlivych radku
	for (int j = 0;j<h;j++) {
		int r_max=radky[j][0];
		for (int i = 0;i<w;i++) {
			if (radky[j][i]>r_max) {
				r_max = radky[j][i];
			}
		}
		for (int i = 0;i<w;i++) {
			if (radky[j][i]==r_max) {
				ok[j][i] = true;
				posekatelnych++;
			}
		}
	}
	// proverovani jednotlivych sloupcu
	for (int j = 0;j<w;j++) {
		int r_max=radky[0][j];
		for (int i = 0;i<h;i++) {
			if (radky[i][j]>r_max) {
				r_max = radky[i][j];
			}
		}
		for (int i = 0;i<h;i++) {
			if (radky[i][j]==r_max) {
				if (!ok[i][j]) {
					posekatelnych++;
				}
				ok[i][j] = true;
			}
		}
	}
	// navrat
	if (posekatelnych<w*h) {
		navrat = "NO";
	} else {
		navrat = "YES";
	}
	return navrat;
}