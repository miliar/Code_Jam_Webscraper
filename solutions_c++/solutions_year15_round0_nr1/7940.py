#include <iostream>
using namespace std;

long T, M, arr[1005], f, total, diff;
char S[1005];

int main() {
	cin>>T;
	for(int j=1; j<=T; j++)
	{
		cin>>M;
		cin>>S;
		for(int i =0; i<=M; i++)
		{
			arr[i] = S[i] - '0';
		}
		
		
		//logic
		f = 0;
		total = 0;
		for(int i =0; i<=M; i++)
		{
			if(arr[i] && (total)<i)
			{
				diff=(i - total);
				f+=diff;
				total+=diff;
			}
			total += arr[i];
		}
		
		cout<<"Case #"<<j<<": "<<f<<endl;
		
		
	}
	return 0;
}
