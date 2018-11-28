#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <algorithm>
#include <cmath>
#include <stack>
#include <map>
#include <iomanip>

using namespace std;
typedef long long lint;

int main() {
	ifstream cin("A-large.in");
	ofstream cout("123.out");
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		lint a;
		cin>>a;
		if(a==0){
			cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
			continue;
		}
		bool used[10];
		for(int i=0;i<10;i++) used[i]=0;
		lint b=a;
		lint v=0;
		while(!used[0] || !used[1] || !used[2] || !used[3] || !used[4] || !used[5] || !used[6] || !used[7] || !used[8] || !used[9]){
			lint c=b;
			while(c>0){
				used[c%10]=true;
				c/=10;
			}
			b+=a;
			v++;
		}
		cout<<"Case #"<<(i+1)<<": "<<(v*a)<<endl;
	}
	cin.close();
	cout.close();
}