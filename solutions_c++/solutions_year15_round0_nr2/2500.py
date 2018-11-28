#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include<unordered_map>
#include<unordered_set>
using namespace std;

#define mp(a,b) make_pair((a),(b))
#define MS( a ) memset( a,0,sizeof(a))
#define MSV( a,v ) memset( a,v,sizeof(a))
typedef long long ll;
typedef pair<int,int> pii;
#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for(typeof((C).end()) I=(C).begin(); I!=(C).end(); ++I)
#define forNF(I,S,C) for(int I=(S); I<int(C); ++I)
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<pii> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned u32;

struct greater
{
	bool operator()(const int s1, const int s2) const
  {
    return s1>s2;
  }
};

map<int,int,greater> cakes;

void preprocess(VI vec){
	cakes.clear();
	sort(ALL(vec));
	int i=0;
	while(i<vec.size()){
		int cur = vec[i];
		int count = 0;
		while(i<vec.size()&&vec[i]==cur){	count++;i++;	}
		cakes[cur]=count;
	}
}

int dfs(map<int,int,greater> newcakes){
	if(newcakes.size()==0){
		return 0;
	}
	map<int,int,greater>::iterator most = newcakes.begin();
	if(most->first<=3){
		return most->first;
	}
	int min = most->first;

	forNF(i,1,most->first/2+1){
		int sp1 = i;
		int sp2 = most->first -i;
		int ct1 = most->second;
		int ct2 = most->second;
		map<int,int,greater> temp = newcakes;
		temp.erase(temp.begin());
		if(temp.find(sp1)==temp.end()){
			temp[sp1] = ct1;
		}else{
			temp[sp1]+=ct1;
		}
		if(temp.find(sp2)==temp.end()){
			temp[sp2] = ct2;
		}else{
			temp[sp2]+=ct2;
		}
		int submin = dfs(temp) +ct1;
		if (min>submin){min = submin;}
	}
	//if(most->first%2==0){
	//	int count = most->second*2;
	//	int split = most->first/2;
	//	map<int,int,greater> temp = newcakes;
	//	temp.erase(temp.begin());
	//	if(temp.find(split)==temp.end()){
	//		temp[split] = count;
	//	}else{
	//		temp[split]+=count;
	//	}
	//	int submin = dfs(temp) + count/2;
	//	if (min>submin){min = submin;}
	//}else{
	//	int sp1 = most->first/2;
	//	int sp2 = most->first/2 +1;
	//	int ct1 = most->second;
	//	int ct2 = most->second;
	//	map<int,int,greater> temp = newcakes;
	//	temp.erase(temp.begin());
	//	if(temp.find(sp1)==temp.end()){
	//		temp[sp1] = ct1;
	//	}else{
	//		temp[sp1]+=ct1;
	//	}
	//	if(temp.find(sp2)==temp.end()){
	//		temp[sp2] = ct2;
	//	}else{
	//		temp[sp2]+=ct2;
	//	}
	//	int submin = dfs(temp) +ct1;
	//	if (min>submin){min = submin;}
	//}
	return min;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC, T;
	cin>>TC;
	for (T = 1; T <= TC; T++){
		int D;
		cin>>D;
		VI vec;
		forN(d,D){
			int p;
			cin>>p;
			vec.push_back(p);
		}
		preprocess(vec);
		int ans = dfs(cakes);
		printf("Case #%d: ", T);
		cout<<ans<<endl;
	}
}