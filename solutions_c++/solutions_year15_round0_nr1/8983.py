#include<iostream>

using namespace std;

int main(){
	int T, Smax, invite, sum, s;
	char tmp;
	cin>>T;
	for (int ii=1; ii<=T; ii++) {
		cin>>Smax;
		invite=0; sum=0;
		for (int jj=0; jj<=Smax; jj++) {
			cin>>tmp;
			s=tmp-char('0');
			if (jj>sum) {
				int diff=jj-sum;
				invite+=diff;
				sum=sum+s+diff;
			}
			else sum+=s;
		}
		cout<<"Case #"<<ii<<": "<<invite<<endl;
	}
}