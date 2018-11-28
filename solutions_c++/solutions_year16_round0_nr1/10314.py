#include <iostream>
using namespace std;

bool populatedigits(int arr[], int N){
while(N){
 arr[N%10]=1;
 N = N/10;
}
int ans=1;
for(int i=0;i<10;i++)
ans = ans*arr[i];

if(ans==1)return true;
else return false;
}


int findLastNumber(int N){
if(N==0)return 0;
int arr[10];

for(int k=1;k<1000000;k++)
{
   bool a = populatedigits(arr,k*N);
   if(a)return k*N;
}
return 0;
}


int main() {
int T=0;int N;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
	   scanf("%d",&N);
	   int ans = findLastNumber(N);
	   if(ans==0)cout<<"Case #"<<i+1<<": INSOMNIA\n";
	   else cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
