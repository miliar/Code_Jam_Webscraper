#include <iostream>
#include <fstream>
#include <conio.h>
#include <cstdlib>

using namespace std;

unsigned long long pals[]={
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004};

int npals=39;
unsigned long long A,B;

int main(){
	//ifstream cin("C-large-1.in");
	ofstream out("out.txt");
	int T; cin>>T;
	
	for (int t=1; t<=T; t++){
		out<<"Case #"<<t<<": ";
		cin>>A>>B;
		
		int n=0;
		for (int i=0; i<npals; i++){
			if (pals[i]>=A && pals[i]<=B)n++;
		}
		out<<n<<"\n";
	}
	
	return 0;
}
