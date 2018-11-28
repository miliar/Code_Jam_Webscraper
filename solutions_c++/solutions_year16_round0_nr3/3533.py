#include <iostream>
#include <string>
#include <bitset>
#include <math.h>
using namespace std;


unsigned __int64 getDivides(bitset<32> tmp, int base, int N){
	unsigned __int64 num = 0;
	for (int i=0;i<N;i++){
		if (tmp[i]==1){
			num += pow(double(base),i);
		}
	}
	double curr = num;
	unsigned __int64 maxnum = sqrt(curr);
//	cout << num << "\t" << curr << "\t" << maxnum << endl;
	for (unsigned __int64 i=2;i<=maxnum;i++){
		if (num%i==0){
			return i;
		}
	}
	
	return -1;
}

int main()
{
	int T;
	int index = 1;
	cin >> T;
	/*
	bitset<32> test("110111");
	for (int i=2;i<=10;i++){
		cout << getDivides(test, i, 6);
	}
*/
	while(T--){
		int N, J;
		unsigned __int64 num = 0;
		cin >> N >> J;
		const int tmp = N;
		int count = 0;
		cout << "Case #" << index++ << ":" << endl;
		for (unsigned __int64 i=1;i<(1<<(N-1));i++){
			num ++;
			bitset<32> bset(num);
			bset[N-1] = 1;
			if (bset[0] == 0 || bset[N-1]==0)
				continue;
			bool fg = false;
			unsigned __int64 divides[12] = {0};
			for (int j=2;j<=10;j++){
				if ((divides[j]=getDivides(bset, j, N))== -1){
					fg = true;
					break;
				}
			}
			if (fg) continue;
			count++;
//			cout << count << ":\t";
			for (int j=N-1;j>=0;j--){
				cout << bset[j];
			}
			for (int j=2;j<=10;j++){
				cout << " " << divides[j];
			}
			cout << endl;
			if (count == J)
				break;
		}
	}
	return 0;
}