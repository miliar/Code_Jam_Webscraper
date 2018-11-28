#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int main()
{
     int T, cas = 1;
     cin >> T;
     while(T--)
     {
	cout << "Case #" << cas <<": ";
	cas++;
	int N;
	cin >> N;
	vector<double> v1(N),v2(N);
	for(int i=0;i<N;i++)
		cin >> v1[i];
	for(int i=0;i<N;i++)
		cin >> v2[i];
	sort(v1.begin(),v1.end());
	sort(v2.begin(),v2.end());
	int count = 0,k=0;
	for(int i=0;i<N;i++)
	{
	   while(v1[i]>v2[k])
	   {
	     if(k == N)
		break;
	     k++;
           }
	   if(k >= N)
		break;
           count++;
	   k++;
	   if(k>=N)
		break;
	}
	int ans1 = N-count, minm = ans1,st=0,en=N-1;
	count = 0;
	for(int i=0;i<N;i++)
	{
	    if(v1[i] > v2[st])
	    {
		st++; 
		count++;
	    }
	}	
	cout << count << " " << ans1 << endl;
     }
    return 0;
}
