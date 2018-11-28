#include <iostream>
#include <map>
#include <string>
#include <sstream>
using namespace std;

bool helper(map<int, bool> mymap){
	for(int i = 0; i<10; i++){
		if (mymap[i] == false){
			return false;
		}
	}
	return true;
}

int main(){
	int numTest;
	string s;
	getline(cin,s);
	stringstream ss(s);
	ss >> numTest;
	int testNum = 1;

	while (testNum <= numTest){
		getline(cin, s);
		stringstream sss(s);
		int n;
		sss>>n;
		cout << "Case #"<<testNum<<": ";
		if(n == 0){
			cout<<"INSOMNIA"<<endl;
		} else {
			int og = n;
			map<int,bool> mymap;
			for(int i = 0; i<10 ; i++){
				mymap[i] = false;
			}
			while(true){
				int temp = n;
				while(true){
					mymap[temp%10] = true;
					if(temp /10 == 0){
						break;
					} else {
						temp = temp / 10;
					}
				}
				if(helper(mymap)){
					break;
				} else {
					n = n+og;
				}
			}
			cout<<n<<endl;
		}
		testNum++;
	}
}