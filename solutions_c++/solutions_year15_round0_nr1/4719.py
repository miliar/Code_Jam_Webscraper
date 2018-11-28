#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::string;



class Audience{
	public:
	//ctor
	Audience(int _Smax, string single_digits);
	//cctor
	Audience(const Audience&);
	vector<unsigned char> getNPWithS(){return nPWithS;};
	int getSmax() { return Smax; };

	int additionalNeeded();

	private:
	int Smax;
	vector<unsigned char> nPWithS;
};

Audience::Audience( int _Smax, string single_digits):Smax(_Smax),nPWithS(_Smax+1){
	for (int i=0;i<=Smax;i++){
		nPWithS[i]=single_digits[i]-'0';
	}
}

int Audience::additionalNeeded (){
	int sum = 0;
	int additionalNeededVal = 0;
	for (int S=0;S<=Smax;S++){
		if (sum < S){
			additionalNeededVal+= S-sum;
			sum = S;
		}
		sum+=nPWithS[S];
	}
	return additionalNeededVal;
}

int main(){
	int N;
	cin>>N;
	for (int i=0;i<N;i++){
		int Smax;
		cin>>Smax;
		string single_digits;
		cin >> single_digits;
		Audience A(Smax,single_digits);
		cout<< "Case #" << i+1 <<": " << A.additionalNeeded() << endl;
	}
}
