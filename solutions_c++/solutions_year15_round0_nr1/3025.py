#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N;
	int SMax;
	int ans=0,ansc;
	scanf("%d",&T);

	for(int t=1;t<=T;t++){
		ans=0;ansc=0;
		char input[1010]={0,};
		scanf("%d%s",&N,input);
		string a = input;
		int cnt=0;
		for(int i=0;i<a.length();i++){
			if(a[i]-'0' ==0  && cnt < i+1){
				ansc ++;
				cnt ++;
			}
			if(a[i]!='0'){
				ans += ansc;
				ansc=0;
			}
			cnt += (a[i]-'0');
		}

		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}