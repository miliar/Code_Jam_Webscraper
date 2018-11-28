#include <iostream>
#include<stdlib.h>
int a[10][10],vis[100];

using namespace std;
void solve(int C)
{
	int b,c;
	cin >> b;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin >> a[i][j];
	for(int i=0;i<4;i++) vis[a[b-1][i]]++;
	cin >> c;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin >> a[i][j];
	for(int i=0;i<4;i++) vis[a[c-1][i]]++;
	int cnt=0,last=-1;
	for(int i=1;i<=16;i++)
	{
		if(vis[i]==2) 
		{
			cnt++;
			last=i;
		}
	}
	if(cnt==0) cout << "Case #" << C << ": Volunteer cheated!" << endl;
	if(cnt==1) cout << "Case #" << C << ": " << last << endl;
	if(cnt>=2) cout << "Case #" << C << ": Bad magician!" << endl;
	
	for(int i=0;i<20;i++) vis[i]=0;
	return;
}
int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("B.txt","w",stdout);
	//fcout << "A";
	int t;
	cin >> t;
	for(int i=0;i<t;i++) solve(i+1);
}