#include <iostream>
#include <fstream>
#include <set>
using namespace std;
ifstream fin("A-small-attempt1.in");

void process(int t){
	set<int> S1;
	set<int> S2;
	int r1,r2;
	fin>>r1;
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++){
			int c;
			fin>>c;
			if(i==r1)
				S1.insert(c);

		}
	fin>>r2;
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++){
			int c;
			fin>>c;
			if(i==r2)
				S2.insert(c);
		}
	 int count = 0;
	 int card = 0;
	 for (set<int>::iterator it=S1.begin(); it!=S1.end(); ++it){
		 if(S2.find(*it)!=S2.end()){
			 card = *it;
	    	count++;
		 }
	 }
	 cout<<"Case #"<<t<<": ";
	 if(count==1)
		 cout<<card<<endl;
	 else if(count>1)
		 cout<<"Bad magician!"<<endl;
	 else
		 cout<<"Volunteer cheated!"<<endl;

}

int main() {
	int T;
	fin>>T;
	for(int i = 1;i<=T;i++)
		process(i);

	return 0;
}
