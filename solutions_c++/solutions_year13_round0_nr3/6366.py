#include<stdio.h>
#include<math.h>

	int fair(int n){
		int tmp[200];
		int remainder;
		int i=0;
		int tp=0;
		int tp1=n;
		
		remainder=tp1%10;
		while(remainder!=0){
			tmp[i]=remainder;
			tp1=tp1/10;
			remainder=tp1%10;
			i++;	
		}
		
		tmp[i]='\0';
		int j=0;
		while(tmp[j]!='\0'){
			tp=tp*10+tmp[j];
			j++;
		}		
		
		if(tp==n){return 1;}
		else{return 0;}
		
	}
	
	int square(int n){	
		float sq=sqrt(n);
		int sq1=(int)sq;
		if(sq>sq1){return 0;}
		if(fair(sq)){return 1;}
		else{return 0;}	
	}
	
	int FairAndSquare(int a,int b){
		int count=0;//counts the fair and squares numbers in the range
		
		for(int i=a;i<=b;i++){
			if(fair(i)&&square(i)){
				count++;	
			}
		}
		return count;
	}

int main(){
	FILE *file,*f;
	int result=0;
	file=fopen("C-small-attempt0.in","r+");
	f=fopen("output.txt","w+");
	char ch;
	int Case=1; 
	int NumOfCases=0;//number of cases
	
	int A=0;//lower range
	int B=0;//upper range
	
	
	ch=fgetc(file);
	while(ch!='\n'){	
		NumOfCases=NumOfCases*10+(ch-'0');	
		ch=fgetc(file);
	}
	
	for(int k=1;k<=NumOfCases;k++){
		ch=fgetc(file);	
		while(ch!=' '){
		A=A*10+(ch-'0');
		ch=fgetc(file);	
		}
		
		ch=fgetc(file);	
		while(ch!='\n'){
		B=B*10+(ch-'0');
		ch=fgetc(file);	
		}
		
		result=FairAndSquare(A,B);
		fprintf(f,"Case #%d: %d\n",k,result);
		
	A=0;B=0;	
	}

			
	return 0;
}
