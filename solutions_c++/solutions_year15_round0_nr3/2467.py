#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <assert.h>

template<typename T>
std::ostream& operator<< (std::ostream& out, const std::vector<T>& v) {
    out << "[";
    size_t last = v.size() - 1;
    for(size_t i = 0; i < v.size(); ++i) {
        out << v[i];
        if (i != last) 
            out << ", ";
    }
    out << "]";
    return out;
}

enum QUAD{
	e = 'e',  i = 'i',  j = 'j',  k = 'k',
	n = 'n', ni = 'I', nj = 'J', nk = 'K'
};

bool negativ(QUAD a){
	return a == n or a == ni or a == nj or a == nk;
}

QUAD operator-(QUAD a){
	switch(a){
		case e:
		return n;
		case n:
		return e;
		
		case i:
		return ni;
		case ni:
		return i;
		
		case j:
		return nj;
		case nj:
		return j;
		
		case k:
		return nk;
		case nk:
		return k;
	}
}

QUAD operator*(QUAD a, QUAD b){
	bool an = negativ(a);
	bool bn = negativ(b);
	if(an)
		a = -a;
	if(bn)
		b = -b;
		
	QUAD c;
	if(a == e and b == e){
		c = e;
	}else if(a == e and b == i){
		c = i;
	}else if(a == e and b == j){
		c = j;
	}else if(a == e and b == k){
		c = k;
	}else if(a == i and b == e){
		c = i;
	}else if(a == i and b == i){
		c = n;
	}else if(a == i and b == j){
		c = k;
	}else if(a == i and b == k){
		c = nj;
	}else if(a == j and b == e){
		c = j;
	}else if(a == j and b == i){
		c = nk;
	}else if(a == j and b == j){
		c = n;
	}else if(a == j and b == k){
		c = i;
	}else if(a == k and b == e){
		c = k;
	}else if(a == k and b == i){
		c = j;
	}else if(a == k and b == j){
		c = ni;
	}else if(a == k and b == k){
		c = n;
	}
	
	if(an)
		c = -c;
	if(bn)
		c = -c;
	return c;
}

class Erreicht{
	bool Ee = false, Ei  = false, Ej  = false, Ek  = false,
         En = false, Eni = false, Enj = false, Enk = false;

	bool sub(bool &t){
		if(t)
			return true;
		else{
			t = true;
			return false;
		}
	}
	
	public:
	bool operator()(QUAD in){
		switch(in){
		case e:	return sub(Ee);
		case i:	return sub(Ei);
		case j:	return sub(Ej);
		case k:	return sub(Ek);
		case n:	return sub(En);
		case ni:return sub(Eni);
		case nj:return sub(Enj);
		case nk:return sub(Enk);
		}
	}
};


QUAD at(size_t &L, size_t &X, std::string &ijk, size_t p){
	auto c = ijk[p % L];
	if(c == 'i')
		return i;
	else if(c == 'j')
		return j;
	else if(c == 'k')
		return k;
	assert(false);
}

bool solve(size_t L, size_t X, std::string ijk){
	QUAD l = e, m = e, r = e;
	
	size_t size = X*L;
	
	//std::cout << "L = " << L << ", X = " << X << ", ijk = " << ijk << "\n";
	/*std::cout << "string: ";
	for(size_t i = 0; i<size; i++)
		std::cout << (char) at(L, X, ijk, i);
	std::cout << "\n";*/
	
	Erreicht lockL;
	size_t i_left;
	for(i_left=0; i_left<size; i_left++){
		l = l * at(L, X, ijk, i_left);
		if(l == i)
			break;
		/*if(i_left % L == 0){
			//std::cout << "schaue auf lock1, index=" << i_left << ", v="<<(char)l<<"\n";
			if(lockL(l)){
				//std::cout << "Lock1 schlaegt zu\n";
				break;
			}
		}*/
	}
		/*std::cout << "left:   v = "<< (char)l << " -> ";
	for(size_t i = 0; i<i_left+1; i++)
		std::cout << (char) at(L, X, ijk, i);
	std::cout << "\n";*/
	if(l != i)
		return false;
	
	size_t i_right;
	Erreicht lockR;
	for(i_right=size-1; i_right>0; i_right--){
		r = at(L, X, ijk, i_right) * r;
		if(r == k)
			break;
		/*if(i_right % L == 0){
			//std::cout << "schaue auf lock2, index=" << i_right << ", v="<<(char)r<<"\n";
			if(lockR(r)){
				//std::cout << "Lock2 schlaegt zu\n";
				break;
			}
		}*/
	}
		/*std::cout << "right:  v = "<< (char)r << " -> ";
	for(size_t i = i_right; i<size; i++)
		std::cout << (char) at(L, X, ijk, i);
	std::cout << "\n";*/
	if(r != k)
		return false;

	Erreicht lockM;
	for(size_t i_middle = i_left+1; i_middle < i_right; i_middle++){
		m = m * at(L, X, ijk, i_middle);
		/*if(i_middle % L == 0){
//					std::cout << "schaue auf lock3, index=" << i_middle << ", v="<<(char)m<<"\n";
			if(lockM(m)){
//							std::cout << "Lock3 schlaegt zu\n";
				break;
			}
		}*/
	}


	/*std::cout << "middle: v = "<< (char)m << " -> ";
	for(size_t i = i_left+1; i<i_right; i++)
		std::cout << (char) at(L, X, ijk, i);
	std::cout << "\n";*/
	return m == j;


	
	

	
	/*std::cout << "i_left = " << i_left << ", l==i = " << (l == i) << "\n";
	std::cout << "m==j = " << (m == j) << "\n";
	std::cout << "i_right = " << i_right << ", r==k = " << (r == k) << "\n";*/
	//std::cout << "\n\n\n";
}

void test(){
	assert(e*e == e);
	assert(n*n == e);
	
	assert(n*i == ni);
	assert(i*n == ni);
	
	assert(i*j == k);
	assert(j*i == nk);
}

int main (int argn, char** args){
	//test();
	std::string in = args[1];
	std::string out = args[2];

	std::fstream input(in, std::ios_base::in);
	std::fstream output(out, std::ios_base::out);
	
	size_t cases;
	input >> cases;
	for(size_t i=0; i<cases; i++){
		size_t L, X;
		std::string ijk;
		input >> L >> X >> ijk;
		
		output << "Case #" << (i+1) << ": " << (solve(L, X, ijk) ? "YES" : "NO" ) << "\n";
	}


	return 0;
}