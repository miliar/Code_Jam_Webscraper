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
  int t;
  cin >> t;
  for(int test=0;test<t;test++){
    string s;
    cin >> s;
    vector<int> counts(26);
    int c=0;
    for(int i=0;i<s.size();i++){
      counts[int(s[i])-65]++;
      c++;
    }
    vector<int> numbs(10);
    while(c!=0){
      if(counts[int('Z')-65]!=0){
	numbs[0]+=counts[int('Z')-65];
	counts[int('E')-65]-=counts[int('Z')-65];
	counts[int('R')-65]-=counts[int('Z')-65];
	counts[int('O')-65]-=counts[int('Z')-65];
	counts[int('Z')-65]-=counts[int('Z')-65];
	c-=numbs[0]*4;
      }
      if(counts[int('W')-65]!=0){
	numbs[2]+=counts[int('W')-65];
	counts[int('T')-65]-=counts[int('W')-65];
	counts[int('O')-65]-=counts[int('W')-65];
	counts[int('W')-65]-=counts[int('W')-65];
	c-=numbs[2]*3;
      }
      if(counts[int('U')-65]!=0){
	numbs[4]+=counts[int('U')-65];
	counts[int('F')-65]-=counts[int('U')-65];
	counts[int('O')-65]-=counts[int('U')-65];
	counts[int('R')-65]-=counts[int('U')-65];
	counts[int('U')-65]-=counts[int('U')-65];
	c-=numbs[4]*4;
      }
      if(counts[int('X')-65]!=0){
	numbs[6]+=counts[int('X')-65];
	counts[int('S')-65]-=counts[int('X')-65];
	counts[int('I')-65]-=counts[int('X')-65];
	counts[int('X')-65]-=counts[int('X')-65];
	c-=numbs[6]*3;
      }
      if(counts[int('O')-65]!=0&&counts[int('N')-65]!=0&&counts[int('E')-65]!=0){
	counts[int('O')-65]-=1;
	counts[int('N')-65]-=1;
	counts[int('E')-65]-=1;
	numbs[1]++;
	c-=3;
      }
      if(counts[int('T')-65]!=0&&counts[int('H')-65]!=0&&counts[int('R')-65]!=0&&counts[int('E')-65]>1){
	counts[int('T')-65]-=1;
	counts[int('H')-65]-=1;
	counts[int('R')-65]-=1;
	counts[int('E')-65]-=2;
	numbs[3]++;
	c-=5;
      }
      if(counts[int('F')-65]!=0&&counts[int('I')-65]!=0&&counts[int('V')-65]!=0&&counts[int('E')-65]!=0){
	counts[int('F')-65]--;
	counts[int('I')-65]--;
	counts[int('V')-65]--;
	counts[int('E')-65]--;
	numbs[5]++;
	c-=4;
      }
      if(counts[int('S')-65]!=0&&counts[int('E')-65]>1&&counts[int('V')-65]!=0&&counts[int('E')-65]!=0&&counts[int('N')-65]!=0){
	counts[int('S')-65]--;
	counts[int('E')-65]--;
	counts[int('V')-65]--;
	counts[int('E')-65]--;
	counts[int('N')-65]--;
	numbs[7]++;
	c-=5;
      }
      if(counts[int('E')-65]!=0&&counts[int('I')-65]!=0&&counts[int('G')-65]!=0&&counts[int('H')-65]!=0&&counts[int('T')-65]!=0){
	counts[int('E')-65]--;
	counts[int('I')-65]--;
	counts[int('G')-65]--;
	counts[int('H')-65]--;
	counts[int('T')-65]--;
	numbs[8]++;
	c-=5;
      }
      if(counts[int('I')-65]!=0&&counts[int('N')-65]>1&&counts[int('E')-65]!=0){
	counts[int('E')-65]-=1;
	counts[int('I')-65]-=1;
	counts[int('N')-65]-=2;
	numbs[9]++;
	c-=4;
      }
    }
    cout << "Case #" << test+1 << ": ";
    for(int i=0;i<10;i++){
      while(numbs[i]!=0){
	cout << i;
	numbs[i]--;
      }
    }
    cout << endl;
  }
  return 0;
}
      
	