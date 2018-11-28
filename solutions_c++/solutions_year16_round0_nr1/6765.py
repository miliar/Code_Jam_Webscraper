//#pragma comment(linker,"/STACK:200000000")
#pragma warning(disable:4996)
#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <utility>
#include <algorithm>
#include <numeric>
#include <functional>
//#include <unordered_map>
using namespace std;

typedef long long ll;
ll T,N;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Ans.out","w",stdout);
	//ifstream fin("dict.out");
	//ofstream fout("Ans.out");
	//FILE *fin=fopen("table.txt","r");
	//FILE *fout=fopen("Ans.out","w");
	cin>>T;
	for(int cas=1;cas<=T;cas++){
		cin>>N; ll val=N;
		if(N!=0){
			int tot=0; bool sign[10];
			memset(sign,0,sizeof(sign));
			for(int i=0;i<1e4;i++){
				ll tmp=val;
				while(tmp!=0){
					int digit=tmp%10;
					tmp/=10;
					if(!sign[digit]){
						tot++; sign[digit]=true;
					}
				}
				if(tot==10) break;
				val+=N;
			}
			if(tot!=10) cout<<"Error "<<N<<endl;
		}
		if(N==0) printf("Case #%d: INSOMNIA\n",cas);
		else printf("Case #%d: %d\n",cas,val);
	}

	return 0;
}