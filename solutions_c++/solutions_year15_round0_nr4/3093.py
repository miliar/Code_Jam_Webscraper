#include <iostream>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include<map>
using namespace std;

bool enter;
int n, i, j, c,r,x, last;


string ret[] = { "GABRIEL", "RICHARD" };

int main() {


//	cout<<"enter";
//	cin>>enter;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> n;

	for (j = 1; j <= n; ++j) {
		cin>>x;
		cin>>r;
		cin>>c;

		if(x==1)
			enter=0;
		else if(x==2){
			if(((r*c)&1)==0){
				enter=0;
			}else{
				enter=1;
			}
		}else if(x==3){
			if((r*c)%3==0){
				if(r!=1&&c!=1)
					enter=0;
				else
					enter=1;
			}else
				enter=1;
		}else if(x==4){
			if((r*c)%4==0){
				if(c==1||c==2||r==1||r==2)
					enter=1;
				else
					enter=0;
			}else{
				enter=1;
			}
		}

		cout << "Case #" << j << ": " << ret[enter] << endl;
	}

	return 0;
}
