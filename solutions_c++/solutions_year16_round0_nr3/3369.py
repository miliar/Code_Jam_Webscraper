#include <iostream>
#include <bitset>
#include <cmath>
using namespace std;
unsigned long long power(int base, int exp) {
    unsigned long long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

int isprime(unsigned long long t) {
	for (int i = 2; i < sqrt(t)+1; ++i) {
		if (t%i==0) {
			return i;
		}
	}
	return 0;
}
int isok(string t, int b) {
	unsigned long long sum = 0;
	for(int i = 0; i< 16; ++i) {
		if (t[15-i] == '1')
			sum += power(b,i);
	}
	return isprime(sum);
}



int main() {
	cout<<"Case #1:"<<endl;
	int T;
	cin>>T;
	int length;
	int number;
	int array[9];
	int count = 0;
	cin>>length>>number;
	for(int i = power(2,length-1)+1; i<(power(2,length)-1); i = i+2) {
		string tmp = bitset<16>(i).to_string();
		bool print = true;
		for (int i = 2; i < 11; ++i) {
			array[i-2] = isok(tmp,i);
			if (array[i-2] == 0) {
				print = false;
				break;
			}
		}
		if (print) {
			count++;
			cout<<tmp<<" ";
			for(int i = 0; i < 8; ++i)
				cout<<array[i]<<" ";
			cout<<array[8]<<endl;
		}
		if (count == number) {
			return 1;
		}

	}
	/*length = length-2;
	for(int i = 1; i<=length; ++i) {
		string tmp;
		for(int j = 0; j<pow(2,i);++i) {
			tmp = bitset<6>(j).to_string();
			for(int j = 2;j<=10;++j) {
				unsigned long long baise = 1+pow(j,length+1);
				unsigned long long sum = 0;
				int count = 0;
				for (int k = 0; k <= i; ++i) {
					sum = sum*j+(tmp[6-k]-0);
				}
				sum=sum*j+baise;
				bool t = true;
				for(int k = 2; k < sum; ++k) {
					if(sum%k==0) {
						array[j] = k;
						count++;
						t = false;
						break;
					}
				}
				if(t) break;
				if (count == 9) {
					cout<<"1"<<tmp<<"1";
					for(int c = 0; c<8; ++c) {
						cout<<array[c]<< " ";
					}
					cout<<array[8]<<endl;
				}
		    }
		}
		
	}*/
}
