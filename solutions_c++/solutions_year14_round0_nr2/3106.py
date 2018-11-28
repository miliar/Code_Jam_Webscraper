


#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>

#include <math.h>
#include <string.h>
#include <utility>
#include <climits>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>


using namespace std;

int main(){

  int T;
  scanf("%d",&T);
for(int _T = 1; _T <= T; _T++){

double C, M, X, minimo = 0.0;
    cin >> C >> M >> X;

int tam =900000;  
double sol;

double solsum, rr1, rr2;


int i = 1, tt=0; 
double solind =( C / (2));
sol = X/(2 + 0 * M);

while(1){  
	

        rr1 = X/(2 + i * M) + solind;
        
	if(sol < rr1){     		
	break;
     }

solind += ( C / (2 + i * M));   
sol = rr1;
i++;
}

 cout <<"Case #"<<_T<<": " << setiosflags(ios::fixed) << setprecision(7)<< sol << endl;
}

return 0;
}
