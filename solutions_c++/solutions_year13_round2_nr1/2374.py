#include<iostream>
#include <algorithm>
#include<vector>
#include<fstream>
using namespace std;

int play(vector<int> mote,int A,int count){

	
	if (mote.size()==0) return count;
	while (mote[0]<A && mote.size()>0) {

			A+=mote[0];
			mote.erase(mote.begin());
	}
	if (mote.size()==0){
		return count;
	}
	else{
		int c1,c2;
		
		if (A>1) c1 = play(mote, A+A-1, count+1);
		mote.pop_back();
		
		c2 = play(mote,A,count+1);
		if (A<=1) c1 = c2+1;
		return min(c1,c2);
	}
}

main(){
	int T;scanf("%d",&T);
	fstream mf;
	mf.open("D:/seijee.txt");
	for (int c=1; c<=T; c++){
		vector<int> mote;
		int A,N,t;
		scanf("%d%d",&A,&N);
		for (int i=0; i<N; i++){
			scanf("%d",&t);
			mote.push_back(t);
		}
		sort(mote.begin(),mote.end());
		
		while (mote[0]<A && mote.size()>0) {
			
			A+=mote[0];
			mote.erase(mote.begin());
		}
		int ans = play(mote, A,0);
		
		mf<<"Case #"<<c<<": "<<ans<<endl;
	}
	mf.close();
}

