#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int cs=1;cs<=t;cs++){
		cout<<"Case #"<<cs<<": ";
		int ln,val;
		vector<int> vec1, vec2;
		cin>>ln; ln--;
		int cln = 0;
		for( int i=0; i < 16; i++){
			cin>>val;
			if( i/4 == ln ){
				vec1.push_back(val);
			}
		}
		cln=0;
		cin>>ln; ln--;
		for( int i=0; i < 16; i++){
			cin>>val;
			if( i/4 == ln ){
				vec2.push_back(val);
			}
		}
		vector<int> res(8);
		sort( vec1.begin(), vec1.end());
		sort( vec2.begin(), vec2.end());
		res.resize( set_intersection( vec1.begin(), vec1.end(), vec2.begin(), vec2.end(), res.begin() ) - res.begin());		
		if( res.size() == 0 )cout<<"Volunteer cheated!"<<endl;
		if( res.size() > 1 )cout<<"Bad magician!"<<endl;
		if( res.size() == 1 )cout<< res[0] <<endl;			
	}
	return 0;
}


