#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000000000
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;

int mat[5][5];

void pre(){
	mat[1][1]=1; mat[2][1]=2; mat[3][1]=3; mat[4][1]=4;
	mat[1][2]=2; mat[2][2]=-1; mat[3][2]=-4; mat[4][2]=3;
	mat[1][3]=3; mat[2][3]=4; mat[3][3]=-1; mat[4][3]=-2;
	mat[1][4]=4; mat[2][4]=-3; mat[3][4]=2; mat[4][4]=-1;
}

int main(){
	int i,t,l,x;
	pre();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	string s;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>l>>x;
		cin>>s;
		string tmp="";
		while(x--){
			tmp=tmp+s;
		}
		s=tmp;
		for(i=0;i<s.length();i++){
			if(s[i]=='i')
			s[i]='2';
			else if(s[i]=='j')
			s[i]='3';
			else
			s[i]='4';
		}
		int idx1=-1,idx2=-1;
		int val=1,neg=0;
		for(i=0;i<s.length();i++){
			int prod=mat[val][s[i]-'0'];
			if(prod<0)
			neg++;
			val=abs(prod);
			if(val==2){
				if(((neg%2)==0)&&(idx1==-1))
				idx1=i;
			}
			if(val==4){
				if(((neg%2)==0)&&(idx1!=-1))
				idx2=i;
			}
		}
		if((val==1)&&(neg&1)&&(idx2!=-1))
		printf("YES\n");
		else
		printf("NO\n");
	}
	fclose(stdout);
	return 0;
}
