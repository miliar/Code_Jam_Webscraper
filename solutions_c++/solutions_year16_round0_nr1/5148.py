#include <iostream>
#include <fstream>

using namespace std;

bool checkfinish(bool fa[]);
void extractDig(int n, bool fa[]);
void printArr(bool fa[]);
int process(int n);

int main(){
	ofstream myfile;
	myfile.open("output.txt");

	ifstream myReadFile;
	myReadFile.open("A-large.in");

	int t, n, m;

	//cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	int i = 1;

	while (!myReadFile.eof()) {

		myReadFile >> n;

		if (n == 0){
			myfile << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else{
			m = process(n);
			myfile << "Case #" << i << ": " << m << endl;
		}

		i++;	
	}


	system("pause");
}

int process(int n){
	bool fArray[] = { false, false, false, false, false, false, false, false, false, false };

	int c = 1;
	int m = -1;

	while (!checkfinish(fArray)){
		m = n * c;
		extractDig(m, fArray);
		c++;
	}

	return m;
}

bool checkfinish(bool fa[]){
	bool r = true;

	for (int i = 0; i < 10; i++){
		if (!fa[i]){
			r = false;
			break;
		}
	}

	return r;
}

void extractDig(int n, bool fa[]){
	if (n<10){
		fa[n] = true;
		return;
	}
	while (n >= 10){
		int d = n % 10;
		fa[d] = true;
		n = (n / 10);
	}
	if (n<10){
		fa[n] = true;
		return;
	}
}

void printArr(bool fa[]){
	cout << "array= ";
	for (int i = 0; i < 10; i++){
		cout << fa[i] << " ";
		
	}

	cout << "\n";
}