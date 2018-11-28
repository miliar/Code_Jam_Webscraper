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
#include <stdio.h>
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;

int main() {
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("z.txt","w",stdout);
	int cases,ii=0;
	cin>>cases;
	while(cases--){
		int num1,num2,s,cont=0;
		cin >> num1;
		map <long int,long int> mymap;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(i==num1-1){
					cin >> s;
					mymap[s]++;
				} else {
					cin >> s;
				}
			}
		}
		cin >> num2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(i==num2-1){
					cin >> s;
					mymap[s]++;
					if(mymap[s]>1){
						cont++;
					}
				} else {
					cin >> s;
				}
			}
		}
		cout << "Case #"<<++ii<<": ";
		if(cont==0){
			cout << "Volunteer cheated!\n";
		}
		if(cont>1){
			cout << "Bad magician!\n";
		}
		if(cont==1){
			for(map<long int,long int>::iterator it=mymap.begin();it!=mymap.end();it++){
				if(it->second>1){
					cout << it->first << endl;
				}
			}
		}
	}
	return 0;
}
