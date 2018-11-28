#include<string>
#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
using namespace std;
long long check_prime(long long num) {
	if (num <= 1)
		return -1;
	else if (num == 2)
		return -1;
	else if (num % 2 == 0)
		return 2;
	else {
		bool prime = true;
		long long divisor = 3;
		double num_d = static_cast<double>(num);
		long long upperLimit = static_cast<int>(sqrt(num_d) + 1);

		while (divisor <= upperLimit) {
			if (num % divisor == 0)
				return divisor;
			divisor += 2;
		}
		return -1;
	}
}
int main() {
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C_coin.out");
	int n,j;
	fin>>n>>n>>j;
	short num[n];
	for(int i=0;i<n;i++)num[i]=0;
	num[0]=1;
	num[n-1]=1;
	int valid_cnt=0;
	vector< vector<int> > validnums;
	vector< vector<int> > divisors;
	for(int zzz=0; zzz<(int)exp2(n-2); zzz++){
		//for(int i=n-1; i>=0; i--)cout<<num[i];
		//cout<<endl;
		bool allthrough_flag = true;
		vector<int> curr_div;
		for(int base=2; base<=10; base++){
			long long tempdiv;
			long long number=0;
			for(int i=0;i<n;i++)
				if(num[i]) number+=pow(base,i);
			tempdiv=check_prime(number);
			if(tempdiv!=-1){
				curr_div.push_back(tempdiv);
			}
			else{
				cout<<number<<endl;
				allthrough_flag = false;
				break;
			}
		}
		if(allthrough_flag){
			vector<int> currnum;
			for(int i=n-1; i>=0; i--)currnum.push_back(num[i]);
			validnums.push_back(currnum);
			divisors.push_back(curr_div);
			valid_cnt++;
		}
		if(valid_cnt>=j)
			break;






		num[1]++;
		for(int i=1; i<n-1; i++){
			if(num[i]>=2){
				num[i+1]++;
				num[i]-=2;
			}
		}
	}
	fout<<"Case #1:"<<endl;

	for(int zzz=0; zzz<j; zzz++){
		for(int i=0;i<n;i++) fout<<validnums[zzz][i];
		fout<<' ';
		for(int i=0;i<9;i++){
			fout<<divisors[zzz][i];
			if(i<9) fout<<' ';
		}
		fout<<endl;
	}
	return 0;
}
