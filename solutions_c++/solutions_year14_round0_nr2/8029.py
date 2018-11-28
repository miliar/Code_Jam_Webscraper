# include <fstream>
# include <iostream>
using namespace std;

double c, f, x, t1, t2;

int main()
{
	int T;
	
	ifstream fin ("f.in");
	freopen("f.out", "w", stdout);
	
	fin>>T;
	double q;
	for(int t=1;t<=T;++t) {
		fin>>c>>f>>x;
		
		q=2;
		t1=x/q;
		t2=0;

		while(t2 + c/(q) + x/(q+f) < t1) {
			t1 = t2 + c/q + x/(q+f);
			t2 += c/q;
			q+=f;
		}

		printf("Case #%d: %.7lf\n", t, t1);
	}
	
	return 0;
}

		
