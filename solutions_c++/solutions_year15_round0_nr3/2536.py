#include <bits/stdc++.h>

using namespace std;

#define mp(a,b) make_pair((a),(b))

map< pair<int,int>, int > mul,mul2;

#define I 1000
#define J 1001
#define K 1002

int conv(char a){
  if( a == 'i' ) return I;
  if( a == 'j' ) return J;
  if( a == 'k' ) return K;
  return -100000000;
}

string convb(int x){
  if( x == I )
    return "I";
  if( x == -I )
    return "-I";
  if( x == J )
    return "J";
  if( x == -J )
    return "-J";
  if( x == K )
    return "K";
  if( x == -K )
    return "-K";
  if( x == 1 )
    return "1";
  if( x == -1)
    return "-1";
  return "UNKNOWN";
}

int can[10010][10010];

int main(){
  freopen("c2.in", "r", stdin);
  freopen("c2.out", "w", stdout);

  mul[mp(I,I)] = -1;
  mul[mp(I,J)] = K;
  mul[mp(I,K)] = -J;

  mul[mp(J,I)] = -K;
  mul[mp(J,J)] = -1;
  mul[mp(J,K)] = I;

  mul[mp(K,I)] = J;
  mul[mp(K,J)] = -I;
  mul[mp(K,K)] = -1;

  mul[mp(1,I)] = I;
  mul[mp(1,J)] = J;
  mul[mp(1,K)] = K;

  mul[mp(I,1)] = I;
  mul[mp(J,1)] = J;
  mul[mp(K,1)] = K;
  
  mul2 = mul;
  for(map<pair<int,int>, int>::iterator pos = mul.begin();pos != mul.end();pos++){
    mul2[ mp(pos->first.first,-pos->first.second) ] = -pos->second;
    mul2[ mp(-pos->first.first,pos->first.second) ] = -pos->second;
    mul2[ mp(-pos->first.first,-pos->first.second) ] = pos->second;
  }
  swap(mul,mul2);

  //for(map<pair<int,int>, int>::iterator pos = mul.begin();pos != mul.end();pos++){
    //cout << convb(pos->first.first) << " x " << convb(pos->first.second) << " " << convb(pos->second) << endl;
  //}

  int t;
  cin >> t;
  int tc = 1;
  string ret;
  int x;
  while(t--){
    int n;
    cin >> n;
    cin >> x;
    cin >> ret;
    string s = "";
    while(x--)
      s += ret;

    for(int len = 1;len<=(int)s.size();len++){
      int start = 1;
      for(int i=0;i<len;i++){
        start = mul[mp(start,conv(s[i]))];
      }
      can[0][len-1] = start;

      for(int i=1;i+len-1<(int)s.size();i++){
        start = mul[mp(-conv(s[i-1]),start)];
        start = mul[mp(start,conv(s[i+len-1]))];
        can[i][i+len-1] = start;
      }
    }
    bool found = false;
    for(int i=0;i<(int)s.size() && !found;i++){
      for(int j=i+1;j<(int)s.size() && !found;j++){
        int a = can[0][i];
        int b = can[i+1][j];
        int c = can[j+1][s.size()-1];
        int neg = (a < 0) + (b < 0) + ( c < 0 );
        neg %= 2;
        if( a == abs(I) && b == abs(J) && c == abs(K) && !neg ){
          found = true;
          break;
        }
      }
    }

    if(found)
      cout << "Case #" << tc++ << ": " << "YES" << endl;
    else
      cout << "Case #" << tc++ << ": " << "NO" << endl;


  }
}
