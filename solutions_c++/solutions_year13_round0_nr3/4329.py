#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <sstream>
 
using namespace std;	

bool palindrom(long long pal){
	stringstream ss;
	ss << pal;
	string str = ss.str();
	bool je=true;
	for(int i=0; i<str.size()/2; i++){
		if(str[i]!=str[str.size()-i-1]) {
			je=false;
			break;
		}
	}
	return je;
}

int main(){
	int kolko;
	scanf("%d",&kolko);
	vector<pair<long long,long long> > otazky;
	vector<long long> vysledky;
	vysledky.resize(kolko,0);
	while(kolko--){
		long long a,b;
		scanf("%lld%lld",&a,&b);
		otazky.push_back(make_pair(a,b));
	}
	for(long long i =0; i<10000000; i++){
		if(palindrom(i)){
			if(palindrom(i*i)){
				long long cislo=i*i;
				for(int j=0; j<otazky.size(); j++){
					if((otazky[j].first<=cislo)&&(otazky[j].second>=cislo)){
						vysledky[j]++;
					}
				}
			}
		}
	}
	for (int i=0; i<otazky.size(); i++){
		cout<<"Case #"<<i+1<<": "<<vysledky[i]<<endl;
	}
}
// \n ||