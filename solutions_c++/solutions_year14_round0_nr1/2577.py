#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int x,m,ss,k,qnty,n;
set<int> cmp;
vector<int> a,b;

int main()
{
  scanf("%d",&ss);
  for(int s=1;s<=ss;++s)
    {
      printf("Case #%d: ",s);
      a.clear();
      b.clear();
      cmp.clear();
      n=-1;
      scanf("%d",&k);
      for(int i=1;i<=4;++i)
	for(int j=1;j<=4;++j)
	  {
	    scanf("%d",&x);		
	    if (i==k)
	      cmp.insert(x);
	  }		
      scanf("%d",&k);
      for(int i=1;i<=4;++i)
	for(int j=1;j<=4;++j)
	  {
	    scanf("%d",&x);
	    if (i==k)
	      b.push_back(x);
	  }
      for(int i=0;i<4;++i)
	  if (cmp.count(b[i])>0)
	    a.push_back(b[i]);
      if (a.size()==1)
	printf("%d\n",a[0]);
      else
	puts(a.size()!=0?"Bad magician!":"Volunteer cheated!");
    }
  return 0;
}

