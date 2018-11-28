#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;



int main()
{


	ofstream outf;
	ifstream inf;
	outf.open("output.in");
	inf.open("input.in");


    //istringstream lines(line);

	int t;
	inf>>t;



	for(int tt=0;tt<t;tt++)
	{
		int patt[100][100];
		int M, N;
		inf>>N>>M;
		for (int i =0;i<N;i++)
			for (int j =0;j<M;j++)
				inf>>patt[i][j];


		int possible=1;
		for (int i =0;i<N;i++){
		for (int j =0;j<M;j++){
			int testx=1;
			int testy=1;
						for (int x =0;x<M;x++)
							if(patt[i][x] > patt[i][j]){ testx=0;break;}
						for (int y=0;y<N;y++)
							if(patt[y][j]>patt[i][j]) {testy=0;break;}
						if(testx==0 && testy==0 ) {possible=0;break;}
					}
		if (possible ==0)break;
		}
		if(possible==1)
		outf<<"Case #"<<tt+1<<": YES\n";
		else
			outf<<"Case #"<<tt+1<<": NO\n";
	}//tt lope


}





