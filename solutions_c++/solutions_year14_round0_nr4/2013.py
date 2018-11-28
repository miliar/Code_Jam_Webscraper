#include <iostream>
//#include <algorithm>
#include <list>
using namespace std;


int main(){
	list<double> Na;
	list<double> Ke;

	int T;
	cin>>T;

	for (int i=1;i<=T;i++){
		int N;
		cin>>N;
		Na.clear();
		Ke.clear();

		double d;
		for (int j=0;j<N;j++) {
			cin>>d;
			Na.push_back(d);
		}

		for (int j=0;j<N;j++) {
			cin>>d;
			Ke.push_back(d);
		}

		Na.sort();
		Ke.sort();
		

		int D=0;

		list<double>::iterator j=Na.begin();
		list<double>::iterator l=Ke.begin();

		while (j!=Na.end()){
			if ((*j)>(*l)) {
				j++;
				l++;
				D++;
				continue;
			}
			j++;
		}
//		continue;

		int O=N;
		j=Na.begin();
		l=Ke.begin();
//		list<double>::iterator l=Ke.begin();

		while (l!=Ke.end()) {
			if ((*l)>(*j)) {
				O--;
				Na.pop_front();
				j=Na.begin();
				l=Ke.erase(l);
				continue;
			}

			l++;
		};


		cout<<"Case #"<<i<<":";
		cout<<" "<<D;
		cout<<" "<<O;
		cout<<endl;
	}

	return 0;
}
