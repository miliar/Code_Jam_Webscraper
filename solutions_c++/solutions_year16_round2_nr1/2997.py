/*input
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER
*/
#include "bits/stdc++.h"
using namespace std;

#define ll      long long
#define vll     vector< long long >
#define vvll    vector< vll >
#define vd      vector< double > 
#define forP(i,x,a) for(ll i=x;i<=a;++i)
#define forM(i,x,a) for(ll i=x;i>=a;--i)
#define all(a) a.begin(), a.end()
#define put(x) printf("%I64d",x);
#define get(x) scanf("%I64d",&x);
#define ENDL printf("\n");
const ll mod = 1e9+7;

#define X first
#define Y second

ll abso( ll a){
  return (a<0)?-a:a;
}
ll PrimeDiv(ll n){
  if(n==2||n==3)return 0;
  if(!(n%2))return 2;
  for(ll j=3;j*j<=n;j+=2){
      if(!(n%j)) return j;
  }
  return 0;
}

ll calcNum(ll a,ll base){
  ll ans=0,p=1;
  for(int i=0;i<16;i++){
    ans += (a&1)*p;
    //cout<<p<<':'<<ans<<' ';
    p*=base;
    a=a>>1;
  }
  return ans;
}
string i2b(ll a){
  string rv,rvr;
  for(int i=0;i<16;i++){
    rvr += '0'+(a&1);
    //cout<<p<<':'<<ans<<' ';
    a=a>>1;
  }
  for(int i=rvr.length()-1;i>=0;i--){
    rv+=rvr[i];
  }
  return rv;
}
int main(int argc, char const *argv[])
{
 ios::sync_with_stdio(0);
 cin.tie(0);
  int t,n,cases;
  
 cin>>t;
 string s;
 for(cases=1;cases<=t;cases++){
  int arr[26]={0};
  int barr[10]={0};
  cin>>s;
  for(int i=0;i<s.length();i++){
    arr[s[i]-'A']++;
  }
  printf("Case #%d: ",cases);
  //ZERO
  while(arr['Z'-'A'] && arr['E' - 'A'] && arr['R' - 'A'] && arr['O'-'A']){
    arr['Z'-'A']--; arr['E' - 'A']--; arr['R' - 'A']--; arr['O'-'A']--;
    barr[0]++;
  }
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //TWO
  while(arr['T'-'A'] && arr['W'-'A'] && arr['O'-'A']){
    arr['T'-'A']--; arr['W'-'A']--; arr['O'-'A']--;
    barr[2]++;
  }
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //FOur
  while(arr['F'-'A'] && arr['O'-'A'] && arr['U'-'A'] && arr['R'-'A']){
    arr['F'-'A']--; arr['O'-'A']--; arr['U'-'A']--;arr['R'-'A']--;
    barr[4]++;
  }
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //FIVE
  while(arr['F'-'A'] && arr['I'-'A'] && arr['V'-'A'] && arr['E'-'A']){
    arr['F'-'A']--; arr['I'-'A']--; arr['V'-'A']--;arr['E'-'A']--;
    barr[5]++;
  }
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //SIX

  while(arr['S'-'A'] && arr['I'-'A'] && arr['X'-'A'] ){
    arr['S'-'A']--; arr['I'-'A']--; arr['X'-'A']--;
    barr[6]++;
  }
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //SEVEN
  while(arr['S'-'A'] && arr['E'-'A']>=2 && arr['V'-'A'] && arr['N'-'A'] ){
    arr['S'-'A']--; arr['E'-'A']--; arr['V'-'A']--; arr['E'-'A']--; arr['N'-'A']--;
    barr[7]++;
  }
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //EIGHT
  while(arr['E'-'A'] && arr['I'-'A'] && arr['G'-'A'] && arr['H'-'A'] && arr['T'-'A'] ){
    arr['E'-'A']--; arr['I'-'A']--; arr['G'-'A']--; arr['H'-'A']--; arr['T'-'A']--;
    barr[8]++;
  }  
  //for(int i=0;i<s.length();i++){    arr[s[i]-'A']++;  }
  //NINE
  while(arr['N'-'A']>=2 && arr['I'-'A'] && arr['N'-'A'] && arr['E'-'A']){
    arr['N'-'A']--; arr['I'-'A']--; arr['N'-'A']--; arr['E'-'A']--;
    barr[9]++;
  }

  //ONE
  while(arr['O'-'A'] && arr['N'-'A'] && arr['E'-'A']){
    arr['O'-'A']--; arr['N'-'A']--; arr['E'-'A']--;
    barr[1]++;
  }

  //THREE
  while(arr['T'-'A'] && arr['H'-'A'] && arr['R'-'A'] && arr['E'-'A']>=2){
    arr['T'-'A']--; arr['H'-'A']--; arr['R'-'A']--;arr['E'-'A']--; arr['E'-'A']--;
    barr[3]++;
  }


  for(int i=0;i<10;i++){   
    while(barr[i]--){
      putchar('0'+i);
    }
  }
  

  putchar('\n');

 }
 
 
 



  return 0;
}