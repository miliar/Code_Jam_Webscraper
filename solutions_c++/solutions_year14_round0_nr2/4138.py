#include <iostream>

using namespace std;

int main() {
	int T,n=1;
	cin>>T;
	while(n<=T) {
		double t=0.0, cr=2.0, c, f, x;
		bool b = true;
		cin>>c>>f>>x;
		while(b) {
			if((x/cr)<(c/cr+x/(cr+f))) {
				t+= x/cr; b=false;
			} else {
				t+= c/cr;
				cr = cr+f;
			}
		}

		cout<<"Case #"<<n<<": ";
		printf("%.7f\n",t);
		n++;
	}
	return 0;
}