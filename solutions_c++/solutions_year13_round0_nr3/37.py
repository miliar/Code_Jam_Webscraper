#include <iostream>
#include <math.h>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
/*
Idea :  let a = [a_{d-1} ... a_0] be palindromes, A = a*a  
A_{i} is came from the summation of a_{i}*a_{0}, a_{i-1}*a_{1}, ...
In our case, we require the summation less than 10.
Consider a_{d-1}*d_0 + a_{d-2}*a_1 + ... + a_0 * a_{d-1}, a_0 cannot be larger than 2.
so we have e.g. 10001, 20002, 11111, 111111111, 1111001111, 101110011101, 20000100002.
For any d, we can have at most 9 1-digits.
When d is odd, we can have at most 2 2-digits and a 1-digit or at most 4 1-digits and a 2-digit.
When d is even, we can have at most 2 2-digits.

Result: for d>=4, number of Fair and Square of a with d digits = (sum_{i=0}^{3}[(d/2 - 1) choose i]) + 1 when d is even
= (sum_{i=0}^{1}[((d-1)/2 - 1) choose i]) * 3 + sum_{i=2}^{3}[((d-1)/2 -1) choose i])*2 +2   when d is odd 
*/

//for same length return false if a >= b
bool strcomp(string a, string b){
	if (a.size() < b.size()){
		return true;
	}else if(a.size() > b.size()){
		return false;
	}else{
	//int l = strlen(a);
	int l = a.size();

	//cout << l << endl;
	int i;
	//for (i=l-1;i>=0;i--){
	for (i=0;i<l;i++){
		//cout << a[i];
		if (a[i] < b[i]){
			return true; 
		}else if (a[i] > b[i]){
			return false;
		}
	}
	return false;
	}
}

string square(string b, int i){
	char* a = new char[2*i-1];
	int j, k;
		for (j=0;j<i;j++){
			int total = 0;
			for (k=0;k<=j;k++){
				total += (b[k]-'0') * (b[j-k] - '0');
			}
			if (total < 0 || total > 9){
				cout << " ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" <<endl;
			}
			a[j] = total + '0';
			a[2*i-2-j] = a[j];
		}
		string s(a);
		delete [] a;
		return s;
}

