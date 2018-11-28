#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include "stdlib.h"
#include "stdio.h"
#include <sstream>
#include <ttmath/ttmath.h>
#include <fstream>
//http://www.ttmath.org/download ttmath library download link
using namespace std;
bool isPal(string str){
	string str2=str;
	reverse(str2.begin(),str2.end());
	if(str.compare(str2)==0)return true;

	return false;
}
bool isSquare(int n){
	double sqr = sqrt(n);
	int isqr=(int)sqr;
	if(sqr-isqr!=0)return false;
	return true;
}
string inttostr(ttmath::Int<15> n){
	string str;
	stringstream ss;
	ss<<n;
	
	str=ss.str();
	return str;
}

int main(){
	int T,i,j;
	int counter;
	char buffer[100];
	ttmath::Int<15>A;
	ttmath::Int<15>B;
	vector<ttmath::Int<15> > hashedData;
	ifstream infile("list");
	string tmp;
	while (getline(infile, tmp))
	{
		ttmath::Int<15>temp;
		istringstream iss(tmp);
		iss>>temp;
		hashedData.push_back(temp);

	}
	cin>>T;
	for(i=0;i<T;i++){
		cin>>A>>B;
		counter=0;	
		for(j=0;j<hashedData.size();j++){
			if(hashedData[j]>=A&&hashedData[j]<=B){
				counter++;

			}
		}
		cout<<"Case #"<<i+1<<": "<<counter<<endl;
	}
	return 0;
}
//the file list contains the following data:
/*1
4
9
121
484
10201
12321
14641
40804
44944
1002001
1234321
4008004
100020001
102030201
104060401
121242121
123454321
125686521
400080004
404090404
10000200001
10221412201
12102420121
12345654321
40000800004
1000002000001
1002003002001
1004006004001
1020304030201
1022325232201
1024348434201
1210024200121
1212225222121
1214428244121
1232346432321
1234567654321
4000008000004
4004009004004
100000020000001
100220141022001
102012040210201
102234363432201
121000242000121
121242363242121
123212464212321
123456787654321
400000080000004
10000000200000001
10002000300020001
10004000600040001
10020210401202001
10022212521222001
10024214841242001
10201020402010201
10203040504030201
10205060806050201
10221432623412201
10223454745432201
12100002420000121
12102202520220121
12104402820440121
12122232623222121
12124434743442121
12321024642012321
12323244744232321
12343456865434321
12345678987654321
40000000800000004
40004000900040004
*/
