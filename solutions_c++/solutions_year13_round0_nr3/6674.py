/*
 * C.cpp
 *
 *  Created on: ??þ/??þ/????
 *      Author: AhmedKamal
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
vector<int> squares ;
bool isPlandrioum(int x){

	if(x<10) return true;
	else if(x < 100){
		if(x == 10)
			return false;
		else if(x%11 == 0)
			return true;

		else return false;

	}

	else if(x < 1000){
		stringstream ss;
		string num;
		ss << x;
		num = ss.str();
		if(num[0] == num[2]) return true;

		else return false;
	}
	else return false;

}
int main(){
freopen("C-small-attempt0.in","rt",stdin);
freopen ("c.out","w",stdout);

for(int i=1; i*i<=1000; i++){
	if(isPlandrioum(i*i) && isPlandrioum(i)){
	//	cout << i*i <<" "<< i <<endl;
		squares.push_back(i*i);
	}

}
int k;
/*REP(k , squares.size()){
	cout << squares[k]<<endl;

}*/
int t;
cin >> t;
int n =1;
while(n <= t){
int count =0;
int A , B ;
cin >> A >> B;
for(int k=0; k<squares.size(); k++){
	if(squares[k] >= A && squares[k] <= B){
		//cout << squares[k]<<endl;
		count++;
	}


}
cout <<"Case #"<<n<<": "<<count<<endl;
n++;
}
return 0;
}
