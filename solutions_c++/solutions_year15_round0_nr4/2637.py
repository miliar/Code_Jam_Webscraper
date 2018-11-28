#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

int main() {
	int T;
	//freopen("a2.in", "r", stdin);
	//freopen("a4.out", "w", stdout);
	cin>>T;
	for(int y = 1; y<=T; y++){
		int x, r, c;
		cin>>x>>r>>c;

		cout<<"Case #"<<y<<": ";
	//	cout<<endl<<x<<" "<<r<<" "<<c<<endl;
		if((x>r && x>c) || ((r*c) % x != 0))
            cout<<"RICHARD"<<endl;
		else {
			int xB = (int)ceil((double)x/2);
			if((r >= xB && c>=x) || (c>= xB && r>=x)){
				//if((x>=5 && x%2 != 0) || x>8)
                  //  cout<<"RICHARD"<<endl;
				//else
				if(x == 4 && ((r < 4 && c < 4) || r < 3 || c < 3))
                    cout<<"RICHARD"<<endl;
                else
                    cout<<"GABRIEL"<<endl;
			} else cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}
