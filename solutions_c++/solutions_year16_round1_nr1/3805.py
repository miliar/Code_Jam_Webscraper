#include <bits/stdc++.h>

using namespace std;
char s[1000];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    
    scanf("%s", s);

    char ans[1000];
    deque<char> m;
    int cnt = 0; 
    
    for (int i = 0; i < strlen(s); i++){
    	
    	if (s[cnt] <= s[i]){
   		 m.push_front(s[i]); 	
    	 cnt = i;
    	} else{ 
    	 m.push_back(s[i]);
    	}
    	 
    }

    for (int i = 0; i < strlen(s); i++){
     //ans[i] = m.pop_front().to_c;
     ans[i]= m.at(i);
     printf("%c", ans[i]);
    }
                        
    printf("\n");
  }
  return 0;
}
