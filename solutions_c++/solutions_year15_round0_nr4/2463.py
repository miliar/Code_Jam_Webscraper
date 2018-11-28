/*input
4
2 2 2
2 1 3
4 4 1
3 2 3
*/
#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
/*It's Another One We're Winning!
We're Really On the Go!
Heaps Of Runs And Wickets!
Now We're Putting On A Show!
Cause You Gotta Get Used To
Being Beaten By The Boys From
CHENNAI, CHENNAI.
WHO THE FUCK IS CHENNAI??
__ Games, To Go
Till The Skipper Lifts The Trophy Letting
EveryBody Know. That You Gotta Get
Used To Being Beaten By The Boys From
CHENNAI, CHENNAI.
WE ARE FUCKING CHENNAI !!*/
void solve(){
	int x,r,c;
	cin>>x>>r>>c;
	switch (x){
		case 1:
			cout<<"GABRIEL\n";
			break;

		case 2:
			if((r*c)%2==0)
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
			break;
		case 3:
			if((r*c)%6==0 || (r==3 && c==3))
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
			break;
		case 4:
			if((r*c)%12==0 || (r==4 && c==4))
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
			break;

	}
}
int main(){
	ios_base::sync_with_stdio(false);
	freopen("C:/Users/Enjoy/Desktop/input.txt","r",stdin);
	freopen("C:/Users/Enjoy/Desktop/output.txt","w",stdout);
	int t;cin>>t;
	int xx=1;
	while(t--){
		cout<<"Case #"<<xx++<<": ";
		solve();
	}
	return 0;
}