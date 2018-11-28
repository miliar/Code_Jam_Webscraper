#include <iostream>

int main(int argc, char** argv) {
int c;
using namespace std;
cin>>c;
int t=1;
while(c--) {
	int l;
	cin>>l;
	string s;
	cin>>s;
	int su=0,r=0,k=0;
	for (int i=0; i<l+1;++i) {
		string n;
		n.push_back(s[i]);
		int val = atoi(n.c_str());
	if (k > su){
			su++;
			r++;
		}
//		cout << su << " " << k << " " << r <<  endl;
	
		su += val;
		++k;
	}
	cout << "Case #" << t++ << ": " << r << endl; 

}

return 0;
}
