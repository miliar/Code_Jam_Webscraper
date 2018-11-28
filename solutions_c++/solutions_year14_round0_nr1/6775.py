#include<iostream>
#include<vector>
using namespace std;

void ratkaise(int ca) {
	vector<int> vaihtoehdot;
	int sarake;
	cin>>sarake;
	sarake--;
	for(int i=0;i<16;i++) {
		int luku;
		cin>>luku;
		if (i/4==sarake) {
			vaihtoehdot.push_back(luku);
		}
	}
	cin>>sarake;
	sarake--;
	for(int i=0;i<16;i++) {
		int luku;
		cin>>luku;
		if (i/4 == sarake) {
			vaihtoehdot.push_back(luku);
		}
	}
	int vastaus = -1;
	bool t = true;
	for(int i=0;i<4;i++) {
		for(int j=4;j<8;j++) {
			if (vaihtoehdot[i] == vaihtoehdot[j]) {
				if (vastaus == -1) {
					vastaus = vaihtoehdot[i];
				} else {
					t = false;
				}
			}
		}
	}
	if (vastaus != -1 && t) {
		cout<<"Case #"<<ca<<": "<<vastaus<<endl;
	} else if (vastaus == -1) {
		cout<<"Case #"<<ca<<": Volunteer cheated!"<<endl;
	} else if (!t) {
		cout<<"Case #"<<ca<<": Bad magician!"<<endl;
	}
}

int main() {
	int lkm;
	cin>>lkm;
	for(int i=0;i<lkm;i++) {
		ratkaise(i+1);
	}
	return 0;
}
