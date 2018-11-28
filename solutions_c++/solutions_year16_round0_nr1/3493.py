#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include<set>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
	//ifstream cin("A-small-attempt0.in");
	//ofstream cout("A-small.out");

	int tc;cin>>tc;
	for(int i=1;i<=tc;i++){
		long int n;cin>>n;
		if(n==0) cout<<"Case #"<<i<<": INSOMNIA\n";
		else{
			std::set<int> ss;
			long int temp=n,count=1;
			while(1){
				while(temp){
					ss.insert(temp%10);
					temp/=10;
				}
				if(ss.size()==10) break;
				else{
					count++;
					temp = count*n;
				}
			}
			cout<<"Case #"<<i<<": "<<count*n<<endl;
		}
	}
}
