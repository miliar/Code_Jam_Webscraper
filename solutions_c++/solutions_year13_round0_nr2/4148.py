#include <stdio.h>
#include <map>
#include <assert.h>
using namespace std;

map<char,int> hash;
enum RESULT{YES,NO};


RESULT JudgeG(int* input,int h_num,int v_num){

	int i,j,k,g_min,g_max,preflag;
	g_min=100;
	g_max=0;

	for(i=0;i<h_num*v_num;i++){
		if(input[i]>g_max) g_max=input[i];
		if(input[i]<g_min) g_min=input[i];
	}
	//printf("g_min=%d,g_max=%d\n",g_min,g_max);
	for(j=g_min;j<=g_max;j++){

		for(k=0;k<h_num*v_num;k++){
			if(input[k]<j) return NO;
		}

		bool* flag = new bool[h_num*v_num];
		memset(flag,0,h_num*v_num);
		
		//‰¡‚ð’²‚×‚é
		for(i=0;i<h_num;i++){
			int *oneline_h=new int[v_num];
			memcpy(oneline_h,&input[i*v_num],v_num*sizeof(int));
			preflag=0;//
			for(k=0;k<v_num;k++){
				if(preflag==0){
					if(oneline_h[k]<=j) preflag=-1;
					else preflag=1;
				}
				else if(preflag==-1 && oneline_h[k]>j){
					preflag=0;
					break;
				}
				else if(preflag==1 && oneline_h[k]<=j){
					preflag=0;
					break;
				}
				
			}//end k
			//printf("preflag=%d\n",preflag);
			
			if(preflag==-1){
					for(k=0;k<v_num;k++) flag[i*v_num+k]=1;
			}
			delete[] oneline_h;

		}//end i
		//c‚ð’²‚×‚é
		for(i=0;i<v_num;i++){
			int* oneline_v=new int[h_num];
			for(k=0;k<h_num;k++){
				oneline_v[k]=input[k*v_num+i];
			}
			preflag=0;
			for(k=0;k<h_num;k++){
				if(preflag==0){
					if(oneline_v[k]<=j) preflag=-1;
					else preflag=1;
				}
				else if(preflag==-1 && oneline_v[k]>j){
					preflag=0;
					break;
				}
				else if(preflag==1 && oneline_v[k]<=j){
					preflag=0;
					break;
				}

			}//end k
			if(preflag==-1){
					for(k=0;k<h_num;k++) flag[k*v_num+i]=1;
			}
			delete[] oneline_v;
		}//end i2
		/*for(int y=0;y<h_num;y++){
			for(int x=0;x<v_num;x++){
				printf("%d,",flag[y*v_num+x]);
			}
			puts("");
		}*/
		for(k=0;k<h_num*v_num;k++){
			if(flag[k]==1) input[k]++; 
		}
		delete[] flag;

	}//end j

	return YES;

}

void main(){
	//FILE* fp=fopen("input.in","r");
	FILE* fp=fopen("B-large.in","r");
	char firstline[10];
	fgets(firstline,10,fp);
	int test_num=atoi(firstline);

	FILE* wfp=fopen("output-large.txt","w");
		
	for(int k=0;k<test_num;k++){
		int h_num,v_num;
		fscanf(fp,"%d %d\n",&h_num,&v_num);
		//
		//char *format=new char[h_num*2+1];
		int *input=new int[h_num*v_num];

		char c[500];
		char* height_s;
		int height_n;
		for(int i=0;i<h_num;i++){

			fgets(c,500,fp);
			for(int j=0;j<v_num;j++){
				if(j%v_num==0){ 
					height_s=strtok(c," ");
					height_n=atoi(height_s);
					input[i*v_num+j]=height_n;
				}
				else{
					height_s=strtok(NULL," ");

					height_n=atoi(height_s);
					input[i*v_num+j]=height_n;

				}
			
			}//end j
		}//end i
		
		fprintf(wfp,"Case #%d: ",k+1);
		int ret=JudgeG(input,h_num,v_num);
		switch(ret){
			case YES:
				fprintf(wfp,"YES");
				break;
			case NO:
				fprintf(wfp,"NO");
				break;
		}//end switch
		fprintf(wfp,"\n");

	}//end k
	fclose(wfp);
	fclose(fp);	

}