// Submitted by Silithus @ Macau
#include <iostream>

using namespace std;

void work(void)
{
	int row[17],ans1,ans2,ans,cnt=0,r,c,i;
	
	cin >> ans1;
	for(r=1; r<=4; r++)
		for(c=0; c<4; c++) {
			cin >> i;
			row[i] = r;
		}
	
	cin >> ans2;
	for(r=1; r<=4; r++)
		for(c=0; c<4; c++) {
			cin >> i;
			if( r==ans2 && row[i]==ans1 ) {
				cnt++;
				ans = i;
			}
		}
	
	if( cnt == 1 )
		cout << ans;
	else
		cout << (cnt==0 ? "Volunteer cheated!" : "Bad magician!");
}

int main(void)
{
	int t,T;
	
	cin >> T;
	for(t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		work();
		cout << endl;
	}
	
	return 0;
}
