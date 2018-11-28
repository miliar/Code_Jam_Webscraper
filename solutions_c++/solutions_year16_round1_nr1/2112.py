// Jai Mata Di
#include <iostream>
using namespace std;
class MaxSortedListGenerator{
	string s;
public:
	void input(){
		cin>>s;
	}
	string findMaxSorted(){
		string output="";
		for(int i=0;i<s.size();i++){
			if(output.size() == 0){
				output.push_back(s[i]);
				//cout<<"1 ";
			}else if(s[i] >= output[0]){
				string z="";
				z.push_back(s[i]);
				output.insert(0,z);
				//cout<<"2 ";
			}else{
				output.push_back(s[i]);
				//cout<<"3 ";
			}
			//cout<<"output = "<<output<<endl;
		}
		return output;
	}
};
int main() {
	int noOfTestCases=0;
	cin>>noOfTestCases;
	for(int testCaseNo=1;testCaseNo <= noOfTestCases;testCaseNo++){
		MaxSortedListGenerator g;
		g.input();
		cout<<"Case #"<<testCaseNo<<": "<<g.findMaxSorted()<<endl;
	}
	return 0;
}
