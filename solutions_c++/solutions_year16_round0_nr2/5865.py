#include <bits/stdc++.h>

using namespace std;

vector<string> split(string str, char delimiter)
{
	vector<string> internal;
	stringstream ss(str);
	string tok;

	while(getline(ss, tok, delimiter))
	{
		internal.push_back(tok);
	}

	return internal;
}

char s[1234];


int main() 
{
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  int tmp;
  scanf("%d", &tt);
  gets(s);
  for (int qq = 1; qq <= tt; qq++) {
		printf("Case #%d: ", qq);

    
    stringstream ss;
    
    gets(s);
   
    for(int j = 0; s[j] ; j++) ss << s[j]; 
    
    vector<string> w = split(ss.str(), ' ');    
    for(int i = w.size()-1; i >= 0; --i)
    {
      const char* ts = w[i].c_str();
      char A = ts[0];
      char B;
      int cnt = 0;
      
      for( int i = 1 ; i < strlen(ts); i++){
        B = ts[i];
        //cout << B ;
        if (A != B){
        	if( A == '-'){
        		cnt +=1;
        		A = B;
        	} else {
        		cnt +=1;
        		A = B;
    			
        	}
        }
        //cout << cnt;        
      }
      if (A == '-'){
      	cnt += 1;
      }
      printf("%d\n", cnt);
    
    }
  }
  return 0;
}
