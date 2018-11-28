#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

int ans;
double A;
double B;

bool genNum(int* value, int totalLength, int curr){
	int i;
	bool result;
	if(totalLength <= curr*2){
		int* pali;
		int flag;
		double tmp = 0;
		double a;
				
		for(i=0;i<totalLength;i++){
			tmp *= 10;
			tmp += (double)value[i];
		}
		if(tmp*tmp > B){
			return false;
		}
		else if(tmp*tmp < A){
			return true;
		}
		// In range		
		pali = (int*)malloc(sizeof(int)*(totalLength*2));
		memset(pali,0,totalLength*2);

		for(i=0;i<totalLength;i++){
			for(int j=0;j<totalLength;j++){
				pali[i+j] += (value[i]*value[j]);
				pali[i+j+1] += (pali[i+j]/10);
				pali[i+j] %= 10;
			}
		}
		if(pali[totalLength*2-1] == 0){
			flag = totalLength*2-2;
		}
		else{
			flag = totalLength*2-1;
		}

		result = true;
		for(i=0;i<=flag;i++){
			if(pali[i] != pali[flag]){
				result = false;
				break;
			}
			flag--;
		};
		if(result){
			ans++;
		}		

		return true;
	}
	else{
		if(curr == 0){
			i = 1;
		}
		else{
			i = 0;
		}
		for(;i<10;i++){
			value[curr] = i;
			value[totalLength-1-curr] = i;
			result = genNum(value,totalLength,curr+1);
			if(!result){	// over range
				break;
			}
		}
		return result;
	}
}


int main(){

	int T;
	int caseNum = 1;

	double temp;
	int minLength;
	int maxLength;
	int* pali_sqrt;

	scanf("%d",&T);
	while(T > 0){
		ans = 0;
		scanf("%lf %lf",&A,&B);
		
		minLength = ceil(log10(sqrt(A)+1));
		maxLength = ceil(log10(sqrt(B)+1));

		for(int i=minLength;i<=maxLength;i++){
			pali_sqrt = (int*)malloc(sizeof(int)*i);
			genNum(pali_sqrt,i,0);						
		}

		printf("Case #%d: %d\n",caseNum, ans);
		caseNum++;
		T--;
	};

	return 0;
}