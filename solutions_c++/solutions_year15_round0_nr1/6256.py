#include <iostream>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
using namespace std;
bool  enter;
int n,i,j,sm,sum,ret;
int main() {
	//cout<<"enter";
//	cin>>enter;
	freopen("in.txt","r",stdin);
	 freopen("out.txt","w",stdout);




	 cin>>n;
	 for (j	 = 1; j <= n; ++j) {
		string s;
		 cin>>sm;
		 cin>>s;
		 sum=ret=0;
		 for (i = 0; i <= sm; ++i) {
		//	 cout<<ret<<" i "<<i<<" sum "<<sum<<endl;
			if(sum<i){
				ret++;
				sum++;
			}
			sum+=s[i]-'0';
		}

		 cout<<"Case #"<<j<<": "<<ret<<endl;
	}



	return 0;
}
