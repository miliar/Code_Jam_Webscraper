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
   // ofstream cout("output.txt");
typedef long long ll;
typedef long double ld;
typedef vector<int> vk;
int t;
ld a[1000001];
int main(){
	cin>>t;
	ld c,f,x;
	a[0] = 0;
	ld mm;
	cout<<setiosflags(ios::fixed)<<setprecision(7);
	for(int j = 0;j < t;j++){
		cin>>c>>f>>x;
		mm = x / 2;
		for(int i = 1; i <= 1000000; i++){
			a[i] = a[i-1] + c / ((i - 1) * f + 2);
			if(a[i] >= x / 2) break;
			mm = min(mm,a[i] + x / (i * f+2));
		}
		cout<<"Case #"<<j+1<<": "<<mm<<endl;
	}
    return 0;
}