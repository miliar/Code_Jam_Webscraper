/*Written by Vladimir Ignatiev*/

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(int A=0;A<B;++A)

int K, N;
multiset<int> key;

struct SChest
{
	bool open;
	int type;
	multiset<int> keys;
}chests[500];

stack<int> result;

void subs(multiset<int>& keys)
{
	for(multiset<int>::iterator pos=keys.begin();pos!=keys.end();++pos)
	{
		multiset<int>::iterator pos2=key.find(*pos);
		key.erase(pos2);
	}
}

set<vector<int> > save;
bool SaveState()
{
	vector<int> s_tmp;
	for(multiset<int>::iterator pos=key.begin();pos!=key.end();++pos)
		s_tmp.push_back(*pos);
	
	s_tmp.push_back(-1);

	rep(n,N)
		if(!chests[n].open) s_tmp.push_back(n);

	if(save.end()!=save.find(s_tmp)) return false;
	save.insert(s_tmp);

	return true;
};


int f()
{	
	bool bOpen=true;
	if(!SaveState()) return 0;

	rep(n,N)
	{
		if(!chests[n].open) 
		{
			bOpen=false;
			multiset<int>::iterator pos=key.find(chests[n].type);
			if(pos==key.end()) continue; 
			key.erase(pos);
			chests[n].open=true;
			key.insert(chests[n].keys.begin(),chests[n].keys.end());	

			if(f()) {result.push(n+1);return 1;}

			subs(chests[n].keys);

			chests[n].open=false;
			key.insert(chests[n].type);
		}
	}

	return bOpen;
}

int main()
{
	FILE* In=fopen("D.in","r");if(!In) return 1;
	FILE* Out=fopen("D.res","w");if(!Out) return 2;

	int c_type, c_n_key, c_key;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		save.clear();
		key.clear();

		fprintf(Out,"Case #%d:",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%d",&K,&N);
		
		rep(k,K)
		{
			int tmp;
			fscanf(In,"%d",&tmp);
			key.insert(tmp);
		}

		rep(n,N)
		{
			int tmp_T,tmp_K,tmp;
			fscanf(In,"%d%d",&tmp_T,&tmp_K);
			chests[n].open=0;
			chests[n].type=tmp_T;

			chests[n].keys.clear();
			rep(k,tmp_K)
			{
				fscanf(In,"%d",&tmp);
				chests[n].keys.insert(tmp);
			}
		}
		
		if(f()) 
		{
			for(;result.size();result.pop())
			{
				fprintf(Out," %d",result.top());
			}
			fprintf(Out,"\n");
		}
		else
			fprintf(Out,"%s\n"," IMPOSSIBLE");

	};
	fclose(In);
	fclose(Out);
	return 0;
}