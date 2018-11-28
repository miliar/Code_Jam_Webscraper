#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>
#include <cstdlib>

using namespace std;


int main() {
	int cases=0;
	cin >> cases;
	for(int casesIter=0;casesIter<cases;casesIter++) {
		int first;
		cin>>first;
		int try1[4][4];
		for(int i=0;i<4;i++) {
			scanf("%d %d %d %d\n", &try1[i][0], &try1[i][1], &try1[i][2], &try1[i][3]);
		}
		int second;
		cin>>second;
		int try2[4][4];
		for(int i=0;i<4;i++) {
			scanf("%d %d %d %d\n", &try2[i][0], &try2[i][1], &try2[i][2], &try2[i][3]);
		}
		
		std::set<int> target;
		for(int i=0;i<4;i++) {
			target.insert(try1[first-1][i]);
		}
		int num_dup=0;
		std::pair<std::set<int>::iterator,bool> ret;
		std::set<int>::iterator it;
		
		for(int i=0;i<4;i++) {	
			ret = target.insert(try2[second-1][i]);
			if(ret.second == false) {
				num_dup++;
				it = ret.first;
			}
		}
		
		if(num_dup>1) {
			cout<<"Case #"<<casesIter+1<<": Bad Magician!"<<endl;
		} else if (num_dup==0) {
			cout<<"Case #"<<casesIter+1<<": Volunteer cheated!"<<endl;
		} else if( num_dup==1) {
			cout<<"Case #"<<casesIter+1<<": "<<*it<<endl;
		}
		
	}
	return 0;

}