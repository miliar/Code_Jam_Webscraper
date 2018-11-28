#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

enum {ONE, I, J, K};

int mult[4][4] = {
    {ONE,I,J,K},
    {I,ONE,K,J},
    {J,K,ONE,I},
    {K,J,I,ONE},
};

int multSign[4][4] = {
    {+1,+1,+1,+1},
    {+1,-1,+1,-1},
    {+1,-1,-1,+1},
    {+1,+1,-1,-1},
};

int invArr[4] = {ONE,I,J,K};
int signInvArr[4] = {+1,-1,-1,-1};

struct Q {
    Q() {}
    Q(int idA_, int s_) : idA(idA_), s(s_) {}
    int idA, s;

    int id() {
	return idA + 2*(1+s);
    }

    Q inv() {
	return Q(invArr[idA],signInvArr[idA]*s);
    }

    void Print() {
	string name[4] = {"1", "i", "j", "k"};
	if(s == -1) {
	    cout << "-";
	}
	cout << name[idA];
    }
};

Q operator* (const Q & a, const Q & b) {
    return Q(mult[a.idA][b.idA],a.s*b.s*multSign[a.idA][b.idA]);
}

bool operator== (const Q & a, const Q & b) {
    return a.idA == b.idA && a.s == b.s;
}


string result(vector<Q> v) {
    vector<Q> cumMult = {Q(ONE,1)};
    bool seenI = false, seenK = false;
    for(Q q : v) {
	cumMult.push_back(cumMult.back()*q);
	seenI = seenI || (cumMult.back() == Q(I,1));
	seenK = seenK || (seenI && cumMult.back() == Q(K,1));
    }
    if(!seenK || !(cumMult.back() == Q(ONE,-1))) {
	return "NO";	    
    }
    return "YES";
}

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
	int L, X;
	cin >> L >> X;
	while(X > 50) {
	    X -= 4;
	}
	cin.ignore();
	string w;
	cin >> w;
	cin.ignore();
	vector<Q> v;
	for(int x = 0; x < X; x++) {
	    for(int i = 0; i < L; i++) {
		v.push_back(Q(w[i]-'i'+1,1));
	    }
	}
	cout << "Case #" << t+1 <<": " << result(v) << endl;
    }
    return 0;
}
