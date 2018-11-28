#include<iostream>
using namespace std;
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<cmath>
#include<set>
#include<ctime>
#include<stack>
#include<list>
typedef  pair<int,int> pii;
#define rep(i,j,n) for(i=j;i<n;i++)
#define pb push_back
#define sz(a) a.size()
#define ff first
#define ss second 
#define lli long long int

int conv[5][5];

int main() {
		
	ios::sync_with_stdio(false);
	freopen ("inp.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	
	
	conv[1][1]= 1;
	conv[1][2]= 2;
	conv[1][3]= 3;
	conv[1][4]= 4;
	
	conv[2][1]= 2;
	conv[2][2]= -1;
	conv[2][3]= 4;
	conv[2][4]= -3;
	
	conv[3][1]= 3;
	conv[3][2]= -4;
	conv[3][3]= -1;
	conv[3][4]= 2;
	
	conv[4][1]= 4;
	conv[4][2]= 3;
	conv[4][3]= -2;
	conv[4][4]= -1;
	
	
	int t,l,x,i,cur,ca=0,state,gg;
	cin>>t;
	string s,s1;
	
	/*rep(i,1,5)
	rep(j,1,5){
		cout<<conv[i][j]<<" \n"[j==4];
	}*/
	
	while(t--){
		ca++;
		state = 0;
		cur = 1;
		cin>>l>>x;
		cin>>s;
		s1 = s;
		rep(i,0,x){
			s = s+s1;
		}
		rep(i,0,x*l){
			int sign = 1;
			if(cur<0)	sign = -1;
			
			if(s[i] == 'i')			gg = 2;
			else if (s[i] == 'j')	gg = 3;
			else if (s[i] == 'k')	gg = 4;
			
			cur = sign * conv[abs(cur)][gg];
			
			if(state == 0){
				if(cur == 2)	state = 1;
			}
			else if(state == 1){
				if(cur == 4)	state = 2;
			}
		//	cout<<cur<<" ";
		}
		//cout<<endl;
		if(cur == -1 and state == 2)	cout<<"Case #"<<ca<<": YES\n";
		else 						cout<<"Case #"<<ca<<": NO\n";
		
	}
	
	
	return 0;
}
