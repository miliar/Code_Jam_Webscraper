#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int power (int number, int index) {
    if (index == 0) {
        return 1;
    }
    int num = number;
    for (int i = 1; i < index; i++) {
        number = number * num;
    }
    return number;
}

int main() {
	int T;
	unsigned long long A,B,LIM;
	string G;
	vector<unsigned long long> vsq;
	vector<unsigned long long> vfsq;
	vector<string> vstr;
	map<unsigned long long,unsigned long long> msq, msqr;
	map<string, unsigned long long> mstr;
	//LIM=100000000000000;
	LIM=100000000000000;
	//cout<<"LIM:" << LIM<<endl;

	for (unsigned long long i=1;i<LIM;i++) {
		unsigned long long sq=i*i;
		if(sq>LIM) {
			break;
		}
		vsq.push_back(sq);
		msq.insert(make_pair(sq, i));
		msqr.insert(make_pair(i, sq));
		//cout << sq << " ";
	}
	//cout << vsq.size();
	//return 0;
	for (unsigned long long i=0;i<vsq.size();i++) {
		stringstream ss;
		ss << vsq[i];
		string pal = ss.str();
		//cout <<i<<":"<<vsq[i]<<endl;
		if (pal==string(pal.rbegin(), pal.rend())) {
			map<unsigned long long,unsigned long long>::iterator it = msq.find(vsq[i]);
			if(it != msqr.end())
			{
				//element found;
				unsigned long long sqr = it->second;

				stringstream ss1;
				ss1 << sqr;
				string pal1 = ss1.str();
				if (pal1==string(pal1.rbegin(), pal1.rend())) {
					vfsq.push_back(vsq[i]);
					mstr.insert(make_pair(pal, 1));
					//cout << sqr << " " << vsq[i] << " " ;
					//cout<<endl;
				}
			}
		}
	}
	//cout << endl << endl;
	//cout << vfsq.size() << endl;

	cin>>T;
	string tmp;
	getline(cin, tmp);
	int count=0;
	for(int i=1; i<=T; i++) {
		cin>>A>>B;

		cout<<"Case #"<<i<<": ";
		count=0;
		for(int i =0;i<vfsq.size();i++) {
			if(vfsq[i]>=A && vfsq[i]<=B) {
				//cout << vfsq[i]<< "-";
				count++;
			}
		}
		cout << count;
		
		//cout << A << " " << B;

		cout<<endl;
	}

	return 0;
}
