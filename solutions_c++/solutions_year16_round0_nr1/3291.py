#include<iostream>
#include<fstream>
#include<vector>

//#define small 
#define large

typedef std::vector<bool> vb;

bool complete(vb &digit){
  for (int i = 0; i < 10; i++) {
    if(!digit[i]) return false;
  }
  return true;
}

int main()
{
#if defined(small)
	freopen("A-small-attempt0.in", "r", stdin);

	std::ofstream out("out.out");
#elif defined(large)
	freopen("A-large.in", "r", stdin);
#endif
	freopen("out.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
	  int N;
	  scanf("%d", &N);
	  if(N == 0){
	    printf("Case #%d: INSOMNIA\n", t);
	    continue;
	  }
	  vb digit(10);
	  int numb = 0;

	  while (!complete(digit)) {
	    numb += N;
	    //    std::cerr << "N: " << N << " numb: " << numb << "\n";
	    int tempNumb = numb;
	    while(tempNumb > 0){
	      digit[tempNumb % 10] = true;
	      tempNumb /= 10;
	    }	    
	  }
	  
	  printf("Case #%d: %d\n", t, numb);	  
	}	
	return 0;
}
