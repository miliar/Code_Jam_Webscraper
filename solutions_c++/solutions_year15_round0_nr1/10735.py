// Hager Radi, Small A , Source code
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;
string level;
int Smax;
int Get_min()
{
//	if(id==0)	return 0;
	int Friend=0;
	int Acc = level[0]-48;
	for(int i=1 ; i<= Smax ; i++)
	{
		if(Acc < i){
			Friend += (i-Acc);
			Acc += (i-Acc);
		}
		Acc += (level[i]-48);
	}
	return Friend;
}
int main() {
	int T;
	cin>>T;
	for(int i=1 ; i<=T ; i++)
	{
		cin>>Smax;
		cin>>level;
		cout<<"Case #"<<i<<": "<<Get_min()<<endl;
	}
	return 0;
}