
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool in1(int a, vector<int> &v){
	for(int i=0;i<v.size();i++){
		if(v[i]==a){
			return true;
		}
	}
	return false;
}


int main() {
	int T;
	ifstream fin("A-small-attempt0.in");
	cin>>T;
	ofstream fout("out.txt");
	for(int i=0;i<T;i++){
		int choice1;
		cin>>choice1;
		vector<int> possible1;
		int in;
		choice1--;
		for(int q=0;q<4;q++){
			for(int w=0;w<4;w++){
				cin>>in;
				if(choice1==q){
					possible1.push_back(in);
				}
			}
		}

		int choice2;
		cin>>choice2;
		vector<int> possible2;
		choice2--;
		for(int q=0;q<4;q++){
			for(int w=0;w<4;w++){
				cin>>in;
				if(choice2==q){
					possible2.push_back(in);
				}
			}
		}
		vector<int> ans;
		//cout<<"!"<<endl;
		for(int b=0;b<possible1.size();b++){
			int qq=possible1[b];
			if(in1(qq,possible2)){
				int q=possible1[b];
				ans.push_back(q);
			}
		}
		string s;
		bool c=false;
		if(ans.size()>1){
			s="Bad magician!";
			c=true;
		}
		if(ans.size()<1){
			s="Volunteer cheated!";
			c=true;
		}

		if(c){
			cout<<"Case #"<<(i+1)<<": "<<s<<endl;
			fout<<"Case #"<<(i+1)<<": "<<s<<endl;
		}else{
			int q=ans[0];
			cout<<"Case #"<<(i+1)<<": "<<q<<endl;
			fout<<"Case #"<<(i+1)<<": "<<s<<endl;
		}

	}
	return 0;
}
