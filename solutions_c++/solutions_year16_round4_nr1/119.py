#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

char win(char a, char b){
	if (a=='P'&&b=='R') return a;
	if (a=='R'&&b=='P') return b;
	
	if (a=='S'&&b=='P') return a;
	if (a=='P'&&b=='S') return b;
	
	if (a=='S'&&b=='R') return b;
	if (a=='R'&&b=='S') return a;
	assert(0);
}

char isvalid(vector<char> t){
	if (t[0]==t[1]) return 0;
	if (t[2]==t[3]) return 0;
	char w1=win(t[0], t[1]);
	char w2=win(t[2], t[3]);
	if (w1==w2) return 0;
	return win(w1, w2);
}

pair<string, char> best(vector<pair<string, char> > t){
	sort(t.begin(), t.end());
	string b;
	char c;
	while (1){
		vector<char> a;
		string tv;
		for (int i=0;i<4;i++){
			a.push_back(t[i].S);
			tv+=t[i].F;
		}
		if (char asd=isvalid(a)){
			if ((int)b.size()==0||tv<b){
				b=tv;
				c=asd;
			}
		}
		if (!next_permutation(t.begin(), t.end())) break;
	}
	return {b, c};
}

vector<pair<string, char> > s4(vector<pair<string, char> > t){
	sort(t.begin(), t.end());
	if ((int)t.size()==2){
		if (t[0].S==t[1].S) return {};
		return {{t[0].F+t[1].F, 'a'}};
	}
	else{
		vector<int> u(t.size());
		int gs=(int)t.size()/4;
		int cp=0;
		int cr=0;
		int cs=0;
		for (int i=0;i<(int)t.size();i++){
			if (t[i].S=='P') cp++;
			if (t[i].S=='S') cs++;
			if (t[i].S=='R') cr++;
		}
		if (cp>gs*2||cr>gs*2||cs>gs*2){
			return {};
		}
		if (cp<gs||cr<gs||cs<gs) return {};
		
		vector<pair<string, char> > v;
		while (cp>gs){
			int fp=0;
			int fr=0;
			int fs=0;
			vector<pair<string, char> > tt;
			for (int i=0;i<(int)t.size();i++){
				if (u[i]==0){
					if (fp<2&&t[i].S=='P'){
						u[i]=1;
						fp++;
						tt.push_back(t[i]);
					}
					if (fr<1&&t[i].S=='R'){
						u[i]=1;
						fr++;
						tt.push_back(t[i]);
					}
					if (fs<1&&t[i].S=='S'){
						u[i]=1;
						fs++;
						tt.push_back(t[i]);
					}
				}
			}
			cp--;
			auto lol=best(tt);
			v.push_back(lol);
		}
		while (cr>gs){
			int fp=0;
			int fr=0;
			int fs=0;
			vector<pair<string, char> > tt;
			for (int i=0;i<(int)t.size();i++){
				if (u[i]==0){
					if (fp<1&&t[i].S=='P'){
						u[i]=1;
						fp++;
						tt.push_back(t[i]);
					}
					if (fr<2&&t[i].S=='R'){
						u[i]=1;
						fr++;
						tt.push_back(t[i]);
					}
					if (fs<1&&t[i].S=='S'){
						u[i]=1;
						fs++;
						tt.push_back(t[i]);
					}
				}
			}
			cr--;
			auto lol=best(tt);
			v.push_back(lol);
		}
		while (cs>gs){
			int fp=0;
			int fr=0;
			int fs=0;
			vector<pair<string, char> > tt;
			for (int i=0;i<(int)t.size();i++){
				if (u[i]==0){
					if (fp<1&&t[i].S=='P'){
						u[i]=1;
						fp++;
						tt.push_back(t[i]);
					}
					if (fr<1&&t[i].S=='R'){
						u[i]=1;
						fr++;
						tt.push_back(t[i]);
					}
					if (fs<2&&t[i].S=='S'){
						u[i]=1;
						fs++;
						tt.push_back(t[i]);
					}
				}
			}
			cs--;
			auto lol=best(tt);
			v.push_back(lol);
		}
		return v;
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		vector<pair<string, char> > lol;
		for (int i=0;i<r;i++){
			lol.push_back({"R", 'R'});
		}
		for (int i=0;i<p;i++){
			lol.push_back({"P", 'P'});
		}
		for (int i=0;i<s;i++){
			lol.push_back({"S", 'S'});
		}
		
		while ((int)lol.size()>1){
			lol=s4(lol);
		}
		if ((int)lol.size()==0){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<lol[0].F<<endl;
		}
	}
}