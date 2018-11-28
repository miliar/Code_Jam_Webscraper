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
#include <cstring>

#define clr(name,val) memset(name,(val),sizeof(name));
#define EPS .000000001
#define ll long long
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo 10000000
#define mp make_pair
#define fs first
#define sc second
#define rep(var,s,n) for(var=(s);var<(n);(var)++)
#define rvp(var,s,n) for(var=(n-1);var>(s-1);(var)--)
#define read_ freopen("input.txt","r",stdin)
#define write_ freopen("output.txt","w",stdout)

///next_permutation  next_permutation (s.begin(),s.end())
///reverse(a,a+n);
///binary_search(first,last);
///vector erase v.erase(v.begin()+position);
///map map<int , int > data;
///map clear  data.clear();
///map iterator>>>> map <int,vector <int> >::const_iterator it;
///find an element in map (colour.find(nd)==colour.end());//if it return true this
///mean the element is'nt in the map.
///pass a vector to a funtion: funtion (vector <data type> &vector name);
///make_pair  point=make_pair(i,j);
///access pair value point.first;point.second;

using namespace std;

///int rr[]= {-1,-1,0,0,1,1};
///int cc[]= {-1,0,-1,1,0,1};
///int rr[]= {0,0,1,-1};/*4 side move*/
///int cc[]= {-1,1,0,0};/*4 side move*/
///int rr[]= {1,1,0,-1,-1,-1,0,1};/*8 side move*/
///int cc[]= {0,1,1,1,0,-1,-1,-1};/*8 side move*/
///int rr[]={1,1,2,2,-1,-1,-2,-2};/*night move*/
///int cc[]={2,-2,1,-1,2,-2,1,-1};/*night move*/

vector<ll> v;
int arr[30];
bool cheak_pal(ll n)
{
    int i=0;
    while(n)
    {
        arr[i++]=(n%10);
        n/=10;
    }
    for(int k=0,j=i-1;k<j;k++,j--)
        if(arr[k]!=arr[j]) return false;
    return true;
}

int bin_(int lb,int ub,ll val)
{
    int mid=(lb+ub)/2;
    while(lb<ub)
    {
        if(v[mid]==val) return mid;
        if(v[mid]>val) ub=mid-1;
        else lb=mid+1;
        mid=(lb+ub)/2;
    }
    return mid;
}

int main()
{
    read_;
    write_;
    ll val,cnt=0;
    for(ll i=1;i<10000010;i++)
    {
        val=i*i;
        if(cheak_pal(i)&&cheak_pal(val))
        {
//            cout<<++cnt<<" "<<val<<endl;
            v.psb(val);
        }
    }
    ll A,B;
    int lb=0,cas=0,ub=v.size()-1,test,loca,locb,res;
    scanf("%d",&test);
    while(test--)
    {
        scanf("%lld %lld",&A,&B);
        loca=bin_(lb,ub,A);
        if(v[loca]<A) loca++;
        locb=bin_(lb,ub,B);
        if(v[locb]>B) locb--;
        res=(locb-loca)+1;
        if(res<0) res=0;
        printf("Case #%d: %d\n",++cas,res);
    }
    return 0;
}
