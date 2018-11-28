#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<double> a1;
vector<double> a2;

int test1(vector<double> v1, vector<double> v2){
	int t = 0;
	while(!v1.empty()){
		if(v1[0]>v2[0]){
			t++;
			v1.erase(v1.begin());
			v2.erase(v2.begin());
		}
		else if(v1[0]<v2[v2.size()-1]){
			v1.erase(v1.begin());
			v2.pop_back();
		}
		else {
			break;
		}
	}
	return t + v1.size();
}

int test2(vector<double> v1, vector<double> v2){
	while(!v1.empty()){
		int i;
		for(i=0;i<v2.size();i++){
			if(v2[i]>v1[0])
				break;
		}
		if(v2.size()==i){
			return v1.size();
		}
		v2.erase(v2.begin()+i);
		v1.erase(v1.begin());
	}
	return 0;
}

int T;

int main(){
	scanf("%d",&T);
	for(int Case=1;Case<=T;Case++){
		int N;
		scanf("%d",&N);
		a1.clear();
		a2.clear();
		for(int i=0;i<N;i++){
			double d;
			scanf("%lf",&d);
			a1.push_back(d);
		}
		for(int i=0;i<N;i++){
			double d;
			scanf("%lf",&d);
			a2.push_back(d);
		}
		sort(a1.begin(),a1.end());
		sort(a2.begin(),a2.end());
		printf("Case #%d: %d %d\n",Case,test1(a1,a2),test2(a1,a2));
	}	
}