#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#include <ctime>
//#include <iostream>
//#include <iterator> map<string,int>::iterator i;
using namespace std;
   // ifstream cin("input.txt");
  //  ofstream cout("output.txt");
typedef long long ll;
typedef long double ld;
typedef vector<int> vk;
int t;
int a[17];
int main(){
	cin>>t;
	int x1,x2;
	int x,z;
	for(int i = 0;i < t;i++){
		cin>>x1;
		for(int j = 1; j <= 16; j++){
			cin>>x;
			if(j >= (x1-1) * 4 + 1 && j <= x1 * 4) a[x]++;
		}
		cin>>x1;
		for(int j = 1; j <= 16; j++){
			cin>>x;
			if(j >= (x1-1) * 4 + 1 && j <= x1 * 4) a[x]++;
		}
		x = 0;
		cout<<"Case #"<<i+1<<": ";
		for(int j = 1; j <= 16;j++){
			if(a[j] == 2) {x++;z = j;}
			a[j] = 0;
		}
		if(x == 0)
			cout<<"Volunteer cheated!";
		else if(x == 1)
			cout<<z;
		else
			cout<<"Bad magician!";
		cout<<endl;
	}
    return 0;
}