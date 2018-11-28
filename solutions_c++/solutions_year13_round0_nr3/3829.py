#include <stdio.h>
#include <map>
#include <assert.h>
#include <windows.h>
#include <mmsystem.h>
#pragma comment(lib,"WinMM.Lib")
using namespace std;
bool IsPalindromes(double in){//‰ñ•¶‚©‚Ç‚¤‚©”»’f‚·‚éB
	char buf[200];
	char inverted[200];
	sprintf(buf,"%.0lf",in);//”š‚ğ•¶š—ñ‚É‚µ‚Ä ‚±‚±‚ÅH•v‚µ‚È‚¢‚Æ‚¢‚©‚ñB
	
	int length=strlen(buf);//•¶š‚Ì’·‚³
	for(int s=0;s<length;s++){//•¶š—ñ‚ğ‹t‚³‡‚ÉŠi”[‚·‚é
		//if(buf[s]!=buf[length-s]) return false;
		inverted[s]=buf[length-s-1];
	}
	//printf("•¶š‚Ì’·‚³%d\n",length);
	//printf("buf%s\n",buf);
	inverted[length]='\0';
	//printf("inv:%s\n",inverted);
	if(strcmp(buf,inverted)==0){//‚à‚µŠ®‘Sˆê’v‚È‚ç‚Î
		return true;
	}
	return false;
}

double *result;
__int64 CalcP(double* large_array,double max_calc){
	__int64 count=0;
	double* pt=large_array;
	double* rpt=result;
	while(*pt!=-1){
		double pows=(*pt)*(*pt);
		if(IsPalindromes(pows)){
			*rpt=pows;
			rpt++;
			count++;
		}
		pt++;
	}
	return count;
	
	//double minimum=ceil(sqrt(from));
	//double maximum=sqrt(to);
	//for(double i=minimum;i<=maximum;i+=1.0){
	//		//i‚ª‰ñ•¶‚©‚Ç‚¤‚©”»’f‚·‚éB
	//	if(IsPalindromes(i,true)){
	//		if(IsPalindromes(i*i,false)){
	//			//‚³‚ç‚É‚»‚ê‚ª‰ñ•¶‚©’²‚×‚éB
	//	//printf("³‰ğ‚Í‚±‚ê%d‚Ì‚×‚«æ%lf\n",i,i*i);
	//			//printf("%.0lf\n",i);
	//			palindromes++;
	//		}
	//	}
	//}	
	//
	//return palindromes;

}

double mirror(double in,int even){
	
	char inverted[200];
	char buf[200];
	sprintf(buf,"%.0lf",in);

	int length=strlen(buf);//•¶š‚Ì’·‚³
	
	for(int s=0;s<length/2+even;s++){//•¶š—ñ‚ğ‹t‚³‡‚ÉŠi”[‚·‚é
		//if(buf[s]!=buf[length-s]) return false;
		if(even==1){	inverted[s]=buf[length-s-1];}
		else{inverted[s]=buf[length-s-2];}
	}
		inverted[length]='\0';
		
		return atof(strcat(buf,inverted));
}


void main(){
	double max_calc=14.0;
	FILE* fp=fopen("C-small-attempt0.in","r");
	char firstline[100];
	fgets(firstline,100,fp);
	int test_num=atoi(firstline);
	
	FILE* wfp=fopen("output.txt","w");
	__int64 large_array_size=(2.0*pow(4.0,max_calc/2.0)-1.0);
	double *large_array;
	try{
	 large_array=new double[large_array_size];//(double*)malloc(large_array_size);
	}catch(bad_alloc){
		assert(!"a");
	}//new double[large_array_size];
	result=new double[large_array_size];

	double* pt=&large_array[0];
	//int counter=0;
	__int64 pre_large_array=1;
	__int64 pre_large_array2=1;

	for(int i=0;i<(int)max_calc;i++){

		for(int k=1;k<=(int)(3.0/2.0*((int)pow(3.0,(double)(i/2+1))-1));k++){
			/*if(pre_large_array==0 && k==0){
				pre_large_array++;
				continue;
			}
			if(pre_large_array2==0 && k==0){
				pre_large_array2++;
				continue;
			}*/

		double temp=0;
		if(i%2==0){
			for(int j=0;j<=i/2;j++){
				temp+= ((pre_large_array >> 2*j) & 3)*pow(10.0,(double)j);
				
			}
			*pt=mirror(temp,0);
		}
		else{
			for(int j=0;j<=i/2;j++){
				temp+= ((pre_large_array2 >> 2*j) & 3)*pow(10.0,(double)j);
			}
			*pt=mirror(temp,1);
		}
		if(i%2==0) pre_large_array++;
		else pre_large_array2++;
		pt++;
		}//end k
		
		
	}//end i
	*pt=-1;
	//‚Ù‚µ‚¢”z—ñ‚Ío—ˆ‚½
	for(int k=0;k<test_num;k++){
		unsigned long system_time_first= timeGetTime();
		double from,to;
		fscanf(fp,"%lf %lf\n",&from,&to);
		//printf("from %.0lf to %.0lf\n",from,to);
		__int64 num=CalcP(large_array,max_calc);//result‚ÉğŒ‚É‚ ‚¤‚â‚Â‚ğ“ü‚ê‚½B
		__int64 count=0;
		for(__int64 i=0;i<num;i++){
			if(result[i]>=from &&result[i]<=to)
			{
				count++;
			}
			}//end i
		fprintf(wfp,"Case #%d: %d\n",k+1,count);
		printf("test case #%d from %.0lf to %.0lf\n",k,from,to);
		unsigned long system_time_second= timeGetTime();
	printf("ŒvZ‚É‚©‚©‚Á‚½ŠÔ%dmsec\n",system_time_second-system_time_first);	
		
	}//end k
	delete[] large_array;
	fclose(wfp);
	fclose(fp);	

}