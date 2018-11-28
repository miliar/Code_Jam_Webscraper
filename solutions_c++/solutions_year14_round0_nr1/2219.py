#include <fstream>
#include <vector>
using namespace std;

char filename[30] = "A-small-attempt0.in";
int main(){

	ifstream in(filename);
	ofstream out("1out");
	
	int casenum;
	in>>casenum;
	int firstcard[16];
	int secondcard[16];

	for(int i=0;i<casenum;i++){
		int first;
		in>>first;

		for(int j=0;j<16;j++)
			in>>firstcard[j];

		int second;
		in>>second;
	
		for(int j=0;j<16;j++)
			in>>secondcard[j];

		vector<int> answer;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++){
				if(firstcard[4*first-4+j] == secondcard[4*second-4+k])
					answer.push_back(firstcard[4*first-4+j]);
			}

		out<<"Case #"<<i+1<<": ";
		if(answer.size()==1)
			out<<answer[0];
		else if(answer.size()==0)
			out<<"Volunteer cheated!";
		else
			out<<"Bad magician!";

		out<<endl;
			

	}
}
