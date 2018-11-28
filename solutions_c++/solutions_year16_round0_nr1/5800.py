#include <bits/stdc++.h>

using namespace std;



int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int N;   
    
    int myints[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    list<int> mylist (myints, myints+10);
    
    scanf("%d", &N);
    int M;
    M = N;
    int ans = 0;
    string insom = "INSOMNIA";
    if (N==0){
    	cout << insom << endl;
    } else {
    while(mylist.size() != 0)
    {
    	if( M < 10){
    		mylist.remove(M);
        //cout << mylist.size() << endl;
  
    	} else {
    		int D = M;
    		while(D != 0){
    		  int R;
    		  R = D - (D/10)*10;
    			mylist.remove(R);
    		  D = D/10;
    		  //cout << D << endl;
    		}
    	  
    	}	
    		//cout << mylist.size() << endl;
        M = M + N;
    		
    		//cout << N << endl;	
    	}	
  		cout << M - N << endl;
   	}   
    
  }
  return 0;
}
