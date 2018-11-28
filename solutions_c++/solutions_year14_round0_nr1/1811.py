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

void display(VI a){
	cout << "###" << endl;
	for(int i=0;i<a.size();i++)
		cout << a[i] << " ";
	cout << endl;
}

VI intersection (VI s, VI t){
	int i=0, j=0;
	VI out;
	while(i < s.size() && j < t.size()){
		if(s[i] < t[j])
			i++;
		else if(s[i] > t[j])
			j++;
		else{
			out.push_back(s[i]);
			i++;
			j++;
		}
	}
	return out;
}

int main(){
	
	VI s, t;
	VI::iterator it;
	int te, m, n, a, case_no = 1;
	scanf("%d", &te);
	while(te--){
		
		VI out(10);
		s.clear();
		t.clear();
		out.clear();
		
		scanf("%d", &m);
		
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				scanf("%d", &a);
				if(i == m)
					s.push_back(a);
			}
		}
		
//		display(s);
		
		scanf("%d", &n);
		
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				scanf("%d", &a);
				if(i == n)
					t.push_back(a);
			}
		}
		
//		display(t);
		
		sort(s.begin(), s.end());
		sort(t.begin(), t.end());
		
//		display(s);
//		display(t);
		
		out = intersection(s, t);
//		display(out);
		
		printf("Case #%d: ", case_no++);
		if(out.size() == 1)
			printf("%d\n", out[0]);
		else if(out.size() > 1)
			printf("Bad magician!\n");
		else if(out.size() == 0)
			printf("Volunteer cheated!\n");
	}
    return 0;
}
