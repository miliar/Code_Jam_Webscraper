/*	magic-trick
 */

#include <iostream>

using namespace std;

void process(int old[4][4], int newa[4][4], int a, int b)
{
	int i, j, ans;
	int count = 0;
	int val[4];

	for(i=0 ; i<4 ; i++) {
		val[i] = old[a][i];
	}

	for(i=0 ; i<4 ; i++)
		for(j=0 ; j<4 ; j++) {
			if(val[j] == newa[b][i]) {
				ans = val[j];
				count++;
			}
		}
	
	if(count == 0)
		cout<<"Volunteer cheated!"<<endl;
	else if(count == 1)
		cout<<ans<<endl;
	else
		cout<<"Bad magician!"<<endl;
		
	return;
}

int main()
{
	int n, i, j, k;
	int old[4][4], newa[4][4];
	int a, b;
	
	cin>>n;
	
	for (i=1 ; i<=n ; i++) {
		cin>>a;
		a--;
		for(j=0 ; j<4 ; j++)
			for(k=0 ; k<4 ; k++)
				cin>>old[j][k];
	
		cin>>b;
		b--;
		for(j=0 ; j<4 ; j++)
			for(k=0 ; k<4 ; k++)
				cin>>newa[j][k];
		
		cout<<"Case #"<<i<<": ";
		process(old, newa, a, b);
	}
	return 0;
}
