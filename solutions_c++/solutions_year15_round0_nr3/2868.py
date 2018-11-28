// Jai Mata Di
#include <iostream>
#include <vector>
using namespace std;
class Quaternion;
vector< vector <Quaternion> > lookupTable;
class Quaternion{
	public:
	bool isNegativeSign;
	unsigned char index;
	Quaternion(unsigned char index, bool isNegativeSign){
		this->index = index;
		this->isNegativeSign = isNegativeSign;
	}
	void print(){
		if (isNegativeSign == true){
			cout<<"-";
		}else{
			cout<<"+";
		}
		if(index == 0){
			cout<<"1";
		}else if (index == 1){
			cout<<"i";
		}else if (index == 2){
			cout<<"j";
		}else if (index == 3){
			cout<<"k";
		}
		cout<<endl;
	}
	void multiplyWith(unsigned char c){
		unsigned char newIndex = lookupTable[this->index][c].index;
		if (lookupTable[this->index][c].isNegativeSign == true){
			//cout<<"negate"<<endl;
			this->isNegativeSign = !this->isNegativeSign;
		}else{
			//cout<<"no negate"<<endl;
		}
		this->index = newIndex;
	}
};
class QuaternionPatternTester{
	vector<unsigned char> inputPattern;
	int lengthOfPattern;
	int noOfTimes;
	public:
	void input(){
		cin>>lengthOfPattern>>noOfTimes;
		char c;
		for(int i=0;i<lengthOfPattern;i++){
			cin>>c;
			inputPattern.push_back((unsigned char)(c - 'h'));
		}
	}
	void print(){
		cout<<"Printing:"<<lengthOfPattern<<" x "<<noOfTimes<<"=";
		for(int i=0;i<lengthOfPattern;i++){
			if (inputPattern[i] == 1){
				cout<<"1";
			}else if (inputPattern[i] == 2){
				cout<<"2";
			}else if (inputPattern[i] == 3){
				cout<<"3";
			}
			cout<<" ";
		}
		cout<<endl;
	}
	bool isPossible(){
		Quaternion q(0,false);
		//q.print();
		unsigned char lookingFor = 1;
		for(int i=0; i<noOfTimes; i++){
			for(int j=0; j<lengthOfPattern; j++){
				unsigned char c = inputPattern[j];
				/*cout<<"input = ";
				if ( c == 0){
					cout<<"0";
				}else if (c == 1){
					cout<<"1";
				}else if (c == 2){
					cout<<"2";
				}else if (c == 3){
					cout<<"3";
				}
				cout<<endl;*/
				q.multiplyWith(c);
				//q.print();
				if (q.index == lookingFor && q.isNegativeSign == false){
					//cout<<"lookingFor"<<lookingFor<<endl;
					lookingFor++;
					q.index = 0;
					q.isNegativeSign = false;
				}
			}
		}
		//cout<<"Final q=";
		//q.print();
		if(lookingFor == 4 && q.index == 0 && q.isNegativeSign == false){
			return true;
		}else{
			return false;
		}
	}
};
void populateLookupTable(){
	Quaternion plus_one(0,false);
	Quaternion minus_one(0,true);
	Quaternion plus_i(1,false);
	Quaternion minus_i(1,true);
	Quaternion plus_j(2,false);
	Quaternion minus_j(2,true);
	Quaternion plus_k(3,false);
	Quaternion minus_k(3,true);
	
	vector <Quaternion> v;
	v.push_back(plus_one);
	v.push_back(plus_i);
	v.push_back(plus_j);
	v.push_back(plus_k);
	lookupTable.push_back(v);
	v.clear();
	
	v.push_back(plus_i);
	v.push_back(minus_one);
	v.push_back(plus_k);
	v.push_back(minus_j);
	lookupTable.push_back(v);
	v.clear();
	
	v.push_back(plus_j);
	v.push_back(minus_k);
	v.push_back(minus_one);
	v.push_back(plus_i);
	lookupTable.push_back(v);
	v.clear();
	
	v.push_back(plus_k);
	v.push_back(plus_j);
	v.push_back(minus_i);
	v.push_back(minus_one);
	lookupTable.push_back(v);
	v.clear();
}
void printLookupTable(){
	for(int i=0;i<lookupTable.size();i++){
		for(int j=0;j<lookupTable[i].size();j++){
			lookupTable[i][j].print();
		}
		cout<<endl;
	}
}
int main() {
	populateLookupTable();
	//printLookupTable();
	int noOfTestCases = 0;
	cin>>noOfTestCases;
	for(int testCaseNo = 1; testCaseNo <= noOfTestCases; testCaseNo++){
		QuaternionPatternTester quaternionPatternTester;
		quaternionPatternTester.input();
		//quaternionPatternTester.print();
		cout<<"Case #"<<testCaseNo<<": ";
		if(quaternionPatternTester.isPossible()){
			cout<<"YES";
		}else{
			cout<<"NO";
		}
		cout<<endl;
	}
	return 0;
}
