#include <bits/stdc++.h>
using namespace std;
string num[]={"ZERO","FOUR","TWO","SIX", "EIGHT","THREE" ,"ONE","SEVEN","FIVE","NINE"};
char N[]={0,4,2,6,8,3,1,7,5,9};
int main(){
  int q;
  cin>>q;
  for(int Q=1;Q<=q;Q++){

    string str;
    cin>>str;
    int cnt[302]={};
    for(int i=0;i<str.size();i++) cnt[str[i]]++;

    string ans;
    for(int i=0;i<=9;i++){
      while(1){
	int c=1;
	for(int j=0;j<num[i].size();j++){
	  if(!cnt[num[i][j]]) c=0;
	  cnt[num[i][j]]--;
	}
	for(int j=0;j<num[i].size()&&!c;j++) cnt[num[i][j]]++;
	if(c) ans+=(N[i]+'0');
	if(c==0)break;
      }
    }
    
    int f=0;
    for(int i='A';i<='Z';i++) if(cnt[i])f++;
    sort(ans.begin(),ans.end());

    cout <<"Case #"<<Q<<": ";
    cout << ans<<endl;    
    assert(!f);
  }
  return 0;
}
