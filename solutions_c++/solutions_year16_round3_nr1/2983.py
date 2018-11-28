#include <bits/stdc++.h>
#define P_MAX 1000
using namespace std;
char alpha = 'A';

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int np;
    scanf("%d", &np);
    vector<int> P(P_MAX);
    
    for (int i = 0; i < np; i++) {
    	cin >> P[i]; 
    }      
    int pos;
    //auto biggest;
    vector<string> sP(P_MAX);
    char m;
    char n;
    int cnt = 0;
    while( P[np-1] > 0) {                
    	auto biggest = max_element(begin(P), end(P)); 
    	pos = distance(begin(P), biggest);
    	if(P[pos] == 0){
    	  sP[cnt] = n;
        cnt++;
    	  continue;         
    	}
    	P[pos]--;
    	m = alpha+pos;
    	
    	//printf("%c", alpha+pos);
    	biggest = max_element(begin(P), end(P)); 
    	pos = distance(begin(P), biggest);
    	if(P[pos] == 0){
    	  sP[cnt] = m;
        cnt++;
    	  continue;         
    	}
    	P[pos]--;

    	n = alpha+pos;
    	sP[cnt] = m;
    	sP[cnt] +=n;
    	cnt++;
    	//printf("%c ", alpha+pos);	
    }              
    
    if( sP[cnt-1] == "C"){
				sP[cnt-1] = sP[cnt-2];
				sP[cnt-2] = "C";
		}
    for(auto i: sP){   
      cout <<  i << " " ;
    }
    cout << endl;
  }
  return 0;
}
