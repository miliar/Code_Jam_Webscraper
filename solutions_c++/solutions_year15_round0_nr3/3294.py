#include <iostream>
#include <assert.h>
#include <vector>
using namespace std;

// a * b != b * a
// a * (b * c) = (a * b) * c.
// -a * -b = a * b, and -a * b = a * -b = -(a * b).


int let2int(char x){
	if(x == '1') return 0;
	if(x == 'i') return 1;
	if(x == 'j') return 2;
	if(x == 'k') return 3;
	assert(false);
}

char getSign(int i, int j)
{
	char sign[4][4] = {
		{1 , 1, 1,  1},
		{1 ,-1, 1, -1},
		{1 ,-1,-1,  1},
		{1 ,1 ,-1, -1}
	};
	return sign[i][j];
}

char mul(int i, int j)
{
	char prod[4][4] = {
		{'1','i','j','k'},
		{'i','1','k','j'},
		{'j','k','1','i'},
		{'k','j','i','1'}
	};
	return prod[i][j];
}

vector<pair<int,int> > findLetter(const string& str,char letter,int x, int curX, int offset){
	if (offset >= str.size())
	{
		offset = 0;
		curX++;
	}
	vector<pair<int,int> > offsets;
	int sign = 1;
	char currLetter = '1';
	while(curX <= x)
	{
		int a = let2int(currLetter);
		int b = let2int(str.c_str()[offset]);
		sign *= getSign(a,b);
		currLetter = mul(a,b);
		if(sign == 1 && letter == currLetter){
			offsets.push_back(make_pair(offset,curX));
		}
		offset++;
		if (offset >= str.size())
		{
			offset = 0;
			curX++;
		}
	}
	return offsets;
}


bool matchPattern(const string& buff, int l, int x)
{
	bool cacheJ[l][x];
	for(int i=0; i<l; i++){
		for(int j=0; j<x; j++){
			cacheJ[i][j] = false;
		}
	}

	int offset = 0;
	int curX = 0;
	x = x - 1;
	
	vector<pair<int,int> > offsetsI = findLetter(buff,'i',x,curX,offset);
	
	for(int i=0; i<offsetsI.size(); ++i){
		offset =  offsetsI[i].first;
		curX   =  offsetsI[i].second;
		vector<pair<int,int> > offsetsJ = findLetter(buff,'j',x,curX,offset+1);
		
		for(int j=0; j<offsetsJ.size(); ++j){
			offset =  offsetsJ[j].first;
			curX   =  offsetsJ[j].second;

			if(cacheJ[offset][curX]){
				continue;
			}
			else{
				cacheJ[offset][curX]  = true;
			}
			vector<pair<int,int> > offsetsK = findLetter(buff,'k',x,curX,offset+1);
			
			for(int k=0; k<offsetsK.size(); ++k){
				offset =  offsetsK[k].first;
				curX   =  offsetsK[k].second;
				if(curX == x and offset == buff.size() -1){
					return true;
				}
			}
		}
	}
	return false;


}

int main()
{
	int n = 0;
	cin >> n;

	int l,x;
	string buff;

	for(int i=0; i<n; ++i){
		cin >> l >> x;
		cin >> buff;
		cout << "Case #" << i+1 << ": " << (matchPattern(buff,l,x)?"YES":"NO") << endl;
	}
	return 0;
}