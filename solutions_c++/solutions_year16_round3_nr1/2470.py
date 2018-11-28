#include<bits/stdc++.h>
#define REP(a,b,c) for(int a=b;a<c;a++)
#define fst first
#define snd second
#define pb push_back
#define sz(v) ((int)v.size())
#define mp make_pair
using namespace std;
typedef pair<int,int> pii;
vector<pii>v;
int main(){
  int t,n,in;
  cin>>t;
  REP(caso,1,t+1){
  	v.clear();
  	cin>>n;
  	REP(i,0,n){
  		cin>>in;
  		v.pb(mp( in , i ));
  	}
  	sort(v.begin(),v.end());
  	cout<<"Case #"<<caso<<":";
  	if(n == 2){
  		REP(i,0,v[0].fst) cout<<" "<<"AB";
  	}
  	else if(n==3){
  		while(1){
  			if(v[2].fst==0) break;
  			if(v[2].fst == 1 && v[1].fst == 1 && v[0].fst == 1 ){
  				cout<<" "<<(char)(v[0].snd+65);
  				v[sz(v)-3].fst--;
  			}
  			cout<<" "<<(char)(v[sz(v)-1].snd +65)<<(char)(v[sz(v)-2].snd+65);
  			v[sz(v)-1].fst--;
  			v[sz(v)-2].fst--;
  			sort(v.begin(),v.end());
  		}
  	}
  	else{
  		while(1){
  			if(v[sz(v)-1].fst==0) break;
  			if(v[sz(v)-1].fst == 1 && v[sz(v)-2].fst == 1 && v[sz(v)-3].fst == 1 && v[sz(v)-4].fst == 0){
  				cout<<" "<<(char)(v[sz(v)-3].snd+65);
  				v[sz(v)-3].fst--;
  			}
  			cout<<" "<<(char)(v[sz(v)-1].snd +65)<<(char)(v[sz(v)-2].snd+65);
  			v[sz(v)-1].fst--;
  			v[sz(v)-2].fst--;
  			sort(v.begin(),v.end());
  		}
  	}
  	cout<<endl;
  }
  return 0;
}
