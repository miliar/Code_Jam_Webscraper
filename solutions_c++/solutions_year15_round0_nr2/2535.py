#include <iostream>
using namespace std;

int main(){

	int T;
	int Diner;
	int Pi[1000], BPi[1000], Pi2[1000];
	int result, result2, result3;
	int sum, Bsum;
	int flag, Bflag;
	double sum2, Bsum2;
	int max;

	int order[3];

	cin >> T;
	for (int i = 1; i <= T; i++){
		result = 0;
		sum = 0;
		sum2 = 0;
		flag = 0;
		max = 0;
		Bflag = 0;
		Bsum = 0;
		Bsum2 = 0;
		result2 = 0;
		result3 = 0;
		order[0] = 0;
		order[1] = 0;
		order[2] = 0;

		cin >> Diner;
		for (int j = 0; j < Diner; j++){
			cin >> Pi[j];
			sum += Pi[j];
			if (max < Pi[j]) max = Pi[j];
			if (order[0] < Pi[j]){
				order[1] = order[0];
				order[0] = Pi[j];
			}
			BPi[j] = Pi[j];
			Bsum += BPi[j];
			Pi2[j] = Pi[j];
		}
		sum2 = sqrt(sum);
		sum = (int)sum2;
		Bsum = sum;
		if (sum < sum2) sum++;

		for (int j = 0; j < Diner; j++){
			while (Pi2[j] > order[1] && order[1]>0){
				Pi2[j] -= order[1];
				result3++;
			}
			while (Pi[j] > sum){
				Pi[j] -= sum;
				result++;
				flag = 1;
			}
			while (BPi[j] > Bsum){
				BPi[j] -= Bsum;
				result2++;
				Bflag = 1;
			}
			
		}
		result += sum;
		result2 += Bsum;
		result3 += order[1];

		if (flag == 0 || max < result){
			result = max;
		}
		if (Bflag == 0){
			result2 = max;
		}
		
		if (result > result2){
			result = result2;
		}

		if (result > result3 && result3 > 0){
			result = result3;
		}
		
		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}