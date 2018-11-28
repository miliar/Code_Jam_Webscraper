#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
using namespace std;

unsigned int N;
ifstream inFile;
ofstream outFile;

class Quat{
private:
	int value;
public:
	const static int One = 1;
	const static int I   = 2;
	const static int J   = 3;
	const static int K   = 4;
	Quat(int v): value(v){}
	Quat():value(One){}
	Quat(char in){
		switch(in){
			case 'i':
			case 'I':
				value = I; break;
			case 'j':
			case 'J':
				value = J; break;
			case 'k':
			case 'K':
				value = K; break;
			default:
				value = One;
		}
	}
	Quat mult(Quat other){
		int sign = this->sign()*other.sign();
		int resV;
		int left  = abs(value);
		int right = abs(other.value);
		switch(left){
			case One:
				resV = right;
				break;
			case I:
                switch(right){
                    case One: resV =  I; break;
                    case   I: resV = -1; break;
                    case   J: resV =  K; break;
                    case   K: resV = -J; break;
                }
                break;
            case J:
                switch(right){
                    case One: resV =  J; break;
                    case   I: resV = -K; break;
                    case   J: resV = -1; break;
                    case   K: resV =  I; break;
                }
                break;
            case K:
                switch(right){
                    case One: resV =  K; break;
                    case   I: resV =  J; break;
                    case   J: resV = -I; break;
                    case   K: resV = -1; break;
                }
		}
		return Quat(resV*sign);
	}
	bool eq(Quat in){
		return value == in.value;
	}
	bool eq(int in){
		return value == in;
	}
	void negate(){
		value*= (-1);
	}
	int sign(){
		return (value<0)? -1 : 1;
	}
	string toString(){
		string out = string();
		if(sign()==-1) out += "-";
		switch(abs(value)){
			case One: out+="1"; break;
			case   I: out+="i"; break;
			case   J: out+="j"; break;
			case   K: out+="k"; break;
		}
		return out;
	}
};

bool searchIJK(Quat* search, int searchLen){
	//for(int i=0; i<searchLen; i++){
		//cout << search[i].toString() << " ";
	//}
	//cout << endl << endl;
	Quat iProd;
	for(int z=0; z<searchLen; z++){
		iProd = iProd.mult(search[z]);
		//cout << iProd.toString() << "\n";
		if(iProd.eq(Quat::I)){
			//search for j, find remaining k
			Quat jProd;
			for(int a=z+1; a<searchLen; a++){
				jProd = jProd.mult(search[a]);
				//cout << "  " << jProd.toString() << "\n";
				if(jProd.eq(Quat::J)){
					Quat kProd;
					for(int b=a+1; b<searchLen; b++){
						kProd = kProd.mult(search[b]);
					}
					//cout << "    " << kProd.toString() << "\n";
					if(kProd.eq(Quat::K)) return true;
				}
			}
		}
	}
	//cout << endl << endl;
	return false;
}

int main(int argc, char const *argv[]){
	if(argc != 2){
		cout<<"Error in Input"<<endl;
		return 0;
	}
	inFile.open(argv[1]);
	outFile.open("output.txt", ios::trunc | ios::out);
	if(!(inFile.is_open() && outFile.is_open()) ){
		cout << "can't open files"<<endl;
		return 0;
	}

	unsigned int T;
	inFile >> T;
	cout << "Running through " << T << " Iterations" << endl;
	for(int count=0; count<T; count++){
		unsigned long L, X;
		inFile >> L;
		inFile >> X;
		Quat str[L];
		for(int z=0; z<L; z++){
			char in;
			inFile >> in;
			Quat q = Quat(in);
			str[z] = q;
		}

		Quat q = str[0];
		for(int z=1; z<L; z++){
			q = q.mult(str[z]);
		}
		cout << q.toString() << endl;

		bool possible = false;
		if (q.eq(-1) && (X%2 == 1)) {
			possible = true;
		} else if (X%4 == 2) {
			possible = true;
		}
		bool found = false;
		if(possible){
			cout << "possible!";
			Quat* search;
			int searchLen;
/*			if(q.eq(-1)){
				//search = one instance of str
				searchLen = L;
				search = str;
			} else {
				//search = two instances of str
				searchLen = 2*L;
				search = new Quat[searchLen];
				for(int z=0; z<L; z++){
					search[z]   = str[z];
					search[z+L] = str[z];
				}
			}*/
			searchLen = X*L;
			search = new Quat[searchLen];
			for(int z=0; z<searchLen; z++){
				search[z] = str[z%L];
			}
			cout << "searching" << endl;
			found = searchIJK(search, searchLen);
		}

		cout << "Case #" << count+1 << ": ";
		cout << ((found)? "YES" : "NO");
		cout << std::endl;
		outFile << "Case #" << count+1 << ": ";
		outFile << ((found)? "YES" : "NO");
		outFile << std::endl;
	}
	cout << endl;

	inFile.close();
	outFile.close();
	return 0;
}
