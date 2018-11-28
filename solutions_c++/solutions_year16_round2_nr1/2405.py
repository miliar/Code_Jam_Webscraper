/*
  1.   0 z
       2 w
       4 u
       6 x
  2.   5 f
       8 g
  3.   3 t
       7 s
  4.   1 o
       9 i
*/
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
char a[10][10]={"ZERO", "ONE","TWO","THREE", "FOUR",
	"FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};
char b[15]="zoitufxsgi";
char str[2010];
int alpha[26];
vector<int>ans;
bool find(int n){
	for(int i=0;i<strlen(a[n]);i++){
		if(alpha[a[n][i]-'A']<=0) return false;
	}
	ans.push_back(n);
	for(int i=0;i<strlen(a[n]);i++){
		alpha[a[n][i]-'A']--;
	}
	return true;
}
int main(){
//	freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int ca=1;ca<=t;ca++){
		memset(alpha,0,sizeof(alpha));
		ans.clear();
		scanf("%s",str);
		int n=strlen(str);
		for(int i=0;i<n;i++){
			alpha[str[i]-'A']++;
		}
		while(find(0));
		while(find(2));
		while(find(4));
		while(find(6));
		while(find(5));
		while(find(8));
		while(find(3));
		while(find(7));
		while(find(1));
		while(find(9));
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<ca<<": ";
		for(int i=0;i<ans.size();i++){
			cout<<ans[i];
		}
		cout<<endl;
	}
	return 0;
}
