#include <fstream>
#include<math.h>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
int T, IND;
long long L,X;

class Quaternion
{
	int i, j ,k ,c;

public :
	Quaternion(int i = 0, int j = 0 , int k = 0, int c = 0)
	{
		this->i = i;
		this->j = j;
		this->k = k;
		this->c = c;
	}
	Quaternion operator*(Quaternion & obj)
	{
		int c =  this->c * obj.c - this->k * obj.k - this->j * obj.j - this->i * obj.i;
		int k  = this->c * obj.k + this->i * obj.j - this->j * obj.i + this->k* obj.c;
		int i =  this->c * obj.i + this->i * obj.c + this->j * obj.k - this->k * obj.j;
		int j =  this->c * obj.j + this->j*obj.c - this->i * obj.k +this->k * obj.i;

		return Quaternion(i,j,k,c);
	}

	bool operator==(Quaternion & obj)
	{
		if(this->c == obj.c && this->i == obj.i && this->j == obj.j && this->k == obj.k)
			return true;
		return false;
	}
};

Quaternion I(1,0,0,0);
Quaternion J(0,1,0,0);
Quaternion K(0,0,1,0);
Quaternion C(0,0,0,1);

Quaternion period[5];

Quaternion arr[10001];

void solve () {

	if(!(period[X%4] == Quaternion(0,0,0,-1))) {
		fout<<"Case #"<<IND<<": NO"<<"\n";
		return;
	}
	Quaternion aux  ;
	long long left_length = 0;
	bool stop = false;
	for(int i = 0; i <= 4 && stop == false; i++)
		for(int j = 1; j <= L; j++ ) {
			if(j ==1) {
				aux = arr[1];
			} else { 
				aux = aux * arr[j];
			}
			if(period[i] * aux == Quaternion(1,0,0,0)) {
				left_length = L * i + j;
				stop = true;
				break;
				
			}
		}
    if(stop == false) {
		fout<<"Case #"<<IND<<": NO"<<"\n";
		return;
	}
    stop = false;
	long long right_length = 0;
	for(int i = 0; i <= 4 && stop == false; i++)
		for(int j = L; j >= 1; j-- ) {
			if(j == L) {
				aux = arr[L];
			} else { 
				aux = arr[j] * aux;
			}
			if(aux * period[i]  == Quaternion(0,0,1,0)) {
				right_length = L * i + L-j + 1;
				stop = true;
				break;
				
			}
		}

	if(stop == false) {
		fout<<"Case #"<<IND<<": NO"<<"\n";
		return;
	}

	if(right_length + left_length < L * X) {
		fout<<"Case #"<<IND<<": YES"<<"\n";
	} else {
		fout<<"Case #"<<IND<<": NO"<<"\n";
	}


}

int main()
{
	fin>>T;
	char c;
	Quaternion aux;
	period[0] = Quaternion(0,0,0,1);
	for( IND = 1; IND <= T; IND++) {
		fin>>L>>X;
		for(int i =1; i<=L; i++) {
			fin>>c;
			switch(c) 
			{
			case'i':  aux = Quaternion(1,0,0,0);
				break;
			case 'j': aux = Quaternion(0,1,0,0);
				break;
			case 'k': aux = Quaternion(0,0,1,0);
				break;
			}

			if( i == 1) {
				period[1] = aux;
			} else {
				period[1] = period[1] * aux;
			}
			arr[i] = aux;
		}

		period[2] = period[1] * period[1];
		period[3] = period[2] * period[1];
		period[4] = period[3] * period[1];
		solve();

	}
	return 0;
}