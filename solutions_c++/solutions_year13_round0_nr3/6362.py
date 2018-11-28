#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <ctype.h>
#include <stdint.h>

using namespace std;
int do_work( int num );

#define FGETS(in)	memset( buf, sizeof(buf), 0); \
	                fgets(buf,sizeof(buf),in)
typedef unsigned int u32;
char buf[255]={0};
char out_buf[50000]={0};
char *pch;


char num[200];
uint32_t N=0;
uint32_t M=0;

bool is_palindrome(char * num){
	int len = strlen(num);
	int middle=0;
	if( len == 1 ){
		return true;
	}else if( len == 2 ){
		if( *num == *(num+1) ){
			return true;
		}else{
			return false;
		}
	}
	for( int i=0 ; i<len/2 ; i++){
		if( *(num+i) != *(num+len-1-i)){
			return false;
		}
	}
	return true;
}

uint32_t do_work( uint32_t num ){
	uint32_t b, m=0x40000000,y=0,x;
	x=num;
	while( m!=0){
		b =y|m;
		y>>=1;
		if( x >=b ){
			x-=b;
			y |=m;
		}
		m>>=2;
	}
	uint32_t sql_big = (y+1)*(y+1);
	uint32_t sql_small = (y)*(y);
	if(sql_big == num || sql_small == num){
		return 1;
	}
	return 0;

}
#if 0
uint32_t do_work( uint32_t num ){
	register uint32_t i,sqr;
	char buf[255]={0};
	if ( num  == 1 || num == 4){
		return 1;
	}
	for( i= 1; i < num/2 ; i++){
		sqr = i*i;
		if( sqr == num ){
			sprintf(buf,"%u",i);
			if(is_palindrome(buf)){
				//printf("%u\n",num);
				return 1;
			}else{
				return 0;
			}
		}else if (sqr > num ){
			return 0;
		}
	}
	return 0;
}
#endif

int MAX;
int MIN;
int main( int argc, char ** argv ){
	FILE * in;
	FILE * out;
	u32 count = 0;
	char *pch;
	uint32_t i,j,k=0;
	uint32_t num_true=0;
	char tmp_buf[255]={0};
	printf("%s %s\n", argv[1],argv[2]);
	in = fopen( argv[1], "r" );
	if( NULL == in) 
		return 1;
	out = fopen( argv[2], "w" );
	if( NULL == out) 
		return 2;
	FGETS(in);
	sscanf(buf,"%u",&count);		// get count fix

	for ( i=0 ;i<count; i++ ){
		sprintf(out_buf,"%s Case #%u:",out_buf,i+1);			
		FGETS(in);	
		sscanf(buf,"%lu %lu\n",&MIN,&MAX);
    
		for( j = MIN ; j<(MAX+1) ; j++){
			sprintf(tmp_buf,"%d",j);
			if( true == is_palindrome(tmp_buf)){
				num_true  += do_work(j);
			}
		}
		sprintf(out_buf,"%s %d\n",out_buf,num_true);
		num_true = 0;
	}
	fwrite( out_buf, 1, strlen(out_buf), out);
	fclose(in);
	fclose(out);
	return 0;
}
