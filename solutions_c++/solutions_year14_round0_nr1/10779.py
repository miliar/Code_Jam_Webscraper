//============================================================================
// Name        : google.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.in","w",stdout);
	int t=0,T;
	cin>>T;
	while(t++<T)
	{
		int r1,r2;
		vector<int> V1(4),V2(4),tmp(4);

		cin>>r1;
		for(int i=1;i<=4;i++)
			if(i == r1)
				for(int j =0;j<4;j++)
					cin>>V1[j];
			else
				for(int j=0;j<4;j++)
					cin>>tmp[i];

		cin>>r2;
		for(int i=1;i<=4;i++)
			if(i == r2)
				for(int j=0;j<4;j++)
					cin>>V2[j];
			else
				for(int j=0;j<4;j++)
					cin>>tmp[i];

		int n = 0;
		int loc;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(V1[i] == V2[j])
				{
					loc = i;
					n++;
				}

		if(n > 1)
			printf("Case #%d: Bad magician!\n",t);
		else if(n == 1)
			printf("Case #%d: %d\n",t,V1[loc]);
		else
			printf("Case #%d: Volunteer cheated!\n",t);
	}



	return 0;
}
