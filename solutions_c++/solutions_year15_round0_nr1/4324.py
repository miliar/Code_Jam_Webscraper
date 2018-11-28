#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{


	int T;
	cin>>T;
	for(int t = 1; t<= T;t++){
		int Smax;
		//shyness[1000];
		string shyness;
		cin>>Smax;
		cin>>shyness;
		int standing = shyness[0] - '0';
		int need = 0;
		for(int s = 1; s<=Smax;s++){
			if(s <= standing)
				standing+=(shyness[s]-'0');
			else
			{
				need += s- standing;
				standing =(shyness[s]-'0') + (s-standing ) + standing;
			}
			//shyness[s]=tmp[s] - '0';

			//cout<<shyness[s]<<endl;
		}
		cout<<"Case #"<<t<<": "<<need<<endl;
		
	}
	return 0;
}