#include <iostream>
#include <string>
#include <list>
using namespace std;

int T;
string raw;
list<char> now;
list<char>::iterator it;

int main() {
	#ifdef ONLINE_JUDGE
	
	#else
		freopen("A.in","r",stdin);
		freopen("A.out","w",stdout);
	#endif
	cin>>T;
	for (int ii=1; ii<=T; ii++) {
		cin>>raw;
		now.clear();
		now.push_back(raw[0]);
		it=now.begin();
		for (int i=1; i<raw.size(); i++) {
			if (raw[i]<*now.begin()) 
				now.push_back(raw[i]);
			else 
				now.push_front(raw[i]);
		}
		cout<<"Case #"<<ii<<": ";
		for (it=now.begin(); it!=now.end(); it++) cout<<*it;
		cout<<endl;
	}
} 
