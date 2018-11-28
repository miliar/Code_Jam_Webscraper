#include <iostream>
#include <vector>
using namespace std;

template<typename T>
T read(){
	T temp;
	cin >> temp;
	return temp;
}

struct Concert{
	int smax;
	vector<int> people;
	
	Concert(){
		smax = read<int>();
		for( int i=0; i<smax+1; i++ )
			people.push_back( read<char>() - '0' );
	}
	
	int result(){
		int normal = 0, added = 0;
		
		for( int s=0; s<=smax; s++ ){
			auto p = people[s];
			auto total = normal + added;
			if( p > 0 && total < s )
				added += s - total;
			normal += p;
		}
		
		return added;
	};
};


int main(){
	auto amount = read<int>();
	
	for( int i=1; i<=amount; i++ )
		cout << "Case #" << i << ": " << Concert().result() << endl;
	
	return 0;
}
