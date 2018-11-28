#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

char filename[30]="A-small-attempt00.in";

class game{
public:
	char zimu;
	int time;
};
int main(int argc, char const *argv[])
{
	ifstream in(filename);
	ofstream out("bb22");

	int casenum;
	in>>casenum;
	

	for(int i=0;i<casenum;i++){
		out<<"Case #"<<i+1<<": ";
		//cout<<"Case #"<<i+1<<": ";
		string first,second;
		int n;
		in>>n>>first>>second;

		char previous = '-';
		vector<game> first_;
		for(int i=0;i<first.size();){
			previous = first[i];
			game tmp;
			tmp.zimu = previous;
			tmp.time=0;
			while(i<first.size() && first[i]==previous){
				tmp.time++;
				i++;
			}
			first_.push_back(tmp);
		}
		
		vector<game> second_;
		for(int i=0;i<second.size();){
			previous = second[i];
			game tmp;
			tmp.zimu = previous;
			tmp.time=0;
			while(i<second.size() && second[i]==previous){
				tmp.time++;
				i++;
			}
			second_.push_back(tmp);
		}

		if(first_.size()!=second_.size()){
			out<<"Fegla Won"<<endl;
			continue;
		}

		bool flag = false;
		int cnt=0;
		for(int i=0;i<first_.size();i++){
			if(first_[i].zimu != second_[i].zimu){
				flag =true;
				break;
			}
			else
				cnt += abs(first_[i].time - second_[i].time);
		}

		if(flag)
			out<<"Fegla Won"<<endl;
		else
			out<<cnt<<endl;
	}


	return 0;
}