#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>

#include <math.h>
#include <algorithm>
#include <stdio.h>
using namespace std;



int main()
{

	freopen("D://Source//C++//GCJ//GCJa//Debug//A-small-attempt0.in", "rt", stdin);
	freopen("D://Source//C++//GCJ//GCJa//Debug//output.txt", "wt", stdout);

	int testCases = 0;
	
	cin>>testCases;

	long long r = 0;
	long long t1 = 0;

	for (int t = 0; t < testCases; t++) {
		//for(int i = 0; i < 2; i++) {

		//}
		cin>>r;
		cin>>t1;

		long long whiteRaduis = r;
		long long ringRadius = 0;
		long long sum = 0;
		bool indicator = true;
		int counter = 0;

		while(indicator) {
			ringRadius = whiteRaduis + 1;
			long long area = ringRadius*ringRadius - whiteRaduis*whiteRaduis;
			whiteRaduis += 2;
			//ringRadius++;
			sum += area;
			if(sum > t1) {
				indicator = false;
			} else {
				
				counter++;
			}

		}

		r = 0;
		t1 = 0;

		cout<<"Case #"<<(t+1)<<": "<<counter<<endl;
		
	}

	fclose (stdin);
	fclose (stdout);

	return 0;
}