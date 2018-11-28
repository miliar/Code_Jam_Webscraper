#include <iostream>

using namespace std;

int main() {
	int T,n=1,a1[4];
	cin>>T;
	while(n<=T) {
		int row1,row2, count = 0, temp1, temp2;
		cin>>row1;
		for(int i=0;i<16;i++) {
			cin>>temp1;
			if(i<4*row1-4 || i>=4*row1) continue;
			a1[i%4] = temp1;
		}

		cin>>row2;
		for(int i=0;i<16;i++) {
			cin>>temp2;
			if(i<4*row2-4 || i>=4*row2) continue;
			for(int j=0;j<4;j++)
				if(a1[j] == temp2) {
					temp1 = temp2;
					count++;
				}
		}

		cout<<"Case #"<<n<<": ";
		if(count == 0) cout<<"Volunteer cheated!"<<endl;
		else if(count == 1) cout<<temp1<<endl;
		else cout<<"Bad Magician!"<<endl;

		n++;
	}
	return 0;
}