#include <iostream>

using namespace std;

int main()
{
	int t, a[2], cards[2][4][4], i, j, k, co, e;

	cin>>t;
	for(int ca=1;ca<=t;ca++){
		cout<<"Case #"<<ca<<": "; 
		for(k=0;k<2;k++){
			cin>>a[k];
			a[k]--;
			for(i=0;i<4;i++){
				for(j=0;j<4;j++){
					cin>>cards[k][i][j];
				}
			}
		}
		co=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(cards[0][a[0]][i]==cards[1][a[1]][j])	{co++;e=cards[1][a[1]][j];}
			}
		}
		if(co==1)	cout<<e;
		else if(co>1)	cout<<"Bad magician!";
		else	cout<<"Volunteer cheated!";
		if(ca<t)	cout<<"\n";
	}

	return 0;
}