# include <iostream>
# include <vector>
# include <cstring>
# include <string>
# include <cmath>
# include <algorithm>
# include <iomanip>
# include <cstdio>

using namespace std;

# define INF 1000000000
# define MOD 1000000007
# define all(x) x.begin(),x.end()
# define mp make_pair
# define pb push_back
# define pi pair<int,int>

int x,r,c;

void solve(){

	if(r > c) swap(r,c);

	if(x == 1){
		cout<<"GABRIEL"<<endl;
		return;
	}
	
	if(r == 1 && c == 1){
		if(x == 2) cout<<"RICHARD"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;

	}
	else if(r == 1 && c == 2){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;
	}
	else if(r == 1 && c == 3){
		if(x == 2)	cout<<"RICHARD"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;
	}
	else if(r == 1 && c == 4){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;	
	}
	else if(r == 2 && c == 2){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;
	}
	else if(r == 2 && c == 3){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"GABRIEL"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;
	}
	else if(r == 2 && c == 4){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;
	}
	else if(r == 3 && c == 3){
		if(x == 2)	cout<<"RICHARD"<<endl;
		else if(x == 3)	cout<<"GABRIEL"<<endl;
		else if(x == 4)	cout<<"RICHARD"<<endl;
	}
	else if(r == 3 && c == 4){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"GABRIEL"<<endl;
		else if(x == 4)	cout<<"GABRIEL"<<endl;
	}
	else if(r == 4 && c == 4){
		if(x == 2)	cout<<"GABRIEL"<<endl;
		else if(x == 3)	cout<<"RICHARD"<<endl;
		else if(x == 4)	cout<<"GABRIEL"<<endl;
	}
}

int main(){
	
	freopen("inputCfinal2.in","r",stdin);
	freopen("outputCfinal2.txt","w",stdout);
	
	int ttt;
	cin>>ttt;
	for (int tt = 1; tt <= ttt; ++tt){
		cin>>x>>r>>c;
		cout<<"Case #"<<tt<<": ";
		solve();
	}

	return 0;

}