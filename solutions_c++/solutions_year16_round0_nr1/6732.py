#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(){
	int c,n, l, aux, s=1; //case, number, length, step
	char vs[]= {'0','1','2','3','4','5','6','7','8','9'}; //vector set
    	set<char> s1 (vs,vs+10);
	set<char> nums;
	pair<set<int>::iterator,bool> pair;
	string str;
	while(cin >> c){
		for(int i=0;i<c;i++){
			cin >> n;
			if(n==0){
				cout << "Case #"<< i+1<<": INSOMNIA"<< endl;
			} else{
				while(s1 != nums){
					aux= n*s;
					str = to_string(aux);
					for(int j=0;j<str.size();j++)
						nums.insert(str[j]);
					s++;
				}

				cout << "Case #"<< i+1<<": "<< aux << endl;
				// reset variables
				nums.clear();
				s = 1;
			}
		}
	}
	return 0;
}