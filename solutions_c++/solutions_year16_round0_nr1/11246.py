/*************************************************************************
	> File Name: A.cpp
	> Author: csy
	> Mail: chshaoyi7@gmail.com 
	> Created Time: 2016年04月10日 星期日 09时23分31秒
 ************************************************************************/

#include<iostream>
#include <fstream>
#include<set>
using namespace std;


int main(){

	ifstream fin("large-A.in");
	ofstream fout("large-A.out");
	
	long long int t, n;
	
	cin >> t;
	for(int j=1; j<=t ; j++){
		cin >> n;
		set<long long int> numbers;
		set<long long int> digits;
		long long int i = 1, next;

		cout << "Case #"<< j << ": ";
		while(true){
			next = i*n;
			if(numbers.cind(next)!=numbers.end()){
				cout << "INSOMNIA" << endl;
				break;
			}else{
				if(next==0) {
					digits.insert(0);
				}else{
					while(next!=0){
						digits.insert(next%10);
						next /= 10;
					}
					if(digits.size()==10){
						cout << i*n << endl;
						break;
					}
				}
				numbers.insert(i*n);
			}
			i ++;
		}

	}
}
