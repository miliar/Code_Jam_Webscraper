#include<cstdio>
#include<iostream>
#include<string>
#include<cstdlib>
#include<queue>
#include<stack>
#include<utility>
#include<string>
#include<cstring>
#include<set>
#include<cmath>
#include<vector>
#include<fstream>
#include<map>
#include<list>
#include<algorithm>

#define VI vector<int>
#define VF vector<float>
#define VD vector<double>
#define VC vector<char>
#define VVI vector<VI>
#define VVF vector<VF>
#define VVD vector<VD>
#define VVC vector<VC>
#define SI set<int>
#define SF set<float>
#define SD set<double>
#define SC set<char>
#define SSI set<SI>
#define SSF set<SF>
#define SSD set<SD>
#define SSC set<SC>
#define STI stack<int>
#define STF stack<float>
#define STD stack<double>
#define STC stack<char>
#define STSTI stack<STI>
#define STSTF stack<STF>
#define STSTD stack<STD>
#define STSTC stack<STC>

typedef long long int LLD;
typedef unsigned long long int LLU;

using namespace std;

void display(VF v){
	for(int i=0;i<v.size();i++)
		cout << v[i] << " ";
	cout << endl;
}

bool compare(float a, float b){
	return a > b;
}

int find_z(VF n, VF k){
	
	sort(n.begin(), n.end(), compare);
	sort(k.begin(), k.end(), compare);

	int i=0, j=0, s = n.size(), cnt=0;
	
	while(i < s){
		if(n[i] > k[j])
			cnt++;
		else
			j++;
		i++;
	}
	
	return cnt;
}

int find_y(VF n, VF k){
	sort(n.begin(), n.end());
	sort(k.begin(), k.end());
	
	int i=0, s = n.size(), j=0, cnt=0;
	
	while(i < s){
		if(n[i] > k[j]){
			j++;
			cnt++;
		}
		i++;
	}
	
	return cnt;
}

int main(){
	
	VF na, k;
	int t, n, case_no=1;
	
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		na.clear();
		k.clear();
		
		na.resize(n);
		k.resize(n);
		
		for(int i=0;i<n;i++){
			scanf("%f", &na[i]);
		}
		
		for(int i=0;i<n;i++){
			scanf("%f", &k[i]);
		}
		/*
		sort(na.begin(), na.end());
		sort(k.begin(), k.end());
		
		display(na);
		display(k);
		*/
		printf("Case #%d: ", case_no++);
		
		//		find y.
		
		printf("%d ", find_y(na, k));

		//		find z.
		
		printf("%d\n", find_z(na, k));
	}
    return 0;
}
