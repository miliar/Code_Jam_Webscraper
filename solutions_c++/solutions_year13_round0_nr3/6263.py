// tryagain.cpp : �w�q�D���x���ε{�����i�J�I�C
//

#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include <iostream>
using namespace std;
long doGetFileSize(const char* filePath, const char* mode);
 


int main(void)
{	
				
	FILE *fptr;
	FILE *opftr;
	char **data_matrix=NULL;
	char **data_matrix2=NULL;
	char *data;
	char trash1[2];
	int data_number;
	int col_size,row_size;
	int col,row;
	int length;
	/*�}���ɮ�*/	
	fptr=fopen("C-small-attempt7.in","rb");
	opftr=fopen("C-small-attempt7.out","wb");

	long file_size=doGetFileSize("C-small-attempt7.in","rb");

	
	fscanf(fptr,"%d",&data_number);
	/*�P�_���X��data*/
	int case_num=1;
	
	int add_term,read_row_col=0;

	for(length=0;length<data_number;length++){		
		
		int num1=0,num2=0;
		fscanf(fptr,"%d",&num1);
		fscanf(fptr,"%d",&num2);
		int count=0;
		int digit_array[4]={0};
		int digit_array2[4]={0};
		int j;
		for(int i=num1;i<=num2;i++){
			if(sqrt(double(i))-floor(sqrt(double(i)))==0){
				
					
			
					digit_array[0]=int((double(i)))/1000;
					digit_array[1]=int((double(i)))%1000/100;
					digit_array[2]=int((double(i)))%100/10;
					digit_array[3]=int((double(i)))%10/1;
					
					
					digit_array2[0]=int(sqrt(double(i)))/1000;
					digit_array2[1]=int(sqrt(double(i)))%1000/100;
					digit_array2[2]=int(sqrt(double(i)))%100/10;
					digit_array2[3]=int(sqrt(double(i)))%10/1;
				
					
					for(j=0;j<4;j++){
						if (digit_array[j]!=0)break;
					}
					int k;
					for(k=0;k<4;k++){
						if (digit_array2[k]!=0)break;
					}
					if(j==0){
						if(digit_array[0]==digit_array[3]&&digit_array[1]==digit_array[2]){
							if(k==0){
								if(digit_array2[0]==digit_array2[3]&&digit_array2[1]==digit_array2[2]){
									count++;
								}
							}
							if(k==1){
								if(digit_array2[1]==digit_array2[3]){
									count++;
								}
							}
							if(k==2){
								if(digit_array2[2]==digit_array2[3]){
									count++;
								}
							}
							if(k==3){							
								count++;
							}
						}
					}
							
						

					if(j==1){
						if(digit_array[1]==digit_array[3]){
							if(k==0){
								if(digit_array2[0]==digit_array2[3]&&digit_array2[1]==digit_array2[2]){
									count++;
								}
							}
							if(k==1){
								if(digit_array2[1]==digit_array2[3]){
									count++;
								}
							}
							if(k==2){
								if(digit_array2[2]==digit_array2[3]){
									count++;
								}
							}
							if(k==3){							
								count++;
							}
							
						}
					}

					if(j==2){
						if(digit_array[2]==digit_array[3]){
							if(k==0){
								if(digit_array2[0]==digit_array2[3]&&digit_array2[1]==digit_array2[2]){
									count++;
								}
							}
							if(k==1){
								if(digit_array2[1]==digit_array2[3]){
									count++;
								}
							}
							if(k==2){
								if(digit_array2[2]==digit_array2[3]){
									count++;
								}
							}
							if(k==3){							
								count++;
							}
						}
					}

					if(j==3){
						if(k==0){
							if(digit_array2[0]==digit_array2[3]&&digit_array2[1]==digit_array2[2]){
								count++;
							}
						}
						if(k==1){
							if(digit_array2[1]==digit_array2[3]){
								count++;
							}
						}
						if(k==2){
							if(digit_array2[2]==digit_array2[3]){
								count++;
							}
						}
						if(k==3){							
							count++;
						}
					}
						
							
					//printf("%d ",int(sqrt(double(i))));


					}
		}
		printf("Case #%d: %d\n",case_num,count);
		fprintf(opftr,"Case #%d: %d\n",case_num,count);
		count=0;
		case_num++;
		//system("PAUSE");
	
			
	
	}


	
	
	
	
	

	//system("PAUSE");
	fclose(opftr);
	fclose(fptr);
	return 0;
}
long doGetFileSize(const char* filePath, const char* mode){
  long fileLength = 0;
  FILE *fp;
  //�}���ɮ�
  if(! (fp = fopen(filePath, mode))){
    //File Open Error
    return -1;
  }
  //���ʫ��Ш��ɮת�����
  if(fseek(fp, 0, SEEK_END)) {
    //File seek error.
    return -1;
  }
  //���o�ɮפj�p ���byte
  fileLength = ftell(fp);
  //���ʫ��Ц^�ɮװ_�l
  rewind(fp);
 
  return fileLength;
}

