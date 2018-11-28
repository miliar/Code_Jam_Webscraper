#include <iostream>
#include <assert.h> 
using namespace std;

bool solve(int x, int r, int c){
	if(r<c)
		return solve(x,c,r);
	if(x==1)
		return true;
	if(x>r)
		return false;
	if(x>=3 && c == 1)
		return false;
	if(r*c/x*x!=r*c) 
		return false;
	if(c==1){ 
		assert(x==2 && r%2==0);
		return true;
	}
	if(x<=c) {
		//2<=x<=c<=r
		if(x==2)
			return true;
		if(x==3) //3,3,3 3,3,4
		{
			if(r==3 && c==3)
				return true;
			if(r==4 && c==3)
				return true;
		}else{ //4,4,4
			return true;
		}
	}else{
		// x>c>1, r>=c>1
		if(c==3) {
			//4,4,3
			return true;
		}
		else {
			//c=2
			//3,2,3
			if(x==3)
				return true;
			//4,2,4
			return false;
		}
		//1<c<x<=r<=4
		//2,4,4 false
		//3,4,4 true
	}
}

int main(){
	int T = 0;
	cin>>T;
	for(int i = 0; i < T; i++){
		int x,r,c;
		cin>>x>>r>>c;
		if(solve(x,r,c)){
			cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
		}else{
			cout<<"Case #"<<i+1<<": RICHARD"<<endl;
		}
	}
	return 0;
}
