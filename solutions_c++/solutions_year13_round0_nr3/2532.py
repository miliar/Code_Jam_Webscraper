#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>
#include <queue>

namespace stringutil {

template<typename T>
std::string binary2string(T value, int base) {
    assert(base == 8 || base == 10 || base == 16);
    std::ostringstream os;
    switch (base) {
    case 8:
        if (value < 0) {
            os << '-';
            value *= -1;
        }
        os << std::oct;
        break;
    case 10:
        os << std::dec;
        break;
    case 16:
        if (value < 0) {
            os << '-';
            value *= -1;
        }
        os << std::hex;
        break;
    }
    os << value;  
    return os.str();
}
}

using namespace std;
using namespace stringutil;

bool palin(long long n){
	string s = binary2string(n, 10);
	//cout << "s:" << s << endl;
	int m = (int)s.size();
	if(m==1)	return true;
	if(m%2==0){
		for(int i=0;i<m;i++){
			int front = i;
			int back = m-1-i;
			if(back < front)	break;
			if(s[front]!=s[back])	return false;
		}
		return true;
	}else{
		for(int i=0;i<m;i++){
			int front = i;
			int back = m-1-i;
			if(back == front)	break;
			if(s[front]!=s[back])	return false;
		}
		return true;
	}
}

long long root(long long n){
	for(long long i=1;i<=(long long)sqrt((double)n);i++){
		if(i*i==n)	return i;
	}
	return -1;
}

vector <long long> genPalin(int R){
	vector <long long> palin;

	for(int r=1;r<=R;r++){
		queue <string> Q;
		if(r%2!=0){
			if(r==1){
				for(int i=1;i<10;i++)	Q.push( binary2string(i, 10) );
			}else{
				for(int i=0;i<10;i++)	Q.push( binary2string(i, 10) );
				for(int i=0;i<(r-1)/2;i++){
					queue <string> temp;
					while(!Q.empty()){
						string s = Q.front();
						Q.pop();
						for(int j=0;j<10;j++){
							if(i==(r-1)/2-1 && j==0)	continue;
							string c = binary2string(j, 10);
							temp.push( c+s+c );
						}
					}
					Q = temp;
				}
			}
		}else{
			Q.push( "" );
			for(int i=0;i<(r-1)/2+1;i++){
				queue <string> temp;
				while(!Q.empty()){
					string s = Q.front();
					Q.pop();
					for(int j=0;j<10;j++){
						if(i==(r-1)/2 && j==0)	continue;
						string c = binary2string(j, 10);
						temp.push( c+s+c );
					}
				}
				Q = temp;
			}
		}

		while(!Q.empty()){
			string s = Q.front();
			Q.pop();
			istringstream is(s);
			long long x;
			is >> x;
			palin.push_back( x );
		}
	}
	return palin;
}

int searchLow(const vector <long long> list, long long A){
	int low = 0;
	int high = (int)list.size()-1;
	int mid;

	while( low <= high ){
		mid = (high+low)/2;
		if(list[mid]*list[mid] < A){
			low = mid+1;
		}else{
			if(mid==0)	return mid;
			else if(list[mid-1]*list[mid-1]<A){
				return mid;
			}
			else{
				high = mid-1;
			}
		}
	}
	return 0;
}

int searchHigh(const vector <long long> list, long long B){
	int low = 0;
	int high = (int)list.size()-1;
	int mid;

	while( low <= high ){
		mid = (high+low)/2;
		if(list[mid]*list[mid] > B){
			high = mid-1;
		}else{
			if(mid==(int)list.size()-1)	return mid;
			else if(list[mid+1]*list[mid+1]>B){
				return mid;
			}
			else{
				low = mid+1;
			}
		}
	}
	return (int)list.size()-1;
}

int main(){
	int T;
	cin >> T;

	vector <long long> list = genPalin( 7 );
	//for(int i=0;i<list.size();i++){d
	//	cout << list[i] << endl;
	//}
	sort( list.begin(), list.end() );

	for(int t=1;t<=T;t++){
		long long A, B;
		cin >> A >> B;

		int Ans = 0;
		int low = searchLow( list, A );
		int high = searchHigh( list, B );
		for(int i=low;i<=high;i++){
			if( palin(list[i]*list[i]) ) Ans++; 
		}

		printf("Case #%d: %d\n", t, Ans);
	}

	return 0;
}