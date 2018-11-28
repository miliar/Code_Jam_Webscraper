#include <fstream>
#include <iomanip>
#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

char filename[30]="D-large.in";

int main(int argc, char const *argv[])
{
	ifstream in(filename);
	ofstream out("4out");

	int casenum;
	in>>casenum;

	for(int i=0;i<casenum;i++){
		out<<"Case #"<<i+1<<": ";
		int blocknum;
		in>>blocknum;
		deque<double> A;
		deque<double> B;
		for(int j=0;j<blocknum;j++){
			double tmp;
			in>>tmp;
			A.push_back(tmp);
		}

		for(int j=0;j<blocknum;j++){
			double tmp;
			in>>tmp;
			B.push_back(tmp);
		}
			
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());

		deque<double> Atwo(A);
		deque<double> Btwo(B);

		int score=0;

		while(A.size()!=0){
			if(A[0]>B[0]){
				score++;
				A.pop_front();
				B.pop_front();
			}
			else{
				A.pop_front();
				B.pop_back();
			}
		}

		out<<score<<" ";

		score=0;
		for(int j=0;j<Atwo.size();j++){
			auto  it = find_if(Btwo.begin(),Btwo.end(),[=](double b)->bool{
				return b > Atwo[j];
			});

			if(it==Btwo.end()){
				score++;
				Btwo.pop_front();
			}
			else{
				Btwo.erase(it);
			}
		}

		out<<score<<endl;
	}
}