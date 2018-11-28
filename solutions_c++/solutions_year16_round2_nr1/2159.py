#include<fstream>
#include<string>

using namespace std;

int main() {
	int n;
	ifstream is;
	is.open("A-large.in");
	ofstream os;
	os.open("outA.txt");
	is>>n;
	for(int i=0; i<n; i++) {
		string tel;
		is>>tel;
		int a[25], b[10];
		for(int j=0;j<10;j++){
			b[j]=0;
		}
		
		for(int j=0;j<25;j++){
			a[j]=0;
		}
		
		for(int j=0;j<tel.size();j++){
			a[(int)(tel[j] - 'A')]++;
			if(tel[j] == 'Z') {
				a[(int)('Z' - 'A')]--;
				a[(int)('E' - 'A')]--;
				a[(int)('R' - 'A')]--;
				a[(int)('O' - 'A')]--;
				b[0]++;
			}
			if(tel[j] == 'W') {
				a[(int)('T' - 'A')]--;
				a[(int)('W' - 'A')]--;
				a[(int)('O' - 'A')]--;
				b[2]++;
			}
			if(tel[j] == 'U') {
				a[(int)('F' - 'A')]--;
				a[(int)('O' - 'A')]--;
				a[(int)('U' - 'A')]--;
				a[(int)('R' - 'A')]--;
				b[4]++;
			}
			if(tel[j] == 'X') {
				a[(int)('S' - 'A')]--;
				a[(int)('I' - 'A')]--;
				a[(int)('X' - 'A')]--;
				b[6]++;
			}
			if(tel[j] == 'G') {
				a[(int)('E' - 'A')]--;
				a[(int)('I' - 'A')]--;
				a[(int)('G' - 'A')]--;
				a[(int)('H' - 'A')]--;
				a[(int)('T' - 'A')]--;
				b[8]++;
			}
		}
		b[7] = a[(int)('S' - 'A')];
		a[(int)('N' - 'A')] -= b[7];
		a[(int)('V' - 'A')] -= b[7];
		b[5] = a[(int)('V' - 'A')];
		b[1] = a[(int)('O' - 'A')];
		a[(int)('N' - 'A')] -= b[1];
		b[9] = a[(int)('N' - 'A')]/2;
		b[3] = a[(int)('T' - 'A')];
		os<<"Case #"<<i+1<<": ";
		for(int j=0;j<10;j++){
			for(int k= 0; k<b[j]; k++) os<<j;
		}
		os<<endl;
	}
	return 0;
}



