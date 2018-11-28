#include<bits/stdc++.h>

using namespace std;

char a[109];

int main(){
	int test, ans;
	bool mas;

	/*freopen("B-large.in", "r", stdin);
	ofstream file;
	file.open("out_b.txt");
	*/
	scanf("%d", &test);
	getchar();
	for(int i=1; i<=test; i++){
		scanf("%s", &a);
		mas=true;
		ans=0;
		for(int j=strlen(a)-1; j>=0; j--){
			if(mas){
				if(a[j]!='+'){
					mas=false;
					ans++;
				}
			}
			else{
				if(a[j]!='-'){
					mas=true;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", i, ans);
		//file<<"Case #"<<i<<": "<<ans<<"\n";
	}
	//file.close();
	return 0;
}