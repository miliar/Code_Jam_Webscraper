#include <stdio.h>
#include <math.h>

int find_fair(int a){
	int aa[100]={0}, digit_a=0, p;
	int ch=0;
	
	while(a){
		aa[digit_a] = a%10;
		a/=10;
		digit_a++;
	}		
	for(p=0 ; p<digit_a ; p++){   //fair 찾기
		if(aa[p] != aa[digit_a-p-1]){
			ch=1;
			break;
		}
	}
	if(ch==1) return 1;
	else return 0;

}

int find_square(int a){
	double root;

	root = sqrt((double)a);
	if(root - (int)root != 0 ) return 1;
	else return 0;
}

int main()
{
	FILE* input = fopen("C-small-attempt0.in","r");
	FILE* output = fopen("Csmall.out","w");
	int t,k;
	fscanf(input,"%d",&t);
	for(k=0 ; k<t ; k++){
		int a,b,i,j;
		int cnt=0;
		double root;
		fscanf(input,"%d %d",&a,&b);

		for(i=a ; i<=b ; i++){
			if(find_square(i)) continue; //square 거르기

			if(find_fair(i)) continue;

			if(find_fair((int)sqrt((double)i))) continue;
			//if(find_square((int)sqrt((double)i))) continue;
			cnt++;
		}
		fprintf(output,"Case #%d: %d\n", k+1, cnt);

	}
	return 0;
}