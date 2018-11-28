#include <iostream>
#include <set>
#include <algorithm>

// #define DEBUG

using namespace std;
typedef set<double>::iterator block_iter;
struct person{
  int point;
  set<double> blocks;

  person():point(0), blocks(){}
  void insert(double x){blocks.insert(x);}

  // I assume blocks is not empty below
  double get_min(){return *blocks.begin();}
  double get_max(){return *blocks.rbegin();}
  double get_minimum_above(double val){
	for(block_iter it=blocks.begin();it!=blocks.end();++it){
	  if(val<*it) return *it;
	}
	return *(blocks.begin());	// when failure return minimum one
  }
  void erase(double val){blocks.erase(val);}
};

bool always_ok(person& A, person& B){
  block_iter a = A.blocks.begin(), b = B.blocks.begin();
  for(;a!=A.blocks.end();++a,++b){
	if(*a<=*b) return false;
  }
  return true;
}

void judge(person& A, double block_A, person& B, double block_B){
  if(block_A > block_B){
#ifdef DEBUG
	cerr << "naomi won: " << block_A << " vs " << block_B << endl;
#endif
	A.point++;
  }else if(block_A < block_B){
#ifdef DEBUG
	cerr << "ken won:   " << block_A << " vs " << block_B << endl;
#endif
	B.point++;
  }else{
#ifdef DEBUG
	cerr << "stalemate!!!" << endl;
#endif
  }
  A.erase(block_A);
  B.erase(block_B);
}

int main(){
  int T;
  cin >> T;
  for(int Case=1;Case<=T;++Case){
	int N;
	cin >> N;
	person naomi, ken;
	double tmp;
	for(int i=0;i<N;++i){
	  cin >> tmp;
	  naomi.insert(tmp);
	}
	for(int i=0;i<N;++i){
	  cin >> tmp;
	  ken.insert(tmp);
	}
	person naomi_ = naomi, ken_ = ken;

	// Deceitful War
#ifdef DEBUG
	cerr << "Deceitful War..." << endl;
#endif
	bool flag = false;
	for(int i=0;i<N;++i){
	  double n, k;				// blocks from naomi and ken
	  n = naomi.get_min();
	  double told;

	  if(!flag){
		flag |= always_ok(naomi, ken);
	  }
	  if(flag){
		told = ken.get_max() + 1e-7;
	  }else{
		told = ken.get_max() - 1e-7;
	  }
#ifdef DEBUG
	  cerr << "naomi told " << told << " instead of " << n << endl;
#endif
	  k = ken.get_minimum_above(told);
	  judge(naomi, n, ken, k);
	}

	// War
#ifdef DEBUG
	cerr << "War..." << endl;
#endif
	for(int i=0;i<N;++i){
	  double n, k;
	  n = naomi_.get_min();
	  k = ken_.get_minimum_above(n);
	  judge(naomi_, n, ken_, k);
	}

	cout << "Case #" << Case
		 << ": " << naomi.point
		 << " "  << naomi_.point
		 << endl;
  }
  return 0;
}
