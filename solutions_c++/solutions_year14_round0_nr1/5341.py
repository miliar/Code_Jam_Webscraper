#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int z, x;
		cin>>z;
		z--;
		int f[17] = {0,};
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>>x;
				if(i==z){
					f[x]++;
				}
			}
		}
		cin>>z;
		z--;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>>x;
				if(i==z){
					f[x]++;
				}
			}
		}
		int num2 = 0;
		int val = -1;
		for(int i=1; i<=16; i++){
			if(f[i]==2){
				num2++;
				val = i;
			}
		}
		cout<<"Case #"<<testnum+1<<": ";
		if(num2==1){
			cout<<val;
		}else if(num2==0){
			cout<<"Volunteer cheated!";
		}else{
			cout<<"Bad magician!";
		}
		cout<<endl;
	}
	return 0;
}
