
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
#include <string.h>
#include<vector>
#include<map>
#include<set>
using namespace std ;
int main()
{
freopen("A-small-attempt1.in","r",stdin);
freopen("a_small_output.out","w",stdout);

int T ;
cin>>T ;
int t =0 ;
while(T--)
{//cout<<"T";
int r1,r2 ;
cin>>r1 ;
vector<vector<int> > arr ;
for(int i =0 ; i < 4  ; i++ )
{
    arr.push_back(vector<int> ());
    for(int j =0 ; j < 4 ; j++){int c;cin>>c;arr[i].push_back(c);}
}
vector<int> vr1 = arr[r1-1];
cin>>r2 ;
for(int i =0 ; i < 4  ; i++ )
{
    for(int j =0 ; j < 4 ; j++){cin>>arr[i][j];}
}
vector<int> vr2 = arr[r2-1];
set<int> st ;
for(int i =0 ; i < vr1.size() ; i++)if (find(vr2.begin(),vr2.end(),vr1[i])!=vr2.end()  )st.insert(vr1[i]);
cout<<"Case #"<<t+1<<": " ;
if (st.size() == 0 )cout<<"Volunteer cheated!"<<endl ;
else if (st.size() == 1)cout<<(*st.begin())<<endl ;
else cout<<"Bad magician!"<<endl ;
t++;
}
return 0 ;
}
