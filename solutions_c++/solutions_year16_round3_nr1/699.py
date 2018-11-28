//sort seja trazida
#include <algorithm> 
#include <assert.h>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;
const int MAXN = 1e3;
const int INF  = 1e9;

#define deb(args...) fprintf(stderr,args)
typedef pair<int,int> pii;


int qtd[MAXN];
set <pii> st;


int main(){
  int test;
  scanf("%d",&test);
  for(int t=0;t<test;t++){
    st.clear();
    int n;
    scanf("%d",&n);
    int tot=0;
    for(int i=0;i<n;i++){
      scanf("%d",&qtd[i]);
      tot+=qtd[i];
      st.insert(pii(qtd[i],i));
    }
    printf("Case #%d: ",t+1);
    int ok=0;
    while(tot>0){
      if(st.size()==2){
 	set<pii>::iterator it = st.end();
	it--;
	if(ok)printf(" ");
	int fi=it->second+'A';
	it--;
	int se=it->second+'A';
	int siz=it->first;
	for(int i=0;i<siz;i++){
	  printf("%c%c ",fi,se);
	}
	ok=1;
	tot-=2*siz;
      }
      else{
	set<pii>::iterator it = st.end();
	it--;
	pii aux=*it;
	if(ok)printf(" ");
	printf("%c",it->second+'A');
	st.erase(it);
	if(aux.first-1!=0)st.insert(pii(aux.first-1,aux.second));
	tot--;
	ok=1;
      }
      
    }
    printf("\n");
  }

  return 0;
}
