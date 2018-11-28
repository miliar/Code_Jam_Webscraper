#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
	int t; cin>>t;
	string S;

	for (int i=1; i<=t; ++i){
		cin>>S;
		vector<int> A;

		size_t found;
		
		found = S.find("Z");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);
			found = S.find("R");
			S.erase(found,1);
			found = S.find("O");
			S.erase(found,1);

			A.push_back(0);

			found = S.find("Z");
		}

		found = S.find("W");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("T");
			S.erase(found,1);
			found = S.find("O");
			S.erase(found,1);

			A.push_back(2);

			found = S.find("W");
		}

		found = S.find("U");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("F");
			S.erase(found,1);
			found = S.find("O");
			S.erase(found,1);
			found = S.find("R");
			S.erase(found,1);

			A.push_back(4);

			found = S.find("U");
		}

		found = S.find("X");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("I");
			S.erase(found,1);
			found = S.find("S");
			S.erase(found,1);

			A.push_back(6);

			found = S.find("X");
		}

		found = S.find("G");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);
			found = S.find("I");
			S.erase(found,1);
			found = S.find("H");
			S.erase(found,1);
			found = S.find("T");
			S.erase(found,1);

			A.push_back(8);

			found = S.find("G");
		}

		found = S.find("S");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);
			found = S.find("V");
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);
			found = S.find("N");
			S.erase(found,1);

			A.push_back(7);

			found = S.find("S");
		}

		found = S.find("V");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("F");
			S.erase(found,1);
			found = S.find("I");
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);

			A.push_back(5);

			found = S.find("V");
		}

		found = S.find("T");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("H");
			S.erase(found,1);
			found = S.find("R");
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);

			A.push_back(3);

			found = S.find("T");
		}

		found = S.find("O");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("N");
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);

			A.push_back(1);

			found = S.find("O");
		}

		found = S.find("N");
		while(found!=std::string::npos){
			S.erase(found,1);
			found = S.find("I");
			S.erase(found,1);
			found = S.find("N");
			S.erase(found,1);
			found = S.find("E");
			S.erase(found,1);

			A.push_back(9);

			found = S.find("N");
		}

		sort(A.begin(), A.end());
		cout<<"Case #"<<i<<": ";
		for (int i=0; i<A.size(); ++i){
			cout<<A[i];
		}
		cout<<endl;
	}

	return 0;
}