// Author : SAGORIKA DAS
// Codejam Round1A
//  A. The Last Word
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<list>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<string>
#define ull unsigned long long
#define ll long long
#define F first
#define S second
#define MOD 1000000007
#define inf 1000000006
#define pb push_back
#define MAX 100002
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define mp make_pair
#define CLEAR(a) memset(a,0,sizeof a)
#define pii pair< int , int >
#define piii pair< int , pii >
#define piiii pair< int, piii >
using namespace std;

int main(){
    
   freopen("input.txt", "r", stdin); 
   freopen("output.txt", "w", stdout);
   int T, cas = 1;
	scanf("%d",&T);
	while(T--){
      string s;
      deque<char> q;
      cin >> s;
      q.push_front(s[0]);
      FOR(i,1,s.size()){
              if(s[i] >= q.front())
              q.push_front(s[i]);
              else q.push_back(s[i]);        
      }         
    printf("Case #%d: ",cas++); 
    while(!q.empty()){
    cout<<q.front();q.pop_front();                  
    }          
    cout<<endl;
    }
	// system("pause");
return 0;	
}
