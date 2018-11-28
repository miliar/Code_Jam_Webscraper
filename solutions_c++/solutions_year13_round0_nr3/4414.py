#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <bitset>
#include <cmath>
using namespace std;
bitset<1001> fs;
int t,a,b;
void fill(int i){
	int n=pow(i,2);
	char c[33];
	itoa(n,c,10);
	string s(c);
	bool chk=true;
	for (int j=0; j<s.length(); j++){
		if (s[j]!=s[s.length()-j-1]) chk=false;
	}
	if (chk) fs[pow(i,2)]=1;
}
int main(){
	fs.reset();
	for (int i=1; i<10; i++){
		fill(i);
	}
	fill(11);
	fill(22);
	fill(33);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int i=0; i<t; i++){
		scanf("%d%d",&a,&b);
		int cnt=0;
		for (int j=a; j<=b; j++){
			if (fs[j]==1)
				cnt++;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
}