#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>

using namespace std;

typedef long long in;

int main(){
  ios::sync_with_stdio(false);
  in a=1000000000000001LL;
  in b=10;
  vector<in> numbs;
  numbs.push_back(a);
  while(b!=1000000000000000LL){
    in q=numbs.size();
    for(int i=0;i<q;i++){
      numbs.push_back(numbs[i]+b);
    }
    b*=10;
  }
  vector<string> s;
  for(int i=0;i<in(numbs.size());i++)
    s.push_back(to_string(numbs[i]));
  in num=0;
  in m;
  vector<in> res;
  vector<string> ress;
  int ressize=0;
  for(int i=0;i<in(s.size());i++){
    vector<in> divs;
    for(int j=2;j<=10;j++){
      num=0;
      m=1;
      for(int r=in(s[i].size())-1;r>=0;r--){
	//if(i==0&&j==10)
	  //cout << m << endl;
	if(s[i][r]=='1')
	  num+=m;
	m*=j;
      }
      for(in r=2;r*r<=num;r++){
	if(num%r==0){
	  divs.push_back(r);
	  break;
	}
      }
    }
    if(divs.size()==9){
      ress.push_back(s[i]);
      ressize++;
      for(int j=0;j<in(divs.size());j++)
	res.push_back(divs[j]);
    }
    if(ressize==50)
      break;
  }
  cout << "Case #1:" << endl;
  in pos=0;
  //cout << ress.size() << endl;
  for(int i=0;i<in(ress.size());i++){
    cout << ress[i] << " ";
    /*for(int j=2;j<=10;j++){
      num=0;
      m=1;
      for(int r=ress[i].size()-1;r>=0;r--){
	if(ress[i][r]=='1')
	  num+=m;
	m*=j;
      }
      cout << num%res[pos] << endl;
      pos++;
    }*/
    for(int j=0;j<9;j++)
      cout << res[pos+j] << " ";
    cout << endl;
    pos+=9;
  }
  return 0;
}
  