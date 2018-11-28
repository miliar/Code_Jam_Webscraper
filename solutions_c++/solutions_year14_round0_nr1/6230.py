#include<set>
#include<iostream>
using namespace std;


template<typename T>
set<T> Intersection(const set<T>& a, const set<T>& b){
	set<T> res;
	for(auto it=a.begin(); it!=a.end(); it++){
		if(b.find(*it) != b.end()){
			res.insert(*it);
		}
	}
	return res;
}

template<typename T>
void input(set<T>& s){
	int row;
	cin >> row;
	for(int i=1;i<=4;i++){
		int a,b,c,d;
		cin >> a >> b >> c >> d;
		if(i==row){
			s.insert(a);
			s.insert(b);
			s.insert(c);
			s.insert(d);
		}
	}
}


int main(){
	int T;
	cin>>T;

	for(int C=1;C<=T;C++){
		set<int> X;
		set<int> Y;

		input(X);
		input(Y);

		auto Z = Intersection(X,Y);

		cout << "Case #" << C << ": ";
		if(Z.size() == 1){
			cout << *(Z.begin()) << endl;
		}
		else if(Z.size()>1){
			cout << "Bad magician!" << endl;
		}
		else{
			cout << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}
