#include <iostream>
using namespace std;

int main(){
	int kolk;
	cin >> kolk;

	for(int i(0);i<kolk;i++){
		int a,x;
		cin >> a;
		for(int j(1);j<a;j++){
			cin >> x >> x >> x >> x;
		}
		int tab[16];
		for(int j(0);j<16;j++)tab[j]=0;
		cin >> x;
		tab[x-1]++;
		cin >> x;
		tab[x-1]++;
		cin >> x;
		tab[x-1]++;
		cin >> x;
		tab[x-1]++;
		for(int j(a);j<4;j++){
			cin >> x >> x >> x >> x;
		}

		// 2.
		cin >> a;
		for(int j(1);j<a;j++){
			cin >> x >> x >> x >> x;
		}
		for(int j(0);j<4;j++){
			cin >> x;
			tab[x-1]++;
		}

		for(int j(a);j<4;j++){
			cin >> x >> x >> x >> x;
		}
		x=0;
		int y=0;
		for(int j(0);j<16;j++){
			if(tab[j]==2){
				x++;y=j+1;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(x==1)cout << y << endl;
		else if(x>1)cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;

	}
	return 0;
}


