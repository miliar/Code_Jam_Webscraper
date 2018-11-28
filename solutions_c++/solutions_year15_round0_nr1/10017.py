#include<iostream>
#include<string>
using namespace std;



void main(){
	int T, prob=1;
	for (cin >> T; T--;){
		int r = 0;
		int c = 0;

		int sMax;
		string list;
		cin >> sMax;
		cin >> list;

		for (int i = 0; i <= sMax; i++)
		{
			int si = list[i] - '0';
			
			if (si > 0)
			{
				if (c < i) r += i - c;
				c += si + r;
			}
			
			
		}
		cout << "Case #" << prob++ << ": "<<r<<endl;
	}
}

