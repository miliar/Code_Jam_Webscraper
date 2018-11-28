// Q4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <list>
using namespace std;

int main()
{
    freopen("D://Practice//D-large.in", "r", stdin);
    freopen("D://Practice//D-large.out", "w", stdout);

	int numCase;
	cin >> numCase;
	for(int i=0; i<numCase; i++) {
		int ans1=0, ans2=0, n;
		double tmp;
		cin >> n;
		list<double> lst1, lst2;
		for(int j=0; j<n; j++){
			cin >> tmp;
			lst1.push_back(tmp);
		}
		for(int j=0; j<n; j++){
			cin >> tmp;
			lst2.push_back(tmp);
		}
		lst1.sort();
		lst2.sort();
		list<double> lst1_copy(lst1), lst2_copy(lst2);
		list<double>::iterator it1=lst1_copy.begin(), it2=lst2_copy.begin();
		while(it1!=lst1_copy.end() && it2!=lst2_copy.end()){
			if(*it1<=*it2) it1++;
			else{
				it1=lst1_copy.erase(it1);
				it2=lst2_copy.erase(it2);
				ans1++;
			}
		}
		
		it2=lst2.begin();
		for(it1=lst1.begin();it1!=lst1.end();it1++){
			while(it2!=lst2.end() && *it2 <= *it1) it2++;
			if(it2==lst2.end()) break;
			else{
				it2=lst2.erase(it2);
			}
		}
		while(it1!=lst1.end()) {
			ans2++;
			it1++;
		}
		cout << "Case #" << (i+1) << ": " << ans1 <<' '<< ans2 << endl;
	}

	return 0;
}