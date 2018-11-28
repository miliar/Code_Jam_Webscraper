#include <iostream>
using namespace std;
 
int main(){
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int tt, s, n, c;
	int y=1;
	cin>>tt;
	while(y<=tt){
		cin>>n>>c>>s;
		if(n==1)
			cout<<"Case #"<<y<<": 1"<<endl;
		
		else if(c==1){
			if(s>=n){
				cout<<"Case #"<<y<<": ";
				for(int i=1;i<=n;i++)
					cout<<i<<" ";
				cout<<endl;
			}
			else 
				cout<<"Case #"<<y<<": IMPOSSIBLE"<<endl;
		}
		else{   
			if(s>=n-1){
				cout<<"Case #"<<y<<": ";
				for(int i=2;i<=n;i++)
					cout<<i<<" ";
				cout<<endl;
			}
			else
				cout<<"Case #"<<y<<": IMPOSSIBLE"<<endl;	
		}
		y++;
	}
	return 0;
}
