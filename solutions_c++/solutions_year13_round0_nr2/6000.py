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
	fptr=fopen("B-small-attempt6.in","rb");
	opftr=fopen("B-small-attempt6.out","wb");

	long file_size=doGetFileSize("B-small-attempt6.in","rb");

	
	data=(char*)malloc(sizeof(char)*file_size);

	fread(&data[0],sizeof(char),1,fptr);
	for(data_number=0;data[data_number]!=10;data_number++){
		fread(&data[data_number],sizeof(char),1,fptr);
		if(data[data_number]==10)break;

	}
	/*�P�_���X��data*/
	int case_num=1;
	
	int add_term,read_row_col=0;

	for(length=data_number+1;length<file_size;length++){		
		
		if(read_row_col==0){
			fread(&data[length],sizeof(char),1,fptr);
			row_size=(data[length]-48);			
			add_term=1;
			if((data[length]-48)==1){
				fread(&data[length+1],sizeof(char),1,fptr);
				if(data[length+1]-48==0){
					row_size=10;
					add_term=1;
				}
				else{
					add_term=0;
				}
			}
			for(int i=0;i<add_term;i++){
				fread(&data[length],sizeof(char),1,fptr);
			}
			fread(&data[length],sizeof(char),1,fptr);
			col_size=data[length]-48;
			add_term=1;


			if(data[length]-48==1){
				fread(&data[length],sizeof(char),1,fptr);

				if(data[length]-48==0){
					col_size=10;
					add_term=1;				
				}
				else{
					add_term=0;
				}
			}
			for(int i=0;i<add_term;i++){
				fread(&data[length],sizeof(char),1,fptr);
			}
			read_row_col=1;
		}
	
			
		/*����0���ɭԤ~�i�HŪ�� �A�M��t�m�O�����m*/
			
		
		data_matrix=(char**)malloc(sizeof(char*)*row_size);
		for(row=0;row<row_size;row++){
			data_matrix[row]=(char*)malloc(sizeof(char)*col_size*2);
		}
		for(row=0;row<row_size;row++){
			for(col=0;col<col_size*2;col++){
				fread(&data_matrix[row][col],sizeof(char),1,fptr);
				printf("%c",data_matrix[row][col]);
			}
		}
		
		printf("\n");
		read_row_col=0;

		if(row_size==1||col_size==1){
			printf("Case #%d: YES\n",case_num);
			fprintf(opftr,"Case #%d: YES\n",case_num);
			case_num++;
			continue;
		}
		/*�ۤv�s�y���x�}*/
		data_matrix2=(char**)calloc(sizeof(char*),row_size);
		for(row=0;row<row_size;row++){
			data_matrix2[row]=(char*)calloc(sizeof(char),col_size*2);
		}
		for(row=0;row<row_size;row++){
			for(col=0;col<col_size*2;col++){				
				if(col%2==0)data_matrix2[row][col]='2';
				if(col_size*2-1==col)data_matrix2[row][col]=data_matrix[row][col];
			}
		}
		/*row check*/
		int check_number=0;
		for(row=0;row<row_size;row++){
			for(int i=0;i<col_size*2-2;i+=2){
				if(data_matrix[row][i]==data_matrix[row][i+2]){
					check_number++;
				}
			}
		
			if(check_number+1==col_size){
				for(col=0;col<col_size*2;col++){
					if(col%2==0)data_matrix2[row][col]=data_matrix[row][0];
				}
			}
			check_number=0;
		}
		/*for(row=0;row<row_size;row++){
			for(col=0;col<col_size*2;col++){
				printf("%c",data_matrix2[row][col]);
			}
		}*/

		/*col check*/
		for(col=0;col<col_size*2;col++){
			for(int i=0;i<row_size-1;i++){
				if(data_matrix[i][col]==data_matrix[i+1][col]){
					check_number++;
				}
				if(check_number+1==row_size){
					for(row=0;row<row_size;row++){
						data_matrix2[row][col]=data_matrix[0][col];
					}
				}
			}
			check_number=0;
		
		}

		int sum=0;
		printf("\n");
		for(row=0;row<row_size;row++){
			for(col=0;col<col_size*2;col++){
				printf("%c",data_matrix2[row][col]);
				sum=sum+(data_matrix2[row][col]-data_matrix[row][col]);
			}
		}
		if(col_size<0||row_size<0||case_num>100)break;
		if(sum==0){
			printf("Case #%d: YES",case_num);
			fprintf(opftr,"Case #%d: YES\n",case_num);
		}
		else{
			printf("Case #%d: NO",case_num);
			fprintf(opftr,"Case #%d: NO\n",case_num);
		}
		
		sum=0;
		printf("\n");
		case_num++;
		if(case_num>100){
			break;
		}


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

