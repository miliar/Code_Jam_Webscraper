#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstdlib>
#include <utility>
#include <sstream>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, s, cnt=0, res, sum = 0;
	string cad;
	cin>>t;
	while(t--)
	{
		res=0;
		cnt++;
		cin>>s;
		cin>>cad;
		sum=(cad[0]-'0');
		if(cad[0]=='0'){res++;sum++;}
		for(int i = 1; i < cad.size();i++){
			if(sum<i){
				//cout<<sum<<" "<<i<<endl;
				res+=i-sum;
				sum+=(cad[i]-'0') + (i-sum);
			}else{
				sum+=(cad[i]-'0');
			}
		}
			
		printf("Case #%d: %d\n", cnt,res);

	}
	return 0;
}