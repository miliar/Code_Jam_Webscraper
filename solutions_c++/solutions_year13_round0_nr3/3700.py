#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;

bool good(vector < int > h, int x) { 
		int prev = 0, n = h.size();
		

		for(int i=0;i<=n-1;i++) {
			//if we can make tree[i] higher than previous one
			if (h[i] + x <= prev) return false;
			//reset the value of prev for the next step
			prev = max(prev + 1, h[i] - x);
		}
		return true;
	}
 

  int minLevel(vector <int> heights) {
    int left=-1;
    int right=1000000000;
    while(right>left+1){
      int mid=(left+right)/2;
      if(good(heights,mid)) right=mid;
      else left=mid;
    }
    return right;
  }
  
bool ppp(int num);
int main()
{
    int testrr,irr,jrr,arr,brr,crr,counterrr=0,ctrr=0;
    float krr;
    cin>>testrr;
    while(testrr--)
    {
        cin>>arr>>brr;
        krr=1;
        while(krr*krr<arr)
            krr++;
        counterrr=0;
        crr=krr;
        while(crr*crr<=brr)
        {
            if(ppp(crr) && ppp(crr*crr))
            {
                counterrr++;
            }
            crr++;
        }
        ctrr++;
    cout<<"Case #"<<ctrr<<": "<<counterrr<<"\n";
    }

}
bool ppp(int num)
{
    int irr,jrr,krr;
    int n,i,val;
    int arrrr[100];
    irr=0;
    vector<int>v;
    v.clear();
    while(num>0)
    {
        arrrr[irr]=num%10;
        num/=10;
        irr++;
    }
    for(jrr=0,krr=irr-1;jrr<krr;jrr++,krr--)
    {
        if(arrrr[jrr]!=arrrr[krr])
        {
            return false;
        }
    }
    return true;
}










