/*

*/

//#pragma comment(linker, "/STACK:16777216")
#include <fstream>
#include <iostream>
#include <string>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <memory.h>
 
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
 
#define  INF 100000000
#define eps 1e-6
#define M_PI 3.141592653589793
//#define mx 1000000000000ll
#define bs 1000002013
//#define free asdfasdfsdadsg
//#define szz 400
//#define pb push_back
#define MAXN 10000
#define free afdshjioey
//#define SIZE 60

using namespace std;
int n; 
long ts;
vector<int> g[MAXN];
bool used[MAXN];
vector<int> ans;
 long tests;
 long a[MAXN],b[MAXN];
 long answ[MAXN];
 long bu[MAXN],bd[MAXN];
 long inp[MAXN];
 
 /*
void dfs (int v) {
	used[v] = true;
	for (size_t i=0; i<g[v].size(); ++i) {
		int to = g[v][i];
		if (!used[to])
			dfs (to);
	}
	ans.push_back (v);
}
 */
void topological_sort() {
	for (int i=1; i<=n; ++i)
		used[i] = false;
		ans.clear();
  for (int i=1;i<=n;i++)
		for (int j=0;j<g[i].size();j++)
            inp[g[i][j]]++;
            
for (int iters=1;iters<=n;iters++)
{
    long q=n;
    while (inp[q]>0||used[q]==1)--q;
    ans.push_back(q);
    for (int i=0;i<g[q].size();i++)
    inp[g[q][i]]--;
    used[q]=1;
  /*  cout<<"#"<<q<<endl;
    for (int i=1;i<=n;i++)
    cout<<inp[i]<<" ";
    cout<<endl;
*/
}
	//reverse (ans.begin(), ans.end());
}

int main(){
//freopen("funny.in","r",stdin);
//freopen("funny.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);

cin>>tests;
for (;tests;--tests)
{
 cin>>n;++ts;
 
 for (int i=1;i<=n;i++)
 cin>>a[i];
 
 for (int i=1;i<=n;i++)
 cin>>b[i];
 
 /*if (ts==17)
 {for (int i=1;i<=n;i++)
 cout<<a[i]<<" "<<b[i]<<endl;
 }*/
 
 for (int i=1;i<=n;i++)
 g[i].clear();
 
 for (int i=1;i<=n;i++)
 for (int j=i+1;j<=n;j++)
 if (a[i]>=a[j])g[i].push_back(j);
 
 for (int i=1;i<=n;i++)
 for (int j=i-1;j>=1;j--)
 if (a[j]==a[i]-1){g[i].push_back(j);break;}
 
 for (int i=1;i<=n;i++)
 for (int j=i+1;j<=n;j++)
 if (b[j]==b[i]-1){
 g[i].push_back(j);break;}
 
 for (int i=1;i<=n;i++)
 for (int j=1;j<i;j++)
 if (b[j]<=b[i])g[i].push_back(j);
 /*
 if (ts==17)
 for (int i=1;i<=n;i++)
 {
     cout<<i<<" #  ";
     for (int j=0;j<g[i].size();j++)
         cout<<g[i][j]<<" ";
         cout<<endl;    
 }*/
 
 topological_sort();
/*if (ts==17){ cout<<"!"<<endl;
 
 for (int i=0;i<ans.size();i++)
 cout<<ans[i]<<" ";
 cout<<endl;
}*/

 cout<<"Case #"<<ts<<":";
 
 for (int i=0;i<ans.size();i++)
 answ[ans[i]]=n-i;
 for (int i=1;i<=n;i++){
 cout<<" "<<answ[i];
 }cout<<endl;
 for (int i=1;i<=n;i++)
 bu[i]=bd[i]=1;
 
 for (int i=1;i<=n;i++)
 for (int j=1;j<i;j++)
 {
 if (answ[i]>answ[j])bu[i]=max(bu[i],bu[j]+1);   
 }
 for (int i=n;i;--i)
 for (int j=i+1;j<=n;j++)
 if (answ[i]>answ[j])bd[i]=max(bd[i],bd[j]+1);
 
 long fl=0;
 for (int i=1;i<=n;i++)
 if (bu[i]!=a[i]||bd[i]!=b[i])
 fl=1;
 if (fl)
 {for (int i=1;i<=n;i++)
 cout<<bu[i]<<" ";
 
 cout<<endl;
 for (int i=1;i<=n;i++)
 cout<<bd[i]<<" ";
 cout<<endl;
 for(int i=1;i<=n;i++)
 cout<<a[i]<<" ";
 cout<<endl;
 for (int i=1;i<=n;i++)
 cout<<b[i]<<" ";
 cout<<endl;}
}

cin.get();cin.get();
return 0;}
