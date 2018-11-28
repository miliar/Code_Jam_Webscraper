#include<iostream.h>
#include<fstream>
int lengthofL(char L[]){
	int i;
	for(i=0;L[i]!='\0';i++){
	}
	return i;
}
int numokOk_func(int l,int r){
	return (l+1)*(r+1);
}
int main(){
	FILE * fileI = fopen("1.in","r");
	FILE * fileO = fopen("1.out","w");
	int numT;
	fscanf(fileI,"%d",&numT);
	char L[101];
	int n;
	for(int nT=1;nT<=numT;nT++){
		fscanf(fileI,"%s",L);
		fscanf(fileI,"%d",&n);
		//cout<<L<<endl;
		//cout<<n<<endl;
		int numofOk = 0;
		int lengthL = lengthofL(L);
		int pos = 0;
		int result=0;
		for(int i=0;i<lengthL -n+1;i++){
			//cout<<L[i]<<endl;
			bool isOk = true;
			for(int j=i;j<i+n;j++){
				//cout<<L[j]<<" ";
				if(L[j]=='a' || L[j]=='u' || L[j]=='e' || L[j]=='o' || L[j]=='i'){
					isOk = false;
					break;
				}
			}
			
			if(isOk){
				numofOk = numokOk_func(i-pos,lengthL-j);
				result+=numofOk;
				pos = i+1;
			}
		}
		
		fprintf(fileO,"Case #%d: %d\n",nT,result);

	}
	fclose(fileI);
	fclose(fileO);
	return 0;
}