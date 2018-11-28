#include<iostream>
#include<fstream>
#include<vector>
#include<string>

//#define small 
#define large

typedef std::vector<bool> vb;

vb str2bv(std::string &str){
  vb bv(str.size());
  for (int i = 0; i < str.size(); i++) {
    if(str[i] == '+')
      bv[i] = true;
  }
  return bv;
}

int main()
{
#if defined(small)
	freopen("B-small-attempt0.in", "r", stdin);

	std::ofstream out("out.out");
#elif defined(large)
	freopen("B-large.in", "r", stdin);
#endif
	freopen("out.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
	  std::string S;
	  //scanf("%s", &S);
	  std::cin >> S;
	  vb bS = str2bv(S);
	  int turn;
	  for (turn = 0; turn < 1e9; turn++) {
	    bool prefix = bS[0];
	    int n = 1;
	    while(n < bS.size()){
	      if(prefix != bS[n])
		break;
	      n++;
	    }
	    if(n == bS.size() && prefix == true)
	      break;
	    for (int i = 0; i < n; i++) {
	      bS[i] = !prefix;
	    }
	  }

	printf("Case #%d: %d\n", t, turn);	  
	}	
	return 0;
}
