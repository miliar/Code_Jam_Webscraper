#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int i,j, k,l;
	int N, T;
	cin>>T;
	string a;
    std::vector<char>::iterator it;

	for(l = 0 ; l < T ; l++){
		cout<<"Case #"<<l+1<<": ";
		cin>>a;
		vector<char> letters;
		letters.push_back(a[0]);
		for(i = 1 ; i < a.length() ; i++)
		{
			 it = letters.begin();
			if(letters[0] <= a[i])
				letters.insert(it, a[i]);
			else
				letters.push_back(a[i]);
		}
		for(i = 0 ; i < a.length() ; i++)
			cout<<letters[i];
		cout<<"\n";
	}
	return 0;
}
