# include <iostream>
# include <cstdio>
# include <vector>
# include <string>
# include <queue>
# include <map>
# include <set>
# include <algorithm>
# include <sstream>
# include <fstream>
# include <cmath>

using namespace std;

# define INF 1<<30
# define MAXN 2000
# define all(x,n) sort(x,x+n)

int T,t,N,rn,rk,ln,lk;
double naomi[MAXN],ken[MAXN];
int s1,s2;

int init(){
	rn = rk = N-1;
	ln = lk = 0;
	return 0;
}

int war(){

	init();
	s2 = 0;
	for(int i = 0 ; i < N ; i++){
		if(naomi[rn] > ken[rk])
			s2++,rn--,lk++;
		else rn--,rk--;
	}	
	return 0;

}

int dwar(){

	init();
	s1 = 0;
	for(int i = 0 ; i < N ; i++){
		if(naomi[ln] > ken[lk])
			s1++,ln++,lk++;
		else ln++,rk--;
	}	
	return 0;

}

int main(){
	
	freopen("dlarge.in","r",stdin);
	freopen("dlarge.txt","w",stdout);

	cin>>T;
	
	while(T--){
		
		cin>>N;
		
		for(int i = 0 ; i < N ; i++)
			cin>>naomi[i];

		for(int i = 0 ; i < N ; i++)
			cin>>ken[i];

		all(naomi,N);
		all(ken,N);

		war();
		dwar();

		cout<<"Case #"<<++t<<": "<<s1<<" "<<s2<<endl;
		
	}	
		
	return 0;
}















