#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int main() {
	int T,n=1;
	cin>>T;
	while(n<=T) {
		int normal=0, cheat=0, N;
		double temp;
		cin>>N;
		list<double> naomi,ken;
		for(int i=0;i<N;i++) {
			cin>>temp;
			naomi.push_back(temp);
		}
		naomi.sort();
		for(int i=0;i<N;i++) {
			cin>>temp;
			ken.push_back(temp);
		}
		ken.sort();
		
		list<double> naomi2(naomi),ken2(ken);

		while(naomi.size()) {
			if(naomi.back()>ken.back()) {
				normal++;
				naomi.pop_back();
				ken.pop_front();
			} else {
				naomi.pop_back();
				ken.pop_back();
			}
		}

		while(naomi2.size()) {
			if(naomi2.front()>ken2.front()) {
				cheat++;
				naomi2.pop_front();
				ken2.pop_front();
			} else {
				naomi2.pop_front();
				ken2.pop_back();
			}
		}

		cout<<"Case #"<<n<<": "<<cheat<<" "<<normal<<endl;
		n++;
	}
	return 0;
}