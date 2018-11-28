#include <iostream>

using namespace std;
long long gu[10]; 
int main(){
  freopen("dumbb.txt", "r", stdin); 
  freopen("dumber2.txt", "w", stdout);
  ios_base::sync_with_stdio(0); 
  int t; cin >> t; 
  for (int g=1; g<=t; g++){
    long long r; cin >> r; 
    memset(gu,0,sizeof(gu)); long long cnt = 0;  
    long long ans = -1;for ( long long y=1; y<=100000; y++){
	long long nu = 1LL * r * y; 
        while (nu){if (!gu[nu%10])cnt++; gu[nu%10]=1; nu/=10;}
        if (cnt == 10){ans = 1LL * r * y; break;}
    }    
    cout << "Case #" << g << ": "; 
    if (ans == -1) cout << "INSOMNIA" << endl; 
    else cout << ans << endl;
  } 
}
