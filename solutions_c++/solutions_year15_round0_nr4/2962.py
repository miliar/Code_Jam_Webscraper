#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <cmath>
#include <cstdio>
#include <map>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t = 1; t <= T; ++t) {
		int X,R,C;
		cin>>X>>R>>C;
		if((R*C)%X !=0){
			cout<<"Case #"<<t<<": "<<"RICHARD"<<endl;
		} else if(X == 1 || X == 2) {
			cout<<"Case #"<<t<<": "<<"GABRIEL"<<endl;
		} else if(X == 3) {
			if((R*C)/X == 1) {
			cout<<"Case #"<<t<<": "<<"RICHARD"<<endl;
			} else {
			cout<<"Case #"<<t<<": "<<"GABRIEL"<<endl;
			}
		} else {
			if((R*C)/X == 1) {
			cout<<"Case #"<<t<<": "<<"RICHARD"<<endl;
			} else if((R*C)/X == 2) {

			cout<<"Case #"<<t<<": "<<"RICHARD"<<endl;
			} else {
				cout<<"Case #"<<t<<": "<<"GABRIEL"<<endl;
			}
		}
	}
}
