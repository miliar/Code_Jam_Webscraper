#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>
#include <list>
#include <map>

using namespace std;

	  vector<int> tokenize_str(const string & str,
							string delims)
    {
		using namespace std;
		// Skip delims at beginning, find start of first token
		string::size_type lastPos = str.find_first_not_of(delims, 0);
		// Find next delimiter @ end of token
		string::size_type pos     = str.find_first_of(delims, lastPos);

		// output vector
		vector<int> tokens;

		while (string::npos != pos || string::npos != lastPos)
		{
			// Found a token, add it to the vector.
			int temp = atoi(str.substr(lastPos, pos - lastPos).c_str());
			tokens.push_back(temp);
			// Skip delims.  Note the "not_of". this is beginning of token
			lastPos = str.find_first_not_of(delims, pos);
			// Find next delimiter at end of token.
			pos     = str.find_first_of(delims, lastPos);
		}

		return tokens;
   }

int main()
{
	FILE *in=fopen("S:/input.in.txt","r");
    FILE *out=fopen("S:/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
	
    for (int ii=0;ii < T ;ii++)
    {
		int N = 0;
		int M = 0;
		fscanf(in,"%d %d",&N, &M);
		vector< vector<int> > v;
		for (int i=0;i<N; i++)
		{
			vector <int> vv;
			for (int j=0;j<M;j++)
			{
				int aa = 0;
				fscanf(in,"%d",&aa);
				vv.push_back(aa);
			}
			v.push_back(vv);
		}
		bool notPossible = false;
		for (int i=0;i<N; i++)
		{
			for (int j=0;j<M;j++)
			{
				int cellv =  v[i][j];
				bool foundRG = false;
				bool foundCG = false;
				for (int k=0;k<M;k++)
				{
					if ( v[i][k]>cellv )
						foundRG = true;
				}

				for (int k=0;k<N;k++)
				{
					if ( v[k][j]>cellv )
						foundCG = true;
				}

				if ( foundRG && foundCG )
				{
					notPossible = true;
				}
			}
		}
		if ( notPossible )
			fprintf(out,"Case #%d: NO\n",ii+1);
		else
			fprintf(out,"Case #%d: YES\n",ii+1);
	}
}