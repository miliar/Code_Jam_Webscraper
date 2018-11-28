#include <bits/stdc++.h>

using namespace std;

int n , j , cnt , mod[12] = {0,0,3,2,5,2,7,2,9,2,11} , mul[15][50];
struct status{
	unsigned x ;
	int p[11];
};
vector < string > ans;

void check( status st ){
	for(int i = 2 ; i <= 10 ; ++ i){
		if(st.p[i] != 0){
			return;
		}
	}
	string os;
	for(int i = n - 1 ; i >= 0 ; -- i){
		if(st.x >> i & 1) os.push_back('1');
		else os.push_back('0');
	}
	ans.push_back( os );
}

bool dfs(int cur , status st){
	if( cur == n ){
		check( st );
		if( ans.size() == j ) return true;
		return false;
	}else{
		status newst = st;
		newst.x |= (1 << cur);
		for(int i = 2 ; i <= 10 ; ++ i){
			newst.p[i] = ( newst.p[i] + mul[i][cur] ) % mod[i];
		}
		if(dfs( cur + 1 , newst )) return true;
		if( cur != 0 && cur != n - 1) if(dfs( cur + 1 , st )) return true;
	}
	return false;
}

int main(int argc,char *argv[]){
	//freopen("out.txt" , "w" , stdout );
	int Case , cas = 0;
	scanf("%d",&Case);
	for(int i = 2 ; i <= 10 ; ++ i){
		mul[i][0]=1;
		for(int j = 1 ; j < 40 ; ++ j) mul[i][j] = mul[i][j - 1] * i % mod[i];
	}
	while(Case--){
		scanf("%d%d",&n,&j);
		status sb;
		sb.x=0;
		for(int i = 2 ; i <= 10 ; ++ i) sb.p[i] = 0;
		dfs( 0 , sb );
		printf("Case #%d:\n" , ++ cas);
		for(auto it : ans){
			cout << it;
			for(int i = 2 ; i <= 10 ; ++ i) cout << " " << mod[i];
			cout << endl;
		}
	}
	return 0;
}