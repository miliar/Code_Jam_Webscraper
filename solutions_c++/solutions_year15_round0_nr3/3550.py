#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int table[5][5]={
	0,0,0,0,0,
	0,1,2,3,4,
	0,2,-1,4,-3,
	0,3,-4,-1,2,
	0,4,3,-2,-1,
};

short int mulj[10001][10001]={0};


string solve(vector<int> &input,int len)
{
	vector<int> ibegin;
	int mul = 1;
	int i,j;
	int flag = 1;
	for(i=0;i<len;++i){
		flag = 1;
		if(mul < 0) {flag = -1;mul = -mul;}
		mul = flag*table[mul][input[i]];
		if(mul == 2)
			ibegin.push_back(i);
	}
	
	if(ibegin.empty())
		return "NO";
	
	vector<int> kbegin;
	mul = 1;
	flag = 1;
	for(i=len-1;i>=0;--i){
		flag = 1;
		if(mul < 0) {flag = -1;mul = -mul;}
		mul = flag*table[input[i]][mul];
		if(mul == 4)
			kbegin.push_back(i);
	}

	if(kbegin.empty())
		return "NO";

	int ilen = ibegin.size();
	int klen = kbegin.size();
	for(i=0;i<ilen;++i)
		for(j=0;j<klen;++j){
			if(ibegin[i]+1<=kbegin[j]-1){
				if(mulj[ibegin[i]+1][kbegin[j]-1]==3)
					return "YES";
			}
			else 
				break;
		}
	
	return "NO";
}

int main()
{
	freopen("C-small-practice.in","r",stdin);
    freopen("C-small-practice.out","w",stdout);

	map<char,int> m;
	m['i'] = 2;
	m['j'] = 3;
	m['k'] = 4;

	int cnt = 0;
	int T;
	cin>>T;
	int L,X;
	
	while(T--){
		string res;
		cin>>L>>X;

		vector<int> input;
		vector<int> tmp(L,0);
		char c;
 		for(int i=0;i<L;++i){
 			cin>>c;
 			tmp[i] = m[c];
 		}

		if(L==1||L*X < 3){
			res = "NO";
		}
		else{
			for(int i=0;i<X;++i)
				input.insert(input.end(),tmp.begin(),tmp.end());
			//cout<<input.size()<<endl;

			int len = input.size();
			for(int i=0;i<len;++i){
				short int mul = 1;
				short int flag = 1;
				for(int j=i;j<len;++j){
					flag = 1;
					if(mul < 0) {flag = -1;mul = -mul;}
					mulj[i][j] = flag*table[mul][input[j]];
					mul = mulj[i][j];
					//cout<<mulj[i][j]<<" ";
				}
				//cout<<endl;
			}

			res = solve(input,L*X);
		}
		
		cout<<"Case #"<<++cnt<<": ";
		cout<<res<<endl;
	}
	
	return 0;
}