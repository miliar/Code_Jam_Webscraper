#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;


bool hash[20];
static int cc = 1;
void output() {
	printf("Case #%d: ", cc++);
}
int main() {
	int cas;	
	int row_f,row_s,idx;
	freopen("A--small-attempt0.in", "r", stdin);
	freopen("A--small-attempt0.out", "w", stdout);
	cin>>cas;
	while(cas--) {
		memset(hash, false,sizeof(hash));
		cin>>row_f;
		for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++) {
			int k;
			cin>>k;
			if(i == row_f - 1)  {
				//cout<<k<<endl;
				hash[k] = true;
			}
		}
		int cnt = 0;
		cin>>row_s;
		for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++) {
			int k;
			cin>>k;
			if(i == row_s - 1) {
				
				if(hash[k])idx = k,cnt ++;
			}
		}
		output();
		if(cnt == 1)cout<<idx<<endl;
		else if(cnt > 1)puts("Bad magician!");
		else puts("Volunteer cheated!");
	}
}