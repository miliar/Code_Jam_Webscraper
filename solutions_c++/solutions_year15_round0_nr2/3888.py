#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>

#define rep(k,a) for(int k = 0; k < (a); k++)

using namespace std;

int ps[333];

int mozn[10][3][3] = {
											{{-1},{-1},{-1}}, 
											{{1},{-1},{-1}},
											{{2},{-1},{-1}},
											{{3},{-1},{-1}},
											{{4},{2,2},{-1}},
											{{5},{2,3},{-1}},
											{{6},{3,3},{-1}},
											{{7},{3,4},{-1}},
											{{8},{4,4},{-1}},
											{{9},{4,5},{3,3,3}},
};
int numofmozn[10] = {-1,1,1,1,2,2,2,2,2,3};
int set[333];

int main()
{/*
	mozn[1][0]={1};
	mozn[2][0]={2};
	mozn[3][0]={3};
	mozn[4][0]={4};
	mozn[5][0]={5};
	mozn[6][0]={6};
	mozn[7][0]={7};
	mozn[8][0]={8};
	mozn[9][0]={9};

	mozn[4][1]={2,2};
	mozn[5][1]={3,2};
	mozn[6][1]={3,3};
	mozn[7][1]={3,4};
	mozn[8][1]={4,4};
	mozn[9][1]={4,5};

	mozn[9][2]={3,3,3};
*/
	int T;
	scanf("%d", &T);
	rep(i, T){
		rep(j, 200)
			ps[i]=0;
		int d;
		scanf("%d", &d);
		rep(j,d){
			int in;
			scanf("%d", &in);
			ps[j]=in;
		}
		int mintime = 999999;
		rep(j, (int)pow(3,d)){
			//printf("j %d\n", j);
			int num = j;
			int zacatek = 0;
			int splits = 0;
			bool broken = false;
			for(int exp = 0; exp < d; exp++){
				int cislice = num % 3;
				if(mozn[ps[exp]][cislice][0]==-1){
		//			printf("BROKEN\n");
					broken = true;
					break;
				}
				for(int pridej = 0; pridej <= cislice; pridej++){
					set[zacatek]=mozn[ps[exp]][cislice][pridej];
					zacatek++;
				}
				splits += cislice;

				num = num - cislice;
				num = num / 3;
			}
			if(!broken){
	//			printf("Muj set (splitu je %d):\n", splits);
				int maxt = -1;
				rep(z, zacatek){
		//			printf("%d ", set[z]);
					if(set[z]>maxt)
						maxt=set[z];
				}
				if(maxt+splits < mintime)
					mintime = maxt+splits;
//				printf("\nTrval %d\n\n", maxt+splits);
			}
			
		}
		printf("Case #%d: %d\n", i+1, mintime);




/*
		int mint = 1;
		int splitn = 0;
		if(count[2]>0)
			mint = 2;
		if(count[3]>0)
			mint = 3;
		if(count[4]==1){
			splitn = 1;
			mint = 3;
		}
		if(count[4]>1){
			splitn = 0;
			mint = 4;
		}
		if(count[5] == 1){
			mint = 4;
			splitn = 1;
		}
		if(count[5] >1){
			mint = 5;
			splitn = 0;
		}
		if(count[6]<=2){
			if(mint < 3+count[6]){
				mint = 3+count[6];
				splitn = count[6];
			}
			*/

	}


	return 0;
}

