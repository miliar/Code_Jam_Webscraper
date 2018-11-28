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

int transform(int left,int right){
	int signl = left>0?1:-1;
	int signr = right>0?1:-1;
	int sign = signl*signr;
	left = abs(left);
	right = abs(right);
	if(left==1||right==1){
		return sign*left*right;
	}
	if(left==right){
		return -sign;
	}
	if(left==3&&right==4){
		return sign*5;
	}
	if(left==3&&right==5){
		return sign*-4;
	}
	if(left==4&&right==3){
		return sign*-5;
	}
	if(left==4&&right==5){
		return sign*3;
	}
	if(left==5&&right==3){
		return sign*4;
	}
	if(left==5&&right==4){
		return sign*-3;
	}
}
int find(VI vec,int start,int target){
	int cur = 0;
	while(start<vec.size()&&cur!=target){
		if(cur == 0){
			cur = 1;
		}
		cur=transform(cur,vec[start]);
		start++;
	}
	if(cur!=target){
		return -1;
	}
	return start-1;
}
int check(VI vec, int start,int end, int target){
	int cur = 1;
	while(start<=end){
		cur=transform(cur,vec[start]);
		start++;
	}
	if(target==cur)return true;
	return false;
}

int check(VI vec, int start, int target){
	int cur = 1;
	while(start<vec.size()){
		cur=transform(cur,vec[start]);
		start++;
	}
	if(target==cur)return true;
	return false;
}

bool dfs(VI vec){
	if(!check(vec,0,-1))return false;
	int i = find(vec,0,3);
	if(i==-1)return false;
	int curstart = i+1;
	while(curstart>=0&&curstart<vec.size()){
		int posj = find(vec,curstart,4);
		if(posj==-1) return false;
		if(check(vec,posj+1,5)){
			return true;
		}
		curstart = find(vec,curstart,1) + 1;
	}
	return false;
}

//bool dfs(VI vec){
//	for(int i = 0;i<vec.size()-2;i++){
//		for(int j=i+1;j<vec.size()-1;j++){
//			if(check(vec,0,i,3)&&check(vec,i+1,j,4)&&check(vec,j+1,vec.size()-1,5)){
//				return true;
//			}
//		}
//	}
//	return false;
//}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC, T;
	cin>>TC;
	for (T = 1; T <= TC; T++){
		int L,X;
		cin>>L>>X;
		VI temp;
		forN(i,L){
			char c;
			cin>>c;
			temp.push_back(c-'i'+3);
		}
		VI vec;
		forN(i,X){
			vec.insert(vec.end(),ALL(temp));
		}

		printf("Case #%d: ", T);
		if(T==8){
			T=8;
		}
		if(dfs(vec)){
			cout<<"YES"<<endl;
		}else{
			cout<<"NO"<<endl;
		}
	}
}