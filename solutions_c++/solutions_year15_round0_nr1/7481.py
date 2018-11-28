#include<iostream>
#include<sstream>
#include<iomanip>
#include<stdlib.h>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<utility>
using namespace std;
#define loop(i,l,r) for(int (i)=(int)(l);(i)<(int)(r);(i)++)
#define rloop(i,l,r) for(int (i)=(int)(l);(i)>(int)(r);(i)--)
#define rep(i,n) loop(i,0,n)
#define rrep(i,n) rloop(i,n-1,-1)
#define INF 1<<30
#define mod 1000000007
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

vector<string> split(stringstream& ss){
	string str;
	vector<string> res;
	while(ss>>str)res.push_back(str);
	return res;
}

template <typename T>
class BIT{
	public:
 	BIT(int size) : _size(size) {
    		_data.resize(size + 1);
  	}
  	void Add(int index, T value) {
    		if (index < 0 || index >= _size) return;
    		index++;
    		while (index <= _size) {
    			_data[index] += value;
    			index += index & -index;
    		}
  	}	
  	T Sum(int index) {
    		if (index < 0 || index >= _size) return 0;
   	 	index++;
    		T ret = 0;
    		while (index > 0) {
      			ret += _data[index];
      			index -= index & -index;
    		}
    	return ret;
  	}
 	private:
  		std::vector<T> _data;
  		int _size;
};


int main(){
	int T,N;
	string s;
	cin>>T;
	rep(i,T){
		BIT<int> BIT(1<<10);
		cin>>N;
		cin>>s;
		int res=0,tmp=0;
		rep(j,s.size()){
			if(s[j]){
				tmp=j-BIT.Sum(j);
				if(tmp>0){
					res+=tmp;
					BIT.Add(j,tmp);
				}
				BIT.Add(j,s[j]-'0');
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
}






