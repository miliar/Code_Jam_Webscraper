#include <vector>
#include <iostream>
using namespace std;
class Element;

vector< vector <Element> > mapping;

class Element{
	public:
	Element(unsigned char val, bool s){
		this->val = val;
		this->s = s;
	}

	bool s;
	unsigned char val;

	void mul(unsigned char c){
		unsigned char newval = mapping[this->val][c].val;
		if (mapping[this->val][c].s == true){
			this->s = !this->s;
		}else{
		}
		this->val = newval;
	}
};
class ElementMatcher{
	public:
	vector<unsigned char> pattern;
	int len;
	int nT;
	bool detect(){
		Element q(0,false);
		unsigned char anticipated = 1;
		for(int i=0; i<nT; i++){
		for(int j=0; j<len; j++){
			unsigned char c = pattern[j];
			q.mul(c);
			if (q.val == anticipated && q.s == false){
				anticipated++;
				q.val = 0;
				q.s = false;
			}
		}
		}
		if(anticipated == 4 && q.val == 0 && q.s == false){
			return true;
		}else{
			return false;
		}
	}
};
void init(){
	Element p_one(0,false);
	Element minus_one(0,true);
	Element p_j(2,false);
	Element p_k(3,false);
	Element minus_k(3,true);
	Element p_i(1,false);
	Element minus_i(1,true);
	Element minus_j(2,true);
	
	vector <Element> v;
	v.push_back(p_one);
	v.push_back(p_i);
	v.push_back(p_j);
	v.push_back(p_k);
	mapping.push_back(v);
	v.clear();
	
	v.push_back(p_i);
	v.push_back(minus_one);
	v.push_back(p_k);
	v.push_back(minus_j);
	mapping.push_back(v);
	v.clear();
	
	v.push_back(p_j);
	v.push_back(minus_k);
	v.push_back(minus_one);
	v.push_back(p_i);
	mapping.push_back(v);
	v.clear();
	
	v.push_back(p_k);
	v.push_back(p_j);
	v.push_back(minus_i);
	v.push_back(minus_one);
	mapping.push_back(v);
	v.clear();
}
int main() {
	init();
	int nT = 0;
	cin>>nT;
	for(int tN = 1; tN <= nT; tN++){
		ElementMatcher elementMatcher;
		cin>>elementMatcher.len>>elementMatcher.nT;
		char c;
		for(int i=0;i<elementMatcher.len;i++){
			cin>>c;
			elementMatcher.pattern.push_back((unsigned char)(c - 'h'));
		}
		cout<<"Case #"<<tN<<": ";
		if(elementMatcher.detect()){
			cout<<"YES";
		}else{
			cout<<"NO";
		}
		cout<<endl;
	}
	return 0;
}
