// tryagain.cpp : 定義主控台應用程式的進入點。
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
	char *data=NULL;
	char trash1[2];
	int data_number;
	char tictactoe_matrix[4][5]={0};
	/*開啟檔案*/	
	fptr=fopen("A-small-attempt3.in","rb");
	opftr=fopen("A-small-attempt3.out","wb");

	

	
	
	/*關閉檔案*/
	fclose(fptr);
	
	
	
	long file_size=doGetFileSize("A-small-attempt3.in","rb");
	data=(char*)malloc(sizeof(char)*file_size);
	int length;
	for(length=0;length<file_size;length++){
		fread(&data[length],sizeof(char),1,fptr);
		//printf("%c",data[length]);
	}
	/*先判斷有幾組data*/
	for(data_number=0;data[data_number]!=10;data_number++){
	}
	int row,col;

	for(length=(data_number+1);length<file_size;length++){
				
		if((length-(data_number+1))%21==0){
			for(row=0;row<4;row++){
				for(col=0;col<5;col++){
					data[(length)+5*row+col];
					//printf("%c",data[(length)+5*row+col]);
				}
			}
			printf("Case #%d: ",(length-(data_number+1))/21+1);
			fprintf(opftr,"Case #%d: ",(length-(data_number+1))/21+1);
			
			int game_set_flag=0;
			/*row check*/
			int row_checksum=0;
			for(row=0;row<4;row++){
				for(col=0;col<4;col++){
					row_checksum=row_checksum+data[(length)+5*row+col];
				}
				if(row_checksum==4*88||row_checksum==3*88+84){
					printf("X won\n");
					fprintf(opftr,"X won\n");
					game_set_flag=1;
					
				}
				if(row_checksum==4*79||row_checksum==3*79+84){
					printf("O won\n");
					fprintf(opftr,"O won\n");
					game_set_flag=1;
					
				}
				row_checksum=0;
				if(game_set_flag==1)break;
			}
			if(game_set_flag==0){
			/*col check*/
				int col_checksum=0;
				for(col=0;col<4;col++){
					for(row=0;row<4;row++){				
						col_checksum=col_checksum+data[(length)+5*row+col];
					}
					if(col_checksum==4*88||col_checksum==3*88+84){
						printf("X won\n");
						fprintf(opftr,"X won\n");
						game_set_flag=1;
						
					}
					if(col_checksum==4*79||col_checksum==3*79+84){
						printf("O won\n");
						fprintf(opftr,"O won\n");
						game_set_flag=1;
						
					}			
					col_checksum=0;
					if(game_set_flag==1)break;
				}
			}
			
			int diogonal_checksum=0;
			/*diogonal check1*/
			if(game_set_flag==0){
				
				for(col=0;col<4;col++){							
						diogonal_checksum=diogonal_checksum+data[(length)+5*col+col];
				}
				if(diogonal_checksum==4*88||diogonal_checksum==3*88+84){
					printf("X won\n");
					fprintf(opftr,"X won\n");
					game_set_flag=1;
				}
				if(diogonal_checksum==4*79||diogonal_checksum==3*79+84){
					printf("O won\n");
					fprintf(opftr,"O won\n");
					game_set_flag=1;
				}			
				diogonal_checksum=0;
			}
			
			if(game_set_flag==0){
				/*diogonal check2*/
				for(col=3;col>=0;col--){							
						diogonal_checksum=diogonal_checksum+data[(length)+5*col+col];
				}
				if(diogonal_checksum==4*88||diogonal_checksum==3*88+84){
					printf("X won\n");
					fprintf(opftr,"X won\n");
					game_set_flag=1;
				}
				if(diogonal_checksum==4*79||diogonal_checksum==3*79+84){
					printf("O won\n");
					fprintf(opftr,"O won\n");
					game_set_flag=1;
				}			
				diogonal_checksum=0;
			}

			int completed=1;
			if (game_set_flag==0){
				for(row=0;row<4;row++){
					for(col=0;col<4;col++){
						if(data[(length)+5*row+col]==46){
							printf("Game has not completed\n");
							fprintf(opftr,"Game has not completed\n");
							completed=0;
							break;
						}
						
					}
					if(completed==0)break;
					
				}
			}
			completed=1;
			int count=0;
			if (game_set_flag==0){
				for(row=0;row<4;row++){
					for(col=0;col<4;col++){
						if(data[(length)+5*row+col]!=46){
							count++;
						}
					}
				}
				if(count==16){
					printf("Draw\n");
					fprintf(opftr,"Draw\n");
					count=0;
				}

			}



	
	



			
		}

	}
	
	
	//system("PAUSE");
	fclose(opftr);
	
	
	
	return 0;
}
long doGetFileSize(const char* filePath, const char* mode){
  long fileLength = 0;
  FILE *fp;
  //開啟檔案
  if(! (fp = fopen(filePath, mode))){
    //File Open Error
    return -1;
  }
  //移動指標到檔案的結尾
  if(fseek(fp, 0, SEEK_END)) {
    //File seek error.
    return -1;
  }
  //取得檔案大小 單位byte
  fileLength = ftell(fp);
  //移動指標回檔案起始
  rewind(fp);
 
  return fileLength;
}

