#include<iostream>
#include<cstdio>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<cstdlib>
#include<utility>
#include<set>
#include<fstream>
#include<map>
#include<cstring>
#include<cmath>
#include <string>
#include <vector>
#define inf 2e9
#define mp(a,b) make_pair(a,b)
#define all(a) a.begin(),a.end()
#define pb(a) push_back(a)
#define show_vector(a) for(int i=0;i<a.size();i++) cout << a[i]<<" ";
#define show_array(a,n) for(int i=0;i<=n;i++) cout << a[i]<<" ";
#define take_array(a,n) for(int i=1;i<=n;i++) cin >> a[i];
typedef long long ll; 

using namespace std;

int main()
{
  ifstream fin("input.txt"); ofstream fout("output.txt");  
  
  int A,n,t,x,c=0;
  vector<int> v;
  fin >> t;
  while(t--)
  {
    v.clear();
    c++;
    fin >> A >> n;
    for(int i=1;i<=n;i++)
    {
      fin >> x;
      v.pb(x);
    }
    sort(all(v));
   long long int ans=0,sum=A;
    if(sum==1&&v[0]>=sum) {fout << "Case #"<<c<<": "<<n<<endl; continue;}
    for(int i=0;i<n;i++)
    {
      if(v[i]<sum) sum+=v[i];
      else
      {
	int count =0;
	while(sum<=v[i])
	{
	  sum +=sum-1;
	  count++;
	  cout << sum <<endl;
	}
	sum+=v[i];
	 if(count <= n-i)ans+=count;
	 else { ans+= n-i; break;};
      }
    }
    fout << "Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
 
