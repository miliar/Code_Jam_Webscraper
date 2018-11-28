#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
 	int test;
	cin >> test;
	for(int i=1;i<test+1;i++){
		int n,count1,count=0;
		cin >> n;
		string s1;
		cin >> s1;
		count1 =  (s1[0]-'0');
		//cout << count1 << endl;		
		for(int j=1;j<n+1;j++){
			//cout << count1 << endl;
			if(count1>=j){
				count1 = count1+(s1[j]-'0');
				continue;
			}
			else{
				count = count +(j-count1);
				count1 = j + (s1[j]-'0');
			}
		}
		cout << "Case #" << i <<": " << count << endl;
	}
	 return 0;
}
				
			


