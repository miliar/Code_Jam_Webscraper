#include<iostream>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

    int n, m1[4][4], r1, m2[4][4], r2, result, cnt, count=0;
    cin>>n;
	while(count!=n) {
		cnt=0;
		count++;
		cin>>r1;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>m1[i][j];
			}
		}
		cin>>r2;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>m2[i][j];
			}
		}

		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				if(m1[r1-1][i]==m2[r2-1][j]) {
					result=m1[r1-1][i]; cnt++;
				}
			}
		}

		cout<<"Case #"<<count<<": ";
		if(cnt==0) {cout<<"Volunteer cheated!\n";}
		else if(cnt>1) {cout<<"Bad magician!\n";}
		else {cout<<result<<endl;}
	}
    return 0;
}