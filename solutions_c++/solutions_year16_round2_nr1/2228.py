#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

string letters[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"},s;
vector<int> number;

void find(char c,int index){
	if (s.find(c)!=string::npos){
		for (int i=0;i<letters[index].size();i++){
			s.erase(s.find(letters[index][i]),1);
		}
		number.push_back(index);
	}
	if (s.find(c)!=string::npos) find(c,index);
}


int main(){
	int TC;
	cin>>TC;
	for (int t=1;t<=TC;t++){
		cin>>s;
		find('Z',0);
		find('W',2); 
		find('U',4); 
		find('X',6);
		find('R',3);
		find('F',5);
		find('V',7);
		find('O',1);
		find('G',8);
		find('I',9);
		sort(number.begin(),number.end());
		cout<<"Case #"<<t<<": ";
		for (int i=0;i<number.size();i++) cout<<number[i];
		cout<<endl;
		number.clear();
	}
}