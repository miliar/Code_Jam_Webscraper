#include <bits/stdc++.h>
using namespace std;
//8192
char arr[10000];
int T, N, R, P, S, SET;
string ans;
void loop(int i){
	int subt = 0;
	int PT=0,RT=0,ST=0;

	if(i== (1<<(N+1))-1) {
		string s (arr, (1<<(N))-1, (1<<(N)));
		if(s.compare(ans)<0){
			ans = s;
			SET = 1;
		}
		//cout<<ans<<endl;
		return;
	}

	if(i%2==0)subt=1;
	if(arr[i/2 - subt]=='P' && PT==0 && R){
		arr[i]='P';
		arr[i+1]='R';
		R--;
		loop(i+2);
		R++;
		PT++;
	}

	if(arr[i/2 - subt]=='P' && PT==1 && R){
		arr[i]='R';
		arr[i+1]='P';
		R--;
		loop(i+2);
		R++;
		PT++;
	}

	if(arr[i/2 - subt]=='R' && RT==0 && S){
		arr[i]='R';
		arr[i+1]='S';
		S--;
		loop(i+2);
		S++;
		RT++;
	}

	if(arr[i/2 - subt]=='R' && RT==1 && S){
		arr[i]='S';
		arr[i+1]='R';
		S--;
		loop(i+2);
		S++;
		RT++;
	}

	if(arr[i/2 - subt]=='S' && ST==0 && P){
		arr[i]='P';
		arr[i+1]='S';
		P--;
		loop(i+2);
		P++;
		ST++;
	}

	if(arr[i/2 - subt]=='S' && ST==1 && P){
		arr[i]='S';
		arr[i+1]='P';
		P--;
		loop(i+2);
		P++;
		ST++;
	}


}

int main(){
	
	cin>>T;
	int top;
	for(int i=0; i<T; i++) {

	ans = "ZZ";
		cout<<"Case #"<<i+1<<": ";
		cin>>N>>R>>P>>S;
		SET=0;
		top = 0;
		if(P){
			P--;
			//func(top, 'P');
			arr[top]='P';
			loop(top+1);
			P++;
		}
		top = 0;
		if(R){
			R--;
			//func(top, 'P');
			arr[top]='R';
			loop(top+1);
			R++;
		}
		top = 0;
		if(S){
			S--;
			//func(top, 'P');
			arr[top]='S';
			loop(top+1);
			S++;
		}

		if(SET) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
}