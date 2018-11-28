#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cctype>
#include <iomanip>
#define INF 2000000000
#define M 1000000007LL

using namespace std;

int main()
{
	int T;
	cin>>T;
	int t = 0;
	while (t++<T){
		double c, f, x;
		cin>>c>>f>>x;
		double time = 0;
		int left = 0, right = x*x;
		int mid;
		int tag;
		double mini = x/2;
		for (int farm = 0; farm<=10000; farm++){
			time = 0;
			for (int i = 1; i<=farm; i++){
				time += c/(2+(i-1)*f);
			}
			time += x/(2+farm*f);
			if (time<mini){
				mini = time;
				tag = farm;
			}
			else break;
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(8)<<mini<<endl;
	}
}