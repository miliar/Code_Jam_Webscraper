#include <iostream>
#include <cmath>
#include <sstream>
#include <string>


using namespace std;


bool palin(int l)
{
	int Number;
	Number = l;

//	string String = static_cast<ostringstream*>( &(ostringstream() << Number) )->str();
	int j;
	string String = "";
	while (l) {
		String += (l % 10 + '0');
		l = l / 10;
	}
	for(int i = 0, j = (String.size() - 1); i <= (String.size()/2); i++,--j){
		if(String[i] != String[j]) {
			return false;
		}
	}
	return true;
}

int main()
{
	int t;
	cin >> t;

	//cin >> a >> b;
	int min, max;
	min = 2;
	int c = 0;
	int l = 1;

//	max = 4;
	for(int xi = 0; xi < t; xi++) {
        int a, b;
		cin >> a >> b;
//		cout <<"a = "<<a <<" b =" <<b<<endl;
		if(a == 1){
			c = 1;
		} else {
			c = 0;
		}
		min = 2;
		while((min* min) <= b){
//			cout<<min*min<<endl;

			int k = min*min;
			if(k >= a) {
			if(palin(k)){
				float m = sqrt(k);
//				cout<<"m = "<<m<<endl;
				if(palin(m)){
					c++;
				}
			}

		}
		min++;

	}
		cout <<"Case #"<<l<<": "<<c<<endl;
		l++;
	}


}
