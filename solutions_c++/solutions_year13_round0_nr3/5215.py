#include<cstdlib>
#include<iostream>
#include<cmath>

using namespace std;

int digit(int y){
	int digit=1;
	while(y>10){
		y /= 10;
		digit++;	
	}
	return digit;
}


bool pldms(int x){	
		int val=0;
		int y = x;
		int digits = digit(x);
		while(digits!=0){
			val = val*10 + y%10;
			y /=10;	
			digits--;		
		}
		if(x ==val)
			return true;
		return false;	
}

int main()
{
	FILE *fp;
	FILE *wfp;
	int case_number;
	int output_case=1;	
	fp = fopen("C-small-attempt0.in","r");
	wfp = fopen("C-small-attempt0.out","w");
	fscanf(fp,"%d\n",&case_number);
	while(case_number>0){
		int lower,upper,ans=0;		
		fscanf(fp,"%d %d\n",&lower, &upper);
		int idx = lower;
		float sq;
		for(;idx<=upper;idx++){
			sq = sqrt(idx);
			if(sq !=ceil(sq) || sq!=floor(sq))
				continue;			
			if(pldms(sq) && pldms(idx)){
				ans++;
			}
		}
		fprintf(wfp,"Case #%d: %d\n",output_case,ans);
		case_number--;
		output_case++;	
	}
		
}
