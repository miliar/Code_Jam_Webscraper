#include <iostream>
using namespace std;

long long t;
long long n, m;
long long arr[33] = { 0, };
long long tri[11] = { 0, };
long long b = 0;
long long d_arr[11][33] = { 1, };
long long result = 0;

void make_num(long long pre, long long val){
	long long as = 0;
	for (long long i = 1; i <= n; i++){
		if (arr[i] == 1){
			as++;
		}
	}
	if (as == n){
		b = 1;
		return;
	}

	if (arr[pre] == 0){
		arr[pre] = val;
		return;
	}
	else if (arr[pre] == 1){
		arr[pre] = 0;
		make_num(pre - 1, 1);
		return;
	}

}

long long prime_chk(long long gg, long long ptr){

	for (long long i = 2; i <= sqrt(gg); i++){
		if (gg%i == 0){
			tri[ptr] = i;
			return 1;
		}
	}
	return 0;
	//�Ҽ��� 0 ,, �Ҽ� �ƴϸ� 1
}

int main(){

	cin >> t;
	cin >> n >> m;
	cout << "Case #1:" << endl;
	arr[1] = 1;
	arr[n] = 1;
	long long aa = 0;
	while (1){
		if (aa == 1){
			//n�ڸ� ���� �ϳ� ����.(ù°�� ������ ���� 1��)
			make_num(n-1,1);
		}

		for (long long i = 2; i <= 10; i++){
			for (long long j = n; j >= 1; j--){
				d_arr[i][j] = 1;
			}
		}
		for (long long i = 2; i <= 10; i++){
			for (long long j = n-1; j >= 1; j--){
				d_arr[i][j] = d_arr[i][j + 1] * i;
			}
		}
		
		for (long long i = 2; i <= n-1; i++){
			for (long long j = 2; j <= 10; j++){
				if (arr[i] == 0){
					d_arr[j][i] = 0;
				}
			}
		}

		//���� ���ڿ� �� �ڸ��� 2~10���� ���ؼ� ���� ���� �Ҽ��� ������ �� ���� ����
		long long complete = 0;
		for (long long i = 2; i <= 10; i++){
			long long pos_num = 0;
			for (long long j = 1; j <= n; j++){
				pos_num += d_arr[i][j];
			}
			tri[i] = pos_num;
			if (prime_chk(pos_num,i)==0){
				break;
			}
			complete = i;
		}
		if (complete != 10){
			if (aa == 0){
				aa = 1;
			}
			continue;
		}

		////�Ҽ��� ���� �� ���Դٸ� ���� �װ� �� �ڸ��� ��Ʈ����� ��(1�� �ڽ��� �ƴ� ��)�� ���Ѵ�.
		//for (long long i = 2; i <= 10; i++){
		//	long long idx = 2;
		//	while (1){
		//		if (tri[i] % idx == 0 && idx!=tri[i]){
		//			tri[i] = idx;
		//			break;
		//		}
		//		idx++;
		//	}
		//}

		//�������� ���� ���ڿ� �� ��Ʈ����� ���� ���
		for (long long i = 1; i <= n; i++){
			cout << arr[i];
		}cout << " ";
		for (long long i = 2; i <= 10; i++){
			if (i == 10){
				cout << tri[i] << endl;
			}
			else{
				cout << tri[i] << " ";
			}	
		}
		//����� ���� ���ؼ� ���� m�� �������� while��
		result++;
		if (result == m){
			break;
		}

		if (b == 1){
			break;
		}
		
		if (aa == 0){
			aa = 1;
		}
	}

	return 0;
}