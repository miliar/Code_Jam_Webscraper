#include<bits/stdc++.h>

using namespace std;

int a[2509];
int b[59];

int main(){
	int test, n, t, v, pos;
	char c;

	/*freopen("B-large.in", "r", stdin);
	ofstream file;
    file.open ("out_b.txt");*/

	scanf("%d", &test);
	for(int i=1; i<=test; i++){
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		t=(2*n)-1;
		for(int j=0; j<t; j++){
			for(int k=0; k<n; k++){
				scanf("%d", &v);
				a[v]++;
			}
		}
		pos=0;
		for(int j=1; j<=2500; j++){
			if(a[j]%2==1){
				b[pos++]=j;
			}
		}
		printf("Case #%d:", i, b);
		//file<<"Case #"<<i<<":";
		for(int j=0; j<pos; j++){
			printf(" %d", b[j]);
			//file<<" "<<b[j];
		}
		printf("\n");
		//file<<endl;
	}
	//file.close();
	return 0;
}