#include <iostream>

using namespace std;

int main()
{
	int i, j, k, T, A, B, cnt;
	int palinSq[5] = {1, 4, 9, 121, 484};
	cin>>T;
	for (i=0; i<T; i++)
	{
		cin>>A>>B;
		cnt = 0;
		for (j=A; j<=B; j++) 
			for (k=0; k<5; k++) if (j==palinSq[k]) cnt++;
		cout<<"Case #"<<i+1<<": "<<cnt<<"\n"; 
	}
	return 0;
}
