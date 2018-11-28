#include<iostream>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;


int main(){

int t;
cin>>t;

for(int i=1;i<=t;i++)
{
  long long int n,N;
  cin>>n;
N=n;
if(n==0)
cout<<"case #"<<i<<": "<<"INSOMNIA"<<"\n";
else
{
int s = 0;
map<int,int> m;
long long int SIZE = 0;
vector<long long int> v;
//cout<<n<<"\n";
while(s==0)
{
  v.push_back(n);
  SIZE++;
  //cout<<<<"n="<<n<<"\t"<<"SIZE="<<SIZE<<"\n";
  long long int x = n;
  while(x>0)
{
  int rem = x%10;
  x/=10;
  m[rem] = 1;
}

if(m.size()==10)
{
 s=1;
 cout<<"case #"<<i<<": "<<v[SIZE-1]<<"\n";


}
else
n = (SIZE+1)*N;
}
}
}

return 0;
}
