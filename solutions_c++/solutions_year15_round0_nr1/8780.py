#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <bitset>
#include <map>
#include <time.h>
#include <string>
#include "math.h"

typedef long long ll;

#define _40l(index,limit) for(int index=0;index < limit;++index)
#define _40le(index,limit) for(int index=0;index <= limit;++index)
#define _41l(index,limit) for(int index=1;index < limit;++index)
#define _41le(index,limit) for(int index=1;index <= limit;++index)

using namespace std;

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int num;
	cin >> num;
	_41le(i,num){
		int max_shy;
		string x;
		cin >> max_shy >> x;
		int cnt=x[0]-'0',nw_cnt=0;
		_41le(j,max_shy)
		{
			int temp = x[j] -'0';
			if(j > cnt) {nw_cnt+=j-cnt; cnt+= temp + j - cnt;}
			else cnt+=temp;
		}
		cout << "Case #"<<i<<": " << nw_cnt << '\n';
	}
	return;
}