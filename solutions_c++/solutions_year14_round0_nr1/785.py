#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>

using namespace std;


ifstream in("A-small-attempt1.in");
ofstream out("output1.txt");
string s; // string to store the read lines
int temp;//integer to read the line integers using stringstream


void readData(int ch,vector<int> &v){
		for(int i=0 ; i<4 ; i++){ //loop to read the four lines matrix(cards)
			getline(in,s);
			if(i == ch-1){
				stringstream iss(s);
				while(iss>>temp){
					v.push_back(temp);
				}
			}
		}
}

int Compare(vector<int> v1,vector<int> v2 , int &r){
	int ret = 0;
	for(int i=0 ; i <4;i++)
		for(int j=0; j<4; j++){
			if(v1[i] == v2[j]){
				ret++;
				r = v1[i];
			}
		}
	return ret;
}
int main(){
	int ts =1;
	int t,ch1,ch2,result;//#of test cases ,choice1 , choice2
	in>>t;
	while(t--){
		vector<vector<int> > v(2);
		in>>ch1;//read the choice #1
		getline(in,s);//dummy getline to read the /n for the current line
		readData(ch1,v[0]);
		in>>ch2;//read the choice #1
		getline(in,s);//dummy getline to read the /n for the current line
		readData(ch2,v[1]);
		int ret = Compare(v[0],v[1],result);
		if(ret == 1){
			out<<"Case #"<< ts <<": "<<result<<endl;
		}else if(ret == 0){
			out<<"Case #"<< ts <<": Volunteer cheated!"<<endl;
		}else{
			out<<"Case #"<< ts <<": Bad magician!"<<endl;
		}
		ts++;
	}
	return 0;
}