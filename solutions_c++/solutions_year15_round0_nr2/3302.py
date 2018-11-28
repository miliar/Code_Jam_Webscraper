#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

ifstream in("pancake.in");
ofstream out("pancake.out");

int t;

bool compare(double a,double b){
    return a>b;
}

int ub(double a){
    if(a > (int)a) return a+1;
    else return a;
}
int main(){
    in >> t;
	for(int k=1;k<=t;k++){
		vector<double> a;
		int d;
		in >> d;
		a.resize(d);

		for(int i=0;i<d;i++){
			in >> a[i];
		}
		sort(a.begin(),a.end(),compare);
		int tot=999999999;
		for(int i=1;i<=a[0];i++){
			int sm=0;
			for(int j=0;j<d;j++){
				sm+=ub((a[j]-i)/i);
			}
			tot=min(tot,sm+i);
		}
		out<<"Case #"<<k<<": "<<tot<<"\n";
	}

	return 0;
}
