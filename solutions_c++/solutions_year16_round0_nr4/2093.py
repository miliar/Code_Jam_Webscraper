#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cassert>

using namespace std;

int main()
{
	int T;
	cin>>T;
	
	for(int t=1;t<=T;t++){
		
		long long K,C,S;
		cin>>K>>C>>S;
		
		//if(K==100 && C==9) cout<<"-----"<<endl;
		
		printf("Case #%d:",t);
		//long long L=pow(K,C);
		
		long long L=1;
		for(int i=0;i<C;i++) L*=K;
		
		if(K==1){
			cout<<" 1";
		}else{
			long long d=(L-1)/(K-1);
			long long cnt=0;
			long long pos;
			for(pos=1;pos<=L;pos+=d){
				cout<<" "<<pos;
				cnt++;
			}
			assert(cnt==K);
			assert(pos-d==L);
		}
		
		cout<<endl;
		//if(K==100 && C==9) cout<<"-----"<<endl;
	}

    
    return 0;
}