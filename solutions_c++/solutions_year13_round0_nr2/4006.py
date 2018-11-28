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
  
int main()
{
    vector<int>v;
    v.clear();
    int rn,rm,rtest;
    int n,q,num,val,i,j,max=-1;
    string op;
    int ri,rct,rj,rk,rarr[101][101],rfailed=0,rwon;
    rct=0;
    cin>>rtest;
     
    while(rtest--)
    {
        rwon=1;
        cin>>rn>>rm;
        for(ri=0;ri<rn;ri++)
        {
            for(rj=0;rj<rm;rj++)
            {
                scanf("%d",&rarr[ri][rj]);
            }
        }
        for(ri=0;ri<rn;ri++)
        {
            for(rj=0;rj<rm;rj++)
            {
                rfailed=0;
                for(rk=0;rk<rm;rk++)
                {
                    if(rarr[ri][rk]>rarr[ri][rj])
                    {
                        rfailed=1;
                        break;
                    }
                }
                if(rfailed==1)
                for(rk=0;rk<rn;rk++)
                {
                    if(rarr[rk][rj]>rarr[ri][rj])
                    {
                        rfailed=1;
                        break;
                    }
                }
                if(rk==rn)
                    rfailed=0;
                if(rfailed==1)
                {
                    rwon=0;
                    ri=rn+1;
                    break;
                }
            }
        }
        int maxr=0,maxc=0;
        max=maxr+maxc;
        rct++;
        if(rwon==1)
            cout<<"Case #"<<rct<<": YES";
        else cout<<"Case #"<<rct<<": NO";
        cout<<"\n";
    }
}
