#include <iostream>
#include <string>
#include <math.h>
#include <bitset>
#include <algorithm>
#include <list>
using namespace std;

int main(){
	int input;
	string j;
	size_t sze=0;
	list<string> mylist;

	cin>>input;
for (int i = 1; i <= input; ++i)
{	cout<<"Case #"<<i<<": ";
	cin>>j;
	sze=j.size();
	string substr ="";
	substr+=j[0];
	for(int k=1;k<sze;k++){
		if(substr[0]==j[k]){
			substr=j[k]+substr;

		}
		else if(substr[0]>j[k]){
			substr=substr+j[k];

		}else if(substr[0]<j[k])
			substr= j[k]+substr;

	}
	cout<<substr<<endl;
	
}

return 0;
}
