#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
bool myfunction (int i,int j) { return (i==j); }

int main() {
	int t,r1,r2,val,i,j,count,n,v;
	ifstream myin;
	myin.open("A-small-attempt2.in");
	ofstream myout;
	myout.open("output.out");

	std::vector<std::vector<int> > a(4),b(4);

	myin>>t;
	n=1;
	while(n<=t) {
		myin>>r1;
		for(i=0;i<4;i++) {
			a[i].resize(4);
			for(j=0;j<4;j++) {
				myin>>val;
				a.at(i)[j] = val;
			}
		}
		myin>>r2;
		for(i=0;i<4;i++) {
			b[i].resize(4);
			for(j=0;j<4;j++) {
				myin>>val;
				b.at(i)[j] = val;
			}
		}
		count=0;
		for(i=0;i<4;i++) {
			val = a[r1-1].at(i);
			for(j=0;j<4;j++) {
				if(myfunction(val,b[r2-1].at(j))) {
					count++;
					v = val;
				}
			}
		}

		if(count == 0) myout<<"Case #"<<n<<": Volunteer cheated!\n";
		else if (count==1)
		{
			myout<<"Case #"<<n<<": "<<v<<"\n";
		}
		else
			myout<<"Case #"<<n<<": Bad magician!\n";

		n++;
	}

	myin.close();
	myout.close();
	
	return 0;
}