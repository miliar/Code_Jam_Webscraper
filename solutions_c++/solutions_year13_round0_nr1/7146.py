#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

using namespace std;

int main(){

	int n;
	cin>>n;
	for(int p=0;p<n;p++){
		int a[4][4];
		char c;
		int st = 0;
		bool free=false;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>c;
				if(c=='T')
					a[i][j]=0;
				else if(c=='X')
					a[i][j]=1;
				else if(c=='O')
					a[i][j]=-1;
				else if(c=='.'){
					a[i][j]=100;
					free = true;
				}
			}
		}
			int q=0,w=0;
			for(int i=0;i<4 &&st==0;i++){
				int r=0,c=0;
				for(int j=0;j<4;j++){
					r += a[i][j];
					c += a[j][i];
 				}
				if( (r >= 3 && r<=4 ) || ( c >=3 && c<=4 ))
					st = 1;
				else if(r <= -3 || c <= -3)
					st = 2;
				//cout<<i<<" "<<i<<" : "<<a[i][i]<<endl;
				q+=a[i][i];
				w+=a[i][3-i];
			}
			//cout<<"# "<<q<<" "<<w<<endl;
			if(st==0){
				if( (q >= 3 && q<=4 ) || ( w >=3 && w<=4 ))
					st = 1;
				else if(q <= -3 || w <= -3)
					st = 2;
			}	
		cout<<"Case #"<<p+1<<": ";
		if(st==0 && !free)
			cout<<"Draw"<<endl;
		else if(st==1)
			cout<<"X won"<<endl;
		else if(st==2)
			cout<<"O won"<<endl;
		else
			cout<<"Game has not completed"<<endl;
	}

	return 0;
}
