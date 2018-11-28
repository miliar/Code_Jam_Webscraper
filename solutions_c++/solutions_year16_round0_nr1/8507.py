/*input
100
0
1
2
11
1692
5
1000000
841536
225019
180824
225065
12500
530244
240506
553495
225800
913370
999996
872960
140485
900440
227991
975091
4
125
515849
460877
716407
3
582075
526189
1250
881232
481816
776275
20
685207
601401
772270
272415
10
9
148320
344889
544202
150643
86408
148450
125000
8
651991
919772
669748
808469
772815
999991
34
776294
336798
960133
930363
747990
721426
999993
40
25
607901
989845
999995
999998
268644
923595
200
819235
203211
191831
889652
283916
999999
568072
900998
70457
571776
884502
543813
999994
309834
124
7
999992
101364
550645
256611
999997
166
920555
6
363098
977735
19709

*/

#include <bits/stdc++.h>
using namespace std;

bool test[10]={false};//change

bool call(){
	for(int i=0; i<10; i++){
		if(test[i]);
		else return true;
	}
	return false;
}

void count (long int temp){
	while(temp!=0){
		test[temp%10]=true;
		temp=temp/10;
	}
	
}

int main(){

	long int t,a;
	scanf("%ld",&t);
	int j=1;
	while(t--){
		memset(test,false,sizeof(test));
		//for(long int i=0; i<10; i++)cout<<test[i];
		scanf("%ld",&a);
		if(a==0){
			printf("Case #%d: INSOMNIA\n",j);
		}
		else{
			long int i=1,temp;
			while(call()){
				temp=a*i;
				count(temp);			
				i++;
			}
			printf("Case #%d: %ld\n",j,temp);
		}

		j++;
	}
	return 0;
}