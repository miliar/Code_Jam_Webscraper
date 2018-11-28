#include <iostream>
#include <string>
//YOLO
//code by loyolman

using namespace std;

int T;

int main() {
	cin>>T;
	for (int j=0;j<T;j++){
		int Smax,PeopleUp,Friends;
		string s;
		
		PeopleUp=0;
		Friends=0;
		cin>>Smax;
		cin>>s;
		
		for (int i=0;i<s.size();i++){
			if (i>PeopleUp) {
				Friends+=i-PeopleUp;
				PeopleUp=i;
			} 
			PeopleUp+=((int)s[i]-48);//(int)'0'=48
		}
		cout<<"Case #"<<j+1<<": "<<Friends<<endl;
	}
	return 0;
}
