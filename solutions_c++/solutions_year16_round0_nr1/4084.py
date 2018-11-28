#include <iostream>
using namespace std;

bool ifFinish(bool digits[]){
//	cout << "digits: ";
	for (int i=0;i<10;i++){
		if (!digits[i]){
//			cout << i << endl;
			return false;
		}
	}
	return true;
}

int main()
{
	int T;
	int index = 1;
	cin >> T;

	while(T--){
		unsigned int N,tmp;
		cin >> tmp;
		N = tmp;
		
		unsigned int maxnum = 1<<31;
		int i=1;
		bool flag = false;
		bool digits[10] = {false};
		for (int i=0;i<10;i++)
			digits[i] = false;
		while(N < maxnum){
//			cout << "index = " << index << "\t" << N << "\t";
			if (N==0){
				break;
			}
			unsigned int s = N;
			while(s!=0){
				int x = s%10;
				digits[x] = true;
				s/=10;
			}
			if (ifFinish(digits)){
				cout << "Case #" << index++ << ": " << N << endl;
				flag = true;
				break;
			}
			i++;
			N = i*tmp;
		}
		if (!flag){
			cout << "Case #" << index++ << ": INSOMNIA" << endl;
		}
	}
}