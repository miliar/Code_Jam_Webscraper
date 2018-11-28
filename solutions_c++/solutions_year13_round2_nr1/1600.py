#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;


int main(int argc, char **argv)
{
	int T,test=1;
	
	ofstream OUT("ANSWER.out");
	ifstream IN("A-large.in");
	
	IN >> T;
	
	while(T--)
	{
		
		long long A;
		int n,answer = 10000000,ans = 0;
		
		IN >> A >> n;
		
		vector<long long>V(n);
		
		for(int i = 0;i < n;i++)
			IN >> V[i];
			
		sort(V.begin(),V.end());
		
		for(int i = 0;i < n;i++)
		{
			if(V[i] < A)
				A += V[i];
			else {
			
				answer = min(answer , ans + n-i);
				
				//printf("(%lld , %d - %d)\n",A,ans + n-i,answer);
				
				
				if(A == 1 )
					ans = 100000000;
				else {
					while(V[i] >= A)
					A += (A-1) , ans++;
					//printf("[%lld %d]\n",A,ans);
				}

				A += V[i];
			}
		}
		
		answer = min(answer , ans);
			
		//	printf("(%d - %d)\n",ans,answer);
			
		cout << "Case #" << test << ": " << answer << endl;
		OUT << "Case #" << test++ << ": " << answer << endl;
	}
	
	// OUT << endl;
	
	return 0;
}

