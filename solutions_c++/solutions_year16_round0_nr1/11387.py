#include<iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int N;
	int T;
	cin >> T;
	for(int i = 1; i<= T ; i++)
	{
		cin >> N;
		if(!N) {cout << "Case #" << i << ": " << "INSOMNIA" <<endl; continue;}
		int j = 1;
		int temp;
		int count = 0;
		int is_seen[10] = {0};
		do
		{
			temp = (j++)*N;
			do
			{
				if(is_seen[temp%10] == 0)
					count++;
				is_seen[temp%10] = 1;
			}while(temp/=10);
			//for(int k = 0;k<10;k++)
			//	cout << is_seen[k] << " ";
			//cout << endl;
			
		}while(count != 10);
		cout << "Case #" << i << ": " << (j-1)*N << endl;
	}
	return 0;
}