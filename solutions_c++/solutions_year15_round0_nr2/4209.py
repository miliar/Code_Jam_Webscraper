#include<iostream>
#include<vector>
#include<utility>

using namespace std;


void printAns(int a[], int N)
{
    int maxAns = 0;
    for(int i=0;i<N;i++)
    {
	maxAns = max(maxAns,a[i]);
    }
  
   int ans = maxAns;
   for(int i=1;i<=maxAns;i++)
   {
	int count = 0;
	for(int j=0;j<N;j++)
       	{
	   int r = a[j]/i;
	   if(a[j]%i != 0)
	     r++;
	   count += r-1;
	}
      ans = min(count+i,ans);
   }
  cout << ans;

}
int main()
{
    int T,N;
    cin >> T; 
    int j=0;
    while(T--)
    {
       cin >> N;
       cout << "Case #" << j+1 <<": ";
       int a[N];
       for(int i=0;i<N;i++)
	cin >> a[i];
       printAns(a,N);
       cout << endl;
       j++;
    }
  return 0;
}
