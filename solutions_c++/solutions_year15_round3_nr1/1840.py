#include <iostream>
#include <algorithm>
using namespace std;

int ans(int c, int w){
	if(c-w==1 || c-w==0){
			return c;
		}
		else{
			if(w<=c/2){
				return 1+ans(c-w, w);
			}
			else{
				if(c-w>0)
					return w+1;
				return w;
			}
		}
}

int main(){
	int cases;
	cin>>cases;
	for(int c=1; c<=cases; c++){
		int R,C,W;
		cin>>R>>C>>W;
		cout<<"Case #"<<c<<": "<<ans(C,W)<<endl;
	}
	return 0;
}