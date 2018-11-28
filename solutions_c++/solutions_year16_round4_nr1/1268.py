/*********** [ scopeInfinity ] ******************/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <map>
#include <cmath>
#include <sstream>
#include <bitset> 
#include <assert.h> 


using namespace std;

typedef long long ll;

ll MOD = 1e9+7;

vector<string> &split(const std::string &s, char delim, vector<string> &e) {
    stringstream ss(s);
    string item;
    while(getline(ss, item, delim))
        e.push_back(item);
    return e;
}


ll Pow(ll a ,int b ,int Mo){
    ll ans = 1;
    for (; b; b >>= 1, a = a * a % Mo)
        if (b&1) ans = ans * a % Mo;
    return ans;
}
//PRS
//0 - paper
//1 - sciisor
//2 - rock

int N,L;
std::vector<int> LEFT(3);

int isWin(int me,int o) {
	assert(me!=o);
	if(o==0 && me==1)
		return 1;
	if(o==1 && me==2)
		return 1;
	if(o==2 && me==0)
		return 1;

	return 0;
}
int getLoser(int me){
	return (me+2)%3;
}
std::vector<int> leftB;
	
char getChar(int x) {
	if(x==0)
		return 'P';
	if(x==1)
		return 'S';
	if(x==2)
		return 'R';
	assert(0);

}
bool gt(int l,int r) {
//021
	if(l==1)
		l=2;
	else if(l==2)
		l=1;
	if(r==1)
		r=2;
	else if(r==2)
		r=1;
	return l>r;

}
bool isPossibe(std::vector<int> &v,int winner,int level) {
	if(level==N) {
		LEFT = leftB;
		v.clear();
	}
//cout<<"L"<<level;
	if(level==0) {
		if(LEFT[winner]==0)
			return 0;
		v.push_back(winner);
		LEFT[winner]--;

		assert(LEFT[winner]>=0);
		return 1;
	}
	int o = getLoser(winner);
	std::vector<int> l,r;
	int flag = true;
	
	flag&= isPossibe(l,winner,level-1);
	flag&= isPossibe(r,o,level-1);
	if(!flag)
		return flag;
	bool LSmall = true;
	for (int i = 0; i < l.size(); ++i)
	{
		if(gt(l[i],r[i]))
		{
			LSmall = false;
			break;
		}
	}
	if(!LSmall)
		swap(l,r);



	for (int i = 0; i < l.size(); ++i)
	{
		v.push_back(l[i]);
	}
	for (int i = 0; i < r.size(); ++i)
	{
		v.push_back(r[i]);
	}
	return flag;

	
}
long solve() {
	cin>>N;
	L = 1<<N;
	std::vector<int> v;
	cin>>LEFT[2]>>LEFT[0]>>LEFT[1];
	leftB = LEFT;

	bool done = false;
	if(isPossibe(v,0,N))
		done = true;
	else if(isPossibe(v,1,N))
		done = true;
	else if(isPossibe(v,2,N))
		done = true;
	else cout<<"IMPOSSIBLE";
	if(done)
	{

		LEFT = leftB;
		std::vector<int> t(3,0);
		for (int i = 0; i < v.size(); ++i)
		{
			cout<<getChar(v[i]);
			t[v[i]]++;
		}
		assert(LEFT==t);
	}
	
}

int main(int argc, char const *argv[])
{
	std::ios::sync_with_stdio(false);
	
	
	int T;
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
			cout<<"Case #"<<i+1<<": ";
			solve();
			cout<<endl;
	}
	

	return 0;
}

