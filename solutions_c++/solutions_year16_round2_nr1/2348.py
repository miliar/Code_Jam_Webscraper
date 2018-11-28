#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<utility>
#include<cmath>
#define loop(i,a,b) for(int i=a;i<b;i++)
#define rep(i,a) loop(i,0,a)
#define pi acos(-1)
#define all(v) v.begin(),v.end()
using namespace std;

const double eps = 1e-8;
const double INF = 1e12;

void print(int n,string s){
	cout<<"Case #"<<n<<": "<<s<<endl;
}

int main(){
	int t;
	cin>>t;
	rep(p,t){
		string s;
		cin>>s;
		vector<int> ans;
		int a[26]={0};
		rep(i,s.size()){
			rep(j,26){
				if(s[i]==(char)('A'+j))a[j]++;
			}
		}
		while(a[(int)('Z'-'A')]>0){
			ans.push_back(0);
			a[(int)('Z'-'A')]--;
			a[(int)('E'-'A')]--;
			a[(int)('R'-'A')]--;
			a[(int)('O'-'A')]--;
		}
		while(a[(int)('W'-'A')]>0){
			ans.push_back(2);
			a[(int)('T'-'A')]--;
			a[(int)('W'-'A')]--;
			a[(int)('O'-'A')]--;
		}
		while(a[(int)('U'-'A')]>0){
			ans.push_back(4);
			a[(int)('F'-'A')]--;
			a[(int)('O'-'A')]--;
			a[(int)('U'-'A')]--;
			a[(int)('R'-'A')]--;
		}
		while(a[(int)('X'-'A')]>0){
			ans.push_back(6);
			a[(int)('S'-'A')]--;
			a[(int)('I'-'A')]--;
			a[(int)('X'-'A')]--;
		}
		while(a[(int)('S'-'A')]>0){
			ans.push_back(7);
			a[(int)('S'-'A')]--;
			a[(int)('E'-'A')]-=2;
			a[(int)('V'-'A')]--;
			a[(int)('N'-'A')]--;
		}
		while(a[(int)('G'-'A')]>0){
			ans.push_back(8);
			a[(int)('E'-'A')]--;
			a[(int)('I'-'A')]--;
			a[(int)('G'-'A')]--;
			a[(int)('H'-'A')]--;
			a[(int)('T'-'A')]--;
		}
		while(a[(int)('F'-'A')]>0){
			ans.push_back(5);
			a[(int)('F'-'A')]--;
			a[(int)('I'-'A')]--;
			a[(int)('V'-'A')]--;
			a[(int)('E'-'A')]--;
		}
		while(a[(int)('I'-'A')]>0){
			ans.push_back(9);
			a[(int)('N'-'A')]--;
			a[(int)('I'-'A')]--;
			a[(int)('N'-'A')]--;
			a[(int)('E'-'A')]--;
		}
		while(a[(int)('O'-'A')]>0){
			ans.push_back(1);
			a[(int)('O'-'A')]--;
			a[(int)('N'-'A')]--;
			a[(int)('E'-'A')]--;
		}
		while(a[(int)('R'-'A')]>0){
			ans.push_back(3);
			a[(int)('T'-'A')]--;
			a[(int)('H'-'A')]--;
			a[(int)('R'-'A')]--;
			a[(int)('E'-'A')]-=2;
		}
		string temp="";
		sort(ans.begin(),ans.end());
		rep(i,ans.size()){
			temp+=(char)(ans[i]+'0');
		}
		print(p+1,temp);
	}
	return 0;
}