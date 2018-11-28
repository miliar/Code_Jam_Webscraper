#include <iostream>;
#include <fstream>;

using namespace std;

ifstream infile;
ofstream outfile;

int n,k;
int a[4][4];
int b[4][4];
int ans,ans1,ans2;
bool flag;

void read() {

	infile>>ans1;
	ans1--;
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++) 
			infile>>a[i][j];

	infile>>ans2;
	ans2--;
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++) 
			infile>>b[i][j];

}

void calculate() {

	ans=-1;
	outfile<<"Case #"<<k+1<<": ";

	for (int i=0; i<4; i++) {

		flag=false;
		for (int j=0; j<4; j++) 
			if (a[ans1][i]==b[ans2][j]) {flag=true;}
		if (flag) {
			if (ans==-1) {ans=a[ans1][i];} else {outfile<<"Bad magician!"<<endl;return;}
		}
		
	}

	if (ans==-1) {outfile<<"Volunteer cheated!"<<endl;} else {outfile<<ans<<endl;}

}


int main() {

	infile.open("input.txt");
	outfile.open("output.txt");

	infile>>n;

	for (k=0; k<n; k++) {
		read();
		calculate();
	}

}