#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <list>
#include <climits>
#include <assert.h>

//#include <gmpxx.h>

#ifdef _WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif

using namespace std;
#define ll long long

int table[5][5]=
{
	0,0,0,0,0,
	0, 1, 2, 3, 4,
	0, 2, -1, 4, -3,
	0, 3, -4, -1, 2,
	0, 4, 3, -2, -1
};

int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;
		cout<<"Case #"<<_t+1<<": "<<endl;

		int N;
		cin>>N;

		const double eps=1e-7;

		vector<double> X(N),Y(N);
		for(int i=0;i<N;++i)
		{
			cin>>X[i]>>Y[i];
		}

		for(int i=0;i<N;++i)
		{
			
			int result = N-1;
			for(int msk=0;msk<(1<<N);++msk)
			{
				if( ((msk>>i)&1) == 0)
					continue;

				int b=msk;
				vector<int> rem;
				int sft=0;
				while(b)
				{
					if(b&1)
						rem.push_back(sft);
					++sft;
					b>>=1;
				}

				double myX = X[i];double myY=Y[i];
				int ok=0;
				for(int sind=0;sind<rem.size();++sind)
				{
					for(int eind=sind+1;eind<rem.size();++eind)
					{
						int s=rem[sind];
						int e = rem[eind];
						double m = 0;
						double x,y;
						if(X[e]==X[s])
						{
							m = 0;
							x=X[e];
							y=myY;
						}else if(Y[e]==Y[s])
						{
							y=Y[e];
							x=myX;
						}else{
							m = (Y[e]-Y[s])/(double)(X[e]-X[s]);
							y = Y[s] + m * (myX - X[s]);
							x = X[s]+(myY - Y[s]) /m;
						}
							
						

						if((
							(y>Y[s]-eps&&y<Y[e]+eps)||
							(y<Y[s]-eps&&y>Y[e]+eps)
							)
							&&y>myY+eps)
							ok |= 1;
						if((
							(y>Y[s]-eps&&y<Y[e]+eps)||
							(y<Y[s]-eps&&y>Y[e]+eps)
							)
							&&y<myY-eps)
							ok |= 2;
						if( ((x>X[s]-eps&&x<X[e]+eps)||
							(x<X[s]-eps&&x>X[e]+eps))
							&&x<myX-eps)
							ok|=4;
						if( ((x>X[s]-eps&&x<X[e]+eps)||
							(x<X[s]-eps&&x>X[e]+eps))
							&&x>myX+eps)
							ok|=8;
						if(i==0&&_t==1&&0)
						{
							cerr<<s<<":"<<e;
							cout<<"  -  ";
							cout<<m<<";"<<y<<";"<<x<<";"<<ok<<endl;
						}
					}
				}

				if(ok<1+2+4+8)
				{
					if(0&&_t==1&&i==4&&N-(int)rem.size()==2){
					for(int k=0;k<rem.size();++k)
						cout<<rem[k]<<";";
					cout<<endl;
					}
					result=  min(result, N-(int)rem.size());
				}
			}
			cout<<result<<endl;
		}

	}
}
