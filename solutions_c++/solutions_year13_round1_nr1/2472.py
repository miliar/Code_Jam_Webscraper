#include<iostream>

using namespace std;

main(){

	int T;
	cin>>T;
	int cou=1;
	while(T--){
		long long r,t;
		cin>>r>>t;
		long long min = 1ll, mid=1;
		long long max = 1000000000ll;
		if(max > t/(r)+100)
			max = t/(r)+100;
		long long cost=0;
		while(mid != (min + max)/2){
			mid = (min + max)/2;
			cost = mid*2*r + (((mid-1)*4 + 2)*mid)/2;
			//cout<<"mid: "<<mid<<" / cost: "<<cost<<endl;
			if(cost > t)
				max = mid;
			else if(cost == t){
				break;
			}
			else
				min = mid;
		}
		cout<<"Case #"<<cou<<": ";
		if(cost > t)
			cout<<mid-1<<endl;
		else
			cout<<mid<<endl;
		cou++;
	}

	return 0;
} 