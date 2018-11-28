#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <climits>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <cmath>
#include <fstream>
#define ll long long int
#define mod 10000007
using namespace std;

ll fastexpo(ll base,ll expo)
{
    if(expo==1)
        return base;
    else if(expo==0)
        return 1;
    else
    {
        if(expo%2==0)
        {
            ll base1=fastexpo(base,expo/2);
            ll ret=base1*base1;
            return ret%mod;
        }
        else
        {
            ll base1=fastexpo(base,(expo-1)/2);
            ll ans=base1*base;
            ans=ans%mod;
            ans=ans*base1;
            return ans%mod;
        }
    }
}

int main()
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,X,R,C,k=1;
	char shubham;
	scanf("%d",&t);
	while(t--)
        {
	    scanf("%d%d%d",&X,&R,&C);
	    switch(X)
	    {
	        case 1:
	                shubham='g';
	                break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    shubham='r';
	                else
	                    shubham='g';
	                    break;
	        case 3:
	                if(R==1||C==1)
	                    shubham='r';
	                else if(R==3||C==3)
	                    shubham='g';
	                else
	                    shubham='r';
	                    break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    shubham='g';
	                else
	                    shubham='r';
	    }
	    if(shubham=='g')
	        printf("Case #%d: GABRIEL\n",k);
	    else
	        printf("Case #%d: RICHARD\n",k);
    k++;
	}
	return 0;
}

