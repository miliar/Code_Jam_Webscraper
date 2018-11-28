#include<iostream>
#include<string.h>
using namespace std;

char cnt[16];

int main(){
	int t, i, ans, a, c=1, b, d;
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
	cin>>t;
	while(t--) {
		memset(cnt,0,sizeof(cnt));
		cin>>ans;
		for(i=0;i<16;i++) {
			cin>>a;
			if(i/4==ans-1) cnt[a-1]=1;
		}
		cin>>ans;
		for(i=0;i<16;i++) {
			cin>>a;
			if(i/4==ans-1) cnt[a-1]|=2;
		}
		for(i=b=0;i<16;i++) {
			if( cnt[i]==3 ) {
				b++;
				d=i+1;
			}
		}
		cout<<"Case #"<<c<<": ";
		if( b == 0 ) {
			cout<<"Volunteer cheated!"<<endl;
		} else if( b == 1 ) {
			cout<<d<<endl;
		} else {
			cout<< "Bad magician!"<<endl;
		}
		c++;
	}

	return 0;
}
