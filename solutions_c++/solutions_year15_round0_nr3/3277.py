//Joe Snider
//
//google codejam 2015 qual 3
//

#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

//only one is non-zero
class QB{
public:
	short w,i,j,k;
	QB():w(0),i(0),j(0),k(0){}
	QB(const short& w, const short& i, const short& j, const short& k):
		w(w),i(i),j(j),k(k){}
	QB& operator*=(const QB& q) {
		short wt = w*q.w - i*q.i - j*q.j - k*q.k;
		short it = w*q.i + j*q.k - k*q.j;
		short jt = w*q.j + k*q.i - i*q.k;
		short kt = w*q.k + i*q.j - j*q.i;
		w=wt;
		i=it;
		j=jt;
		k=kt;
		return *this;
	}
	
	
	
	bool operator==(const QB& q) const {
		return w==q.w && i==q.i && j==q.j && k==q.k;
	}
	bool operator!=(const QB& q) const {
		return !(*this == q);
	}
};

std::ostream& operator<<(std::ostream& out, const QB& q){
   return out << q.w << " " << q.i << " " << q.j <<  " " << q.k ;
}

QB onePower(const QB& q, const long& n) {
	QB ret(1,0,0,0);
	int m2 = n % 4;
	for(int i = 0; i < m2; ++i) {
		ret *= q;
	}
	return ret;
}

bool bigTest(map<char, QB>& table, const string& S, const long long& X) {
	auto cur = table.begin();
	QB v(1,0,0,0);
	for(int xx = 0; xx < X; ++xx) {
	//cout << "gh1 " << v << "\n" << flush;
		for(auto ss = S.begin(); ss != S.end(); ++ss) {
			v *= table[*ss];
			if(v == cur->second) {
				++cur;
				if(cur == table.end()) {
					return true;
				}
				v = QB(1,0,0,0);
			}
		}
	}
	return false;
}

int main() {
	QB i(0,1,0,0);
	QB j(0,0,1,0);
	QB k(0,0,0,1);
	QB m1(-1,0,0,0);
	map<char, QB> table;
	table['i'] = i;
	table['j'] = j;
	table['k'] = k;

	long long T, L, X;
	string S;
	
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cin >> L >> X;
		//cout << "gh1 " << X << "\n";
		cin >> S;
		QB v(1,0,0,0);
		for(auto ss = S.begin(); ss != S.end(); ++ss) {
			v *= table[*ss];
		}
		v = onePower(v,X);
		if(v == m1 && bigTest(table, S, X)) {
			cout << "Case #" << i+1 << ": YES" << "\n";
		} else {
			cout << "Case #" << i+1 << ": NO" << "\n";
		}
	}
	
	return 0;
}

