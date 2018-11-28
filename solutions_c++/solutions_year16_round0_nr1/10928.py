#include<iostream>
#include<bitset>
#include<vector>
#include<string>
#include<sstream>
// #include<fstream>

using namespace std;

#define BASE 10

class MyBigInt {
private:
	vector<int> number;
public:
	MyBigInt(long long);
	MyBigInt operator +(MyBigInt const &) const;
	MyBigInt operator +=(MyBigInt const &);
	int operator [](int const &);
	int size();
	string toString();
};

string MyBigInt::toString() {
	stringstream ss;
	for(vector<int>::reverse_iterator it = number.rbegin(); it!=number.rend(); it++) {
		ss<<*it;
	}
	return ss.str();
}

int MyBigInt::size() {
	return number.size();
}

int MyBigInt::operator [](int const &index) {
	return number[index];
}

MyBigInt MyBigInt::operator +=(MyBigInt const &b) {
	vector<int>::iterator it1 = number.begin();
	vector<int>::const_iterator it2 = b.number.begin();
	int sum = 0;
	int carry = 0;
	while(it1!=number.end() || it2!=b.number.end()) {
		if(it1!=number.end()) {
			sum += *it1;
		} else {
			number.push_back(0);
		}

		if(it2!=b.number.end()) {
			sum += *it2;
			it2++;
		}
		//storing sum in this number i.e. it1
		*it1 = sum%BASE;
		//storing carry of next iteration in current sum variable.
		sum /= BASE;
		//incrementing it1
		it1++;
	}
	if(sum) {
		number.push_back(1);
	}
	return *this;
}

MyBigInt MyBigInt::operator +(MyBigInt const &b) const {
	MyBigInt a = *this;
	a += b;
	return a;
}

MyBigInt::MyBigInt(long long input) {
	while(input > 0) {
		number.push_back((int) input%BASE);
		input /= BASE;
	}
}

string willSleep(long long N) {
	bitset<10> bits;
	int i = 1;
	MyBigInt num(N);
	//cout<<"num = "<<num.toString()<<endl;
	MyBigInt n(N); 
	int rem = 0;
	// ofstream file;
	// file.open("output1.txt",ios_base::app);
	// file<<"------"<<N<<"------"<<endl;
	do {
		if(i>1) {
			n+=num;
		}
		//file<<n<<endl;

		// while (n>0) {
		// 	rem = n%10;
		// 	n = n/10;
		// 	bits.set(rem);
		// }
		for(int index=0; index < n.size(); index++) {
			bits.set(n[index]);
		}
		i++;

	} while (!bits.all());
//	file.close();
	return n.toString();
}

int main() {
	bitset<10> bits;
	int T;
	long long N;
	cin>>T;
	int i = 1;
	while(i<=T) {
		cin>> N;
		if(N==0) {
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		} else {
			cout<<"Case #"<<i<<": "<<willSleep(N)<<endl;
		}
		i++;
	}
}