int main(){

	int i,j,k,l;
	//char* a = "211";
	//char* b = "111";
	//cout << strcomp(a, b);
	vector<string> p2;
	vector<string> p;
//	char a[100];
//	char b[50];
	p.push_back("1");
	p.push_back("2");
	p.push_back("3");
	p.push_back("11");
	p.push_back("22");
	p.push_back("101");
	p.push_back("111");
	p.push_back("121");
	p.push_back("202");
	p.push_back("212");

	p2.push_back("1");
	p2.push_back("4");
	p2.push_back("9");
	p2.push_back("121");
	p2.push_back("484");
	p2.push_back("10201");
	p2.push_back("12321");
	p2.push_back("14641");
	p2.push_back("40804");
	p2.push_back("44944");

	for (i=4;i<52;i++){
		string b(i, '0');
		b[0] = '1';
		b[i-1] = '1';
		for (j=1;j<i-1;j++){
			b[j] = '0';
		}
		p.push_back(b);
		p2.push_back(square(b,i));

		if (i%2==0){
			for (j=1;j<=(i-1)/2;j++){
				b[j] = '1';
				b[i-1-j] = '1';
				p.push_back(b);
				p2.push_back(square(b,i));
				b[j] = '0';
				b[i-1-j] = '0';
			}
			for (j=1;j<=(i-1)/2 -1;j++){
				for (k=j+1;k<=(i-1)/2;k++){
					b[j] = '1';
					b[k] = '1';
					b[i-1-j] = '1';
					b[i-1-k] = '1';
					p.push_back(b);
					p2.push_back(square(b,i));
					b[j] = '0';
					b[k] = '0';
					b[i-1-j] = '0';
					b[i-1-k] = '0';
				}
			}
			for (j=1;j<=(i-1)/2 - 2;j++){
				for (k=j+1;k<=(i-1)/2 -1; k++){
					for(l=k+1;l<=(i-1)/2;l++){
						b[j] = '1';
						b[k] = '1';
						b[l] = '1';
						b[i-1-j] = '1';
						b[i-1-k] = '1';
						b[i-1-l] = '1';
						p.push_back(b);
						p2.push_back(square(b,i));
						b[j] = '0';
						b[k] = '0';
						b[l] = '0';
						b[i-1-j] = '0';
						b[i-1-k] = '0';
						b[i-1-l] = '0';
					}
				}
			}
			b[0] = '2';
			b[i-1] = '2';
			p.push_back(b);
			p2.push_back(square(b,i));
		}else{
			b[(i-1)/2] = '1';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '2';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '0';

			for (j=1;j<(i-1)/2;j++){
				b[j] = '1';
				b[i-1-j] = '1';
				p.push_back(b);
				p2.push_back(square(b,i));
			b[(i-1)/2] = '1';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '2';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '0';
				b[j] = '0';
				b[i-1-j] = '0';
			}
			for (j=1;j<(i-1)/2 -1;j++){
				for (k=j+1;k<(i-1)/2;k++){
					b[j] = '1';
					b[k] = '1';
					b[i-1-j] = '1';
					b[i-1-k] = '1';
					p.push_back(b);
					p2.push_back(square(b,i));
			b[(i-1)/2] = '1';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '0';
					b[j] = '0';
					b[k] = '0';
					b[i-1-j] = '0';
					b[i-1-k] = '0';
				}
			}
			for (j=1;j<(i-1)/2 - 2;j++){
				for (k=j+1;k<(i-1)/2 -1; k++){
					for(l=k+1;l<(i-1)/2;l++){
						b[j] = '1';
						b[k] = '1';
						b[l] = '1';
						b[i-1-j] = '1';
						b[i-1-k] = '1';
						b[i-1-l] = '1';
						p.push_back(b);
						p2.push_back(square(b,i));
			b[(i-1)/2] = '1';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '0';
						b[j] = '0';
						b[k] = '0';
						b[l] = '0';
						b[i-1-j] = '0';
						b[i-1-k] = '0';
						b[i-1-l] = '0';
					}
				}
			}
			b[0] = '2';
			b[i-1] = '2';
			p.push_back(b);
			p2.push_back(square(b,i));
			b[(i-1)/2] = '1';
			p.push_back(b);
			p2.push_back(square(b,i));
		}
/*
		sort(p.begin(), p.end(), strcomp);
		sort(p2.begin(), p2.end(), strcomp);
		
		for (j=0;j<p.size();j++){
			cout << p[j] << endl;
		}
		cout << endl;
		for (j=0;j<p2.size();j++){
			cout << p2[j] << endl;
		}
		*/

	}
		sort(p.begin(), p.end(), strcomp);
		sort(p2.begin(), p2.end(), strcomp);

//		cout <<"size of p : " << p.size() <<endl;
//		for (j=0;j<p.size();j++){
//			cout << p[j] << endl;
//		}
//		cout << endl;
//		cout <<"size of p2 : " << p2.size() <<endl;
//		for (j=0;j<p2.size();j++){
//			cout << p2[j] << endl;
//		}

	int T;
	cin >> T;

	for (i=1;i<=T;i++){
		char A[105], B[105];
		cin >> A >> B;
		string start(A), end(B);
		vector<string>::iterator low = lower_bound(p2.begin(), p2.end(), start, strcomp);
		vector<string>::iterator up = upper_bound(p2.begin(), p2.end(), end, strcomp);
		cout <<"Case #"<<i<<": "<<up-low <<endl;
	}



	return 0;
}


/*
string convertInt(long long number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

bool isPalindromes(string s){
	int i;
	for (i=0;i< ceil((double)s.size()/2);i++){
		if (s[i] != s[s.size()-1-i]){
			return false;
		}
	}
	return true;
}

int main(){
//	long  long A = pow((long double)10,14);
//	cout << A;
	int T;
	cin >> T;
	int i;
	long long j;
	for (i=1;i<=T;i++){
		long long A, B;
		cin >> A >> B;
		long long a = ceil(sqrt((long double)A)), b = floor(sqrt((long double)B));
		long long count = 0;
		string n;
		for (j=a;j<=b;j++){
			n = convertInt(j);
			//cout << n;
			if (isPalindromes(n) && isPalindromes(convertInt(j*j))){
				count++;
			}
		}
		cout <<"Case #"<<i<<": "<<count <<endl;
	}

	return 0;
}
*/