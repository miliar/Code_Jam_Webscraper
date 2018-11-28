#include <iostream>
#include <algorithm>
using namespace std;
// returns 1 if can't be placed
int solve (int r, int c, int x){
	if (r>4 or c>4 or x>4){
		return 0;
	}
	if (r<c){
		int q= c;
		c= r;
		r=q;
	}
	if (r*c%x!=0){
		return 1;
	}
	if (x==1){
		return 0;
	}
	if (x==2 and r*c%2==0){
		return 0;
	}
	if (c==1){
		if (x>2){
			return 1;
		}
		return 0;
	}
	if (r==4){
		if (c==4){
			if (x==4){
				return 0;
			}
			return 1;
		}
		if (c==3){
			if (x==3){
				return 0;
			}
			if (x==4){
				return 0;
			}
		}
		if (c==2){
			if (x==4){
				return 1;
			}
		}
	}
	if (r==3){
		if (c==3 and x==3){
			return 0;
		}
		if (c==2){
			if (x==3){
				return 0;
			}
			
		}
	}
	if (r==2 and c==2){
		if (x==4){
			return 1;
		}
	}
	
	
}




int main() {
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for (int pinkfloyd= 1; pinkfloyd<=t; pinkfloyd++){
		int r, c, x;
		cin>>x;
		cin>>r;
		cin>>c;
		if (solve(r, c, x)==1){
			cout<<"Case #"<<pinkfloyd<<": RICHARD"<<endl;
		}
		else{
			cout<<"Case #"<<pinkfloyd<<": GABRIEL"<<endl;
		}
	}

	return 0;
}