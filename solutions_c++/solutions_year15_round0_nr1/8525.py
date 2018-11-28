#include<iostream>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,l;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>l;
		int tk=0,s=0,h;
		char g;
		for(int j=0;j<=l;j++){
			cin>>g;
			h=int(g-'0');
			if(h && j>tk)
				s+=j-tk,tk=j;
			tk+=h;
		}
		printf("Case #%d: %d\n",i+1,s);
	}
	return 0;
}