#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define pb push_back
#define ft first
#define se second
#define mp make_pair
char mu(char a, char b){
	if(a=='c') return b;
	if(b=='c') return a;
	if(a=='i' && b=='i') return 'v';
	if(a=='i' && b=='j') return 'k';
	if(a=='i' && b=='k') return 'n';
	if(a=='i' && b=='m') return 'c';
	if(a=='i' && b=='n') return 'b';
	if(a=='i' && b=='b') return 'j';
	if(a=='i' && b=='v') return 'm';

	if(a=='j' && b=='i') return 'b';
	if(a=='j' && b=='j') return 'v';
	if(a=='j' && b=='k') return 'i';
	if(a=='j' && b=='m') return 'k';
	if(a=='j' && b=='n') return 'c';
	if(a=='j' && b=='b') return 'm';
	if(a=='j' && b=='v') return 'n';

	if(a=='k' && b=='i') return 'j';
	if(a=='k' && b=='j') return 'm';
	if(a=='k' && b=='k') return 'v';
	if(a=='k' && b=='m') return 'n';
	if(a=='k' && b=='n') return 'i';
	if(a=='k' && b=='b') return 'c';
	if(a=='k' && b=='v') return 'b';

	if(a=='m' && b=='i') return 'c';
	if(a=='m' && b=='j') return 'b';
	if(a=='m' && b=='k') return 'j';
	if(a=='m' && b=='m') return 'v';
	if(a=='m' && b=='n') return 'k';
	if(a=='m' && b=='b') return 'n';
	if(a=='m' && b=='v') return 'i';

	if(a=='n' && b=='i') return 'k';
	if(a=='n' && b=='j') return 'c';
	if(a=='n' && b=='k') return 'm';
	if(a=='n' && b=='m') return 'b';
	if(a=='n' && b=='n') return 'v';
	if(a=='n' && b=='b') return 'i';
	if(a=='n' && b=='v') return 'j';

	if(a=='b' && b=='i') return 'n';
	if(a=='b' && b=='j') return 'i';
	if(a=='b' && b=='k') return 'c';
	if(a=='b' && b=='m') return 'j';
	if(a=='b' && b=='n') return 'm';
	if(a=='b' && b=='b') return 'v';
	if(a=='b' && b=='v') return 'k';	

	if(a=='v' && b=='i') return 'm';
	if(a=='v' && b=='j') return 'n';
	if(a=='v' && b=='k') return 'b';
	if(a=='v' && b=='m') return 'i';
	if(a=='v' && b=='n') return 'j';
	if(a=='v' && b=='b') return 'k';
	if(a=='v' && b=='v') return 'c';	
	return 'i';
}
int main(int argc, char const *argv[]){
	int t,p;
	cin>>t;
	p=t;
	while(t--){
		string inp,act;
		int s,l,last;
		cin>>l>>s;
		cin>>act;
		inp=act;
		for (int i = 1; i < s; ++i) act+=inp;
		char sum[l*s];
		last=l*s-1;
		sum[0]=act[0];
		for (int j = 1; j <=last; ++j){
			sum[j]=mu(sum[j-1],act[j]);
		}
		bool comp=false;
		if(sum[last]=='v'){
			for (int j = 0; j <=last && !comp; ++j){
				if(sum[j]=='i'){
					for (int i = j+1; i <=last && !comp; ++i){
						if(sum[i]=='k'){
							cout<<"Case #"<<p-t<<": "<<"YES"<<endl;
							comp=true;
						}
					}
				}
			}
		}
		if(!comp) cout<<"Case #"<<p-t<<": "<<"NO"<<endl;
	}
	return 0;
}