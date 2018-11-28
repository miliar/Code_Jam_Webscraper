#include<bits/stdc++.h>
using namespace std;
int main(){
	int t, k;
    cin>>t;
    string L,L1;
    for (int i = 1; i <= t; ++i){
      cin>>L>>k;
      L1 = L;
      bool FLAG = 1;
      int n = L.size();
      int cnt = 0;
      int mini = 1e8;
      for (int j = 0; j < n; ++j){
      		if(L[j] == '-'){
      			if( k <= n-j){
      				for (int q = j; q < j+k; ++q)
      				{
      					if(L[q] == '+')L[q] = '-';
      					else L[q] = '+';
      				}
      				cnt++;
      			}
      		}
      }
      for (int j = 0; j < n; ++j){
      		if(L[j] == '-')FLAG = 0;
      }
      if(FLAG)mini = cnt;
      FLAG = 1;
      cnt = 0;
      for (int j = n-1, p = 0; j >= 0; --j,p++){
      	    L[p] = L1[j];
      }
      for (int j = 0; j < n; ++j){
      		if(L[j] == '-'){
      			if( k <= n-j){
      				for (int q = j; q < j+k; ++q)
      				{
      					if(L[q] == '+')L[q] = '-';
      					else L[q] = '+';
      				}
      				cnt++;
      			}
      		}
      }
      for (int j = 0; j < n; ++j){
      		if(L[j] == '-')FLAG = 0;
      }
      if(FLAG){
        	mini = min(mini, cnt);
        	cout<<"Case #"<<i<<": "<<mini<<endl;
      }else if(mini == 1e8){
        	cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
      }else cout<<"Case #"<<i<<": "<<mini<<endl;
    }
}