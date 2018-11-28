#include <iostream>


using namespace std;

int getSum(int P[], int N)
{
	int sum=0;
	for(int i=0;i<N;i++)
		sum+=P[i];
	return sum;
}

int main()
{
	int T;cin>>T;
	int t = 1;
	while(t <= T)
	{
		int N;
		cin>>N;
		int P[N];
		for(int i=0;i<N;i++) 
		{
			cin>>P[i];
		}

		int sum = getSum(P,N);

		string res = "";
		
		
		while(sum != 0)
		{


			int leaveFlags[N];
			for(int i = 0; i < N; i++)
				leaveFlags[i] = 0;
		
			int max = P[0];
			int maxIndex = 0;
			for(int i=0;i<N;i++)
			{
				if(P[i] > max)
				{
					max = P[i];
					maxIndex = i;
				}
			}

			if(sum-2 == 1)
			{
				//Only one should leave
				P[maxIndex] -= 1;
				sum = getSum(P,N);
				res = res + (char(maxIndex+65)) + " ";
				continue;
			}	

			if(max > sum/2)
			{
				//Two of max should leave
				P[maxIndex] -= 2;
				sum = getSum(P,N);
				res = res + (char(maxIndex+65)) + " ";
			}
			else
			{	
				P[maxIndex] -= 1;
				res = res + (char(maxIndex+65));
				//Otherwise find the second highest
				leaveFlags[maxIndex] = 1;

				max = P[0];
				maxIndex = 0;
				for(int i=0;i<N;i++)
				{
					if(P[i] > max && leaveFlags[i] != 1)
					{
						max = P[i];
						maxIndex = i;
					}
				}
				P[maxIndex] -= 1;
				res = res + (char(maxIndex+65)) + " ";
				sum = getSum(P,N);
			}

		}	

		cout<<"Case #"<<t<<": "<<res<<"\n";
		t++;
	}
}