#include<iostream>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;

class largeNumber {
    private:
	//little endian
	string num;

    public:
	largeNumber(string n = "0"); 

	largeNumber(const largeNumber & rhs) {
	    num = rhs.num;
	}

	largeNumber & operator = (const largeNumber & rhs) {
	    num = rhs.num;
	    return *this;
	}

	largeNumber operator + (const largeNumber & rhs) const;
	largeNumber operator * (const largeNumber & rhs) const;
	bool operator == (const largeNumber & rhs);
	bool operator < (const largeNumber & rhs);
	bool operator <= (const largeNumber & rhs);

	char & operator [] (int i) {
	    return num[i];
	}

	char operator [] (int i) const {
	    return num[i];
	}
	int size() const {
	    return num.size();
	}
};

largeNumber::largeNumber(string n) {
    num = "";
    for(int i=n.size()-1; i>=0; i--)
	num.append(1,n[i]);
}

largeNumber largeNumber::operator + (const largeNumber & rhs) const {
    string num0, num1, sum; 
    num0 = num;
    num1 = rhs.num;
    int carryout=0;
    if(num0.size() > num1.size()) {
	num1.append(num0.size()-num1.size(), '0');
    } else if(num0.size() < num1.size()){
	num0.append(num1.size()-num0.size(), '0');
    }

    sum = "";
    for(size_t i=0; i< num0.size(); i++) {
	int bit0 = num0[i] - 48;
	int bit1 = num1[i] - 48;
	int s = bit0 + bit1 + carryout;
	int sumbit = s % 10;
	carryout = s / 10;
	sum.insert(0, 1,sumbit+48);
    }

    if(carryout == 1)
	sum.insert(0, 1,'1');

    return largeNumber(sum);
}

largeNumber largeNumber::operator * (const largeNumber & rhs) const {
    largeNumber product("0");
    for(int i=0; i<size(); i++) {
	int carryout = 0;
	int bit0 = num[i] - 48;
	string p = "";
	for(int j=0; j<rhs.size(); j++) {
	    int bit1 = rhs[j] - 48;
	    int s = bit0*bit1+carryout;
	    int bitr = s % 10;
	    carryout = s/10;
	    p.insert(0,1,bitr+48);
	}
	if(carryout>0) p.insert(0,1,carryout+48);
	p.append(i,'0');
	product = product + largeNumber(p);
    }

    return product;
}

bool largeNumber::operator == (const largeNumber & rhs) {
    return num == rhs.num;
}

bool largeNumber::operator < (const largeNumber & rhs) {
    if(size() < rhs.size()) return true;
    if(size() > rhs.size()) return false;
    for(int i=size()-1; i>=0; i--) {
	if(num[i]<rhs.num[i]) return true;
	else if(num[i]>rhs.num[i]) return false;
    }
    return false;
}

bool largeNumber::operator <= (const largeNumber & rhs) {
    return this->operator < (rhs) || this->operator == (rhs);
}

ostream & operator << (ostream & os, const largeNumber & rhs) {
    for(int i=rhs.size()-1; i>=0; i--)
	os<<rhs[i];
    return os;
}

istream & operator >> (istream & os, largeNumber & rhs) {
    string str;
    os >> str;

    rhs = largeNumber(str);
    return os;

}

bool isFair(const largeNumber & ln) {
    int i0 = 0, i1 = ln.size()-1;
    while(i1>=i0) {
	if(ln[i0]!=ln[i1])
	    return false;
	--i1;
	++i0;
    }
    return true;
}


int main(int argc, char ** argv) {
    //read
    ifstream file(argv[1]);
//    ifstream file("input.txt");
    ofstream ofile("output.txt");
    int numT;
    file>>numT;

    for(int i=0; i<numT; i++) {
	largeNumber A, B;
	file>>A>>B;
	largeNumber beginner("1");
	largeNumber tester("1");
	largeNumber counts("0");
	while(tester*tester < A){
	    beginner = tester;
	    tester = tester * largeNumber("2");
	}

	while( beginner*beginner <= B) {
	    if(A <= beginner*beginner && isFair(beginner) && isFair(beginner*beginner)) {
		counts = counts + largeNumber("1");
	    }
	    beginner = beginner + largeNumber("1");
	}
	ofile<<"Case #"<<(i+1)<<": "<<counts<<endl;
    }


    return 0;
}
