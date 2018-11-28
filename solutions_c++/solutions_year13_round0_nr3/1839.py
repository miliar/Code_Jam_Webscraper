#include <iostream>
#include <climits>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <utility>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

typedef unsigned long long ull;

vector<ull> vu;
vector<int> vd(20,0);

bool ispalim(ull d)
{
	int nd=0;
	while(d>0)
	{
		vd[nd++]=d%10;
		d=d/10;
	}
	int l=0,r=nd-1;
	while(l<r)
	{
		if(vd[l]!=vd[r])
			return false;
		l++;r--;
	}	
	return true;
}

void init()
{
	ull m=(ull)sqrt(pow(10,14)+1);
	ull i=1;
	while(i<=m)
	{
		if(ispalim(i)&&ispalim(i*i))
			vu.push_back(i*i);
		i++;
	}
}

int palimcount(ull A, ull B)
{
	vector<ull>::iterator low,up;
	low=lower_bound(vu.begin(),vu.end(),A);
	up=upper_bound(vu.begin(),vu.end(),B);

	return up-low;
}

int main() {
 
        init();
        int T;
        cin>>T;
        int count=1;
        
        while(T--)
        {
		ull A, B;
		cin>>A>>B;

                cout<<"Case #"<<count++<<": "<<palimcount(A,B)<<endl;
         }



        return 0;
}
