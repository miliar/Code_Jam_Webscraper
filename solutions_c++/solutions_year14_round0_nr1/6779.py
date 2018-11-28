#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <memory.h>
#include<cstring>
using namespace std;
 
int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int cnt=1;
	while(t-->0)
	{
		int fi;
		cin >> fi;
		int a[4][4];
		for(int i=0;i<4;i++)
		{
		  for(int j=0;j<4;j++)
		{ 	
		   cin >> a[i][j];
		}
	  }
	  int se;
		cin >> se;
		int b[4][4];
		for(int i=0;i<4;i++)
		{
		  for(int j=0;j<4;j++)
		{ 	
		   cin >> b[i][j];
		}
	  }
	  int ans=0;
	  int s=0;
	  for(int i=0;i<4;i++)
		{
		  for(int j=0;j<4;j++)
		 {
		  if(a[fi-1][i]==b[se-1][j])
		     {
		     	ans++;
		     	s=a[fi-1][i];
		     	break;
		     }
		  }
		}
		if(ans==0)
		  {
		  	cout << "Case #" << cnt << ":" << " Volunteer cheated!"<<endl;
		  }
		  else if(ans==1)
		  {
		  	cout << "Case #" << cnt << ": " << s<<endl;
		  }
		  else
		  {
		  	cout << "Case #" << cnt << ":" << " Bad magician!"<<endl;
		  }
	  cnt++;
	}
}