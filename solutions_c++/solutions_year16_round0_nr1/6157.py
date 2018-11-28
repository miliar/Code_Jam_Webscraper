/*input
100
0
1
2
11
1692
9
808968
629159
545641
207673
451500
1250
20
1000000
507433
824677
999998
631543
981888
223725
999992
92636
388289
207531
999996
576992
6
999995
12500
124033
417075
442468
999994
1123
803776
374446
137934
337067
922644
802825
335182
862676
335008
999999
34
56421
200
775436
7
124
166
253815
360497
767863
154667
40
354265
26387
567650
546716
999991
333287
267514
84802
614934
807345
999993
232629
5
125000
10
999997
269415
405297
807333
672364
893543
769045
778255
859683
8
450037
350671
473257
3
125
742304
529535
25
194188
527474
543058
585717
388081
7063
4
221589
392302
989306
393399
*/

#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long int ull;
typedef long long int lli;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii; 

#define rep(i, n) for (int i = 0; i < n; i++)
#define F first
#define S second
#define INF    0x3f3f3f3f
#define NEGINF 0xC0C0C0C0
#define NULO -1

int main(){
	int n, t;

	scanf("%d", &t);

	rep(j, t){
    	int vet[10], aux, x = 2;
    	bool OK;

    	scanf("%d", &n);
    	memset(vet, 0, sizeof vet);

        if (!n)
        	printf("Case #%d: INSOMNIA\n", j + 1);
        else{
            aux = n;
            while(1){

              while(aux != 0){
              	  vet[aux % 10] = 1;
                  aux /= 10;
              }
 
              OK = true;
              for(int i = 0; i < 10; i++)
              	  if (!vet[i]){
              	      OK = false;
              	      break;
              	  }

              if (OK)
                  break;
              else{
                  aux = n * x;
                  x++;
              }    	       

            }

    		printf("Case #%d: %d\n", j + 1, n * (x - 1));
    	}
	}

	return 0;
}