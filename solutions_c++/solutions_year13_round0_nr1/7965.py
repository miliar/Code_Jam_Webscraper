#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>


#define abs(n) (n<0 ? -n: n)
using namespace std;
int do_work(void );

#define WORK_WITH_STR( buf, sep )		 \
								         \
		pch = strtok( buf, sep );        \
		while( pch != NULL ){	         \
		    do_work( pch );				 \
			pch = strtok ( NULL, " ");	 \
		}						         \

#define FGETS(in)	memset( buf, sizeof(buf), 0); \
	                fgets(buf,sizeof(buf),in)
typedef unsigned int u32;
char buf[255]={0};
char out_buf[1000]={0};
char *pch;


char chess[4][4]={0};
int do_work( void ){
    int i,j;
	int x_count=0;
	int o_count=0;
	int t_count=0;
	int dot_count=0;
	int x_win = 0;
	int y_win = 0;
	int not_c = 0;
	for( i=0 ; i< 4; i++){
		x_count= o_count=t_count=dot_count=0;
		for( j=0 ; j< 4; j++){
			switch( chess[i][j]){
				case 'X':
					x_count++;
					break;
				case'O':
					o_count++;
					break;
				case 'T':
					t_count++;
					break;
				case '.':
					dot_count++;
					break;
		}
		}
		if( (x_count+ t_count ) == 4 ){
			return 1;
		}else if( (t_count+ o_count) == 4 ){
			return 2;
		}else if( dot_count > 2 ||	// ... ....
			( x_count ==2 && ( t_count == 1 && dot_count == 1) ) || //xxt. 
			( o_count ==2 && ( t_count == 1 && dot_count == 1) ) || //oot.
			( x_count == 1 && t_count == 1 && o_count == 0) ||  //xt..
			( x_count == 0 && t_count == 1 && o_count == 1 )
		 ){ // ot..
			 not_c = 1;
		}
	}

	x_count= o_count=t_count=dot_count=0;
	for( i=0; i< 4; i++){
		switch(chess[i][i]){
				case 'X':
					x_count++;
					break;
				case'O':
					o_count++;
					break;
				case'T':
					t_count++;
					break;
				case '.':
					dot_count++;
					break;
		}
	}

	if( (x_count+t_count ) == 4 ){
		return 1;
	}else if( (t_count+ o_count) == 4 ){
		return 2;
	}
	if( dot_count > 2 ||	// ... ....
			( x_count ==2 && ( t_count == 1 && dot_count == 1) ) || //xxt. 
			( o_count ==2 && ( t_count == 1 && dot_count == 1) ) || //oot.
			( x_count == 1 && t_count == 1 && o_count == 0) ||  //xt..
			( x_count == 0 && t_count == 1 && o_count == 1 )){ // ot..
			not_c = 1;
	}

	if( (x_count+t_count ) == 4 ){
		return 1;
	}else if( (t_count+ o_count) == 4 ){
		return 2;
	}

	x_count= o_count=t_count=dot_count=0;
	for( i=0; i< 4; i++){
		printf("%d\n",abs(3-i));
		switch(chess[i][abs(3-i)]){
				case 'X':
					x_count++;
					break;
				case'O':
					o_count++;
					break;
				case'T':
					t_count++;
					break;
				case '.':
					dot_count++;
					break;
		}

	}
	if( (x_count+t_count ) == 4 ){
		return 1;
	}else if( (t_count+ o_count) == 4 ){
		return 2;
	}else if( dot_count > 2 ||	// ... ....
			( x_count ==2 && ( t_count == 1 && dot_count == 1) ) || //xxt. 
			( o_count ==2 && ( t_count == 1 && dot_count == 1) ) || //oot.
			( x_count == 1 && t_count == 1 && o_count == 0) ||  //xt..
			( x_count == 0 && t_count == 1 && o_count == 1 )){ // ot..
			not_c = 1;
	}

	for( i=0 ; i<4; i++){
		x_count= o_count=t_count=dot_count=0;
		for( j = 0; j< 4; j++){
			switch( chess[j][i]){
				case 'X':
					x_count++;
					break;
				case'O':
					o_count++;
					break;
				case'T':
					t_count++;
					break;
				case '.':
					dot_count++;
					break;
			}
		}
		if( (x_count+ t_count ) == 4 ){
			return 1;
		}else if( (t_count+ o_count) == 4 ){
			return 2;
		}
		if( dot_count > 2 ||	// ... ....
			( x_count ==2 && ( t_count == 1 && dot_count == 1) ) || //xxt. 
			( o_count ==2 && ( t_count == 1 && dot_count == 1) ) || //oot.
			( x_count == 1 && t_count == 1 && o_count == 0) ||  //xt..
			( x_count == 0 && t_count == 1 && o_count == 1 )){ // ot..
			not_c = 1;
		}
	}
	if( not_c ) return 3;
	return 4;
}

const char x_win_str[]="X won";
const char o_win_str[]="O won";
const char not_completed[]="Game has not completed";
const char draw[]="Draw";
int main( int argc, char ** argv ){
	FILE * in;
	FILE * out;
	u32 count = 0;
	char *pch;
	int i,j,k;
	int res;
	printf("%s %s\n", argv[1],argv[2]);
	in = fopen( argv[1], "r" );
	if( NULL == in) 
		return 1;
	out = fopen( argv[2], "w" );
	if( NULL == out) 
		return 2;
	FGETS(in);
	sscanf(buf,"%u",&count);		// get count fix

	for ( i=0 ; i<count; i++ ){
		sprintf(out_buf,"%s Case #%u:",out_buf,i+1);
		//WORK_WITH_STR(buf," ");
		for(j=0; j<4; j++){
			FGETS(in);
			chess[j][0] = buf[0];
			chess[j][1] = buf[1];
			chess[j][2] = buf[2];
			chess[j][3] = buf[3];
		}
		FGETS(in);
		res = do_work();
		char * res_buf;
		switch( res ){
		case 1:
			res_buf = (char *)x_win_str;break;
		case 2:
			res_buf = (char *)o_win_str;break;
		case 3:
			res_buf = (char *)not_completed;break;
		case 4:
			res_buf = (char *)draw;break;
		}
		sprintf(out_buf,"%s %s\n",out_buf,res_buf);		
	}
	fwrite( out_buf, 1, sizeof(out_buf), out);
	fclose(in);
	fclose(out);
	return 0;
}
