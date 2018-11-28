#include <iostream>

using namespace std;


int checkarr(int arr[])
{
  for(int i=0;i<10;i++)
    {
      if(arr[i]==0)
	return 0;
    }   
  return 1;
}
void fillarray(int num,int arr[])
{
  long long unsigned int cur;
  while(num !=0)
    {
      cur = num%10;
      if (arr[cur]==0)
	arr[cur]=1;
      num = num/10;
    }
  return ;
}

void solve(long long unsigned int num)
{
  if(num == 0)
    {
    cout << "INSOMNIA" << "\n"; 
    return ;
    }
  int arr[10]={0};
  long long unsigned int sum=num;
  while(checkarr(arr)==0)
    {
      fillarray(sum, arr);
      sum = sum+num;
    } 
  cout << sum-num << "\n";
}

int main()
{
    freopen("A-large.in", "r", stdin);
   freopen ("myfile.txt","w",stdout);
  int t;
  cin >> t;
  long long unsigned int num;
  for(int i=0;i<t;i++)
    {
      scanf("%llu",&num);
      printf("Case #%d: ", i+1);
      solve(num);
    }
  return 0;
}
