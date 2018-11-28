#include<cstdio>
#include<cstring>
#include<stdint.h>
#include<fstream>
#include<iostream>
using namespace std;

char buf[10000000];
int hui_wen_num[10000000];


int find_sum(int64_t a)
{
	int pos = 0;
	int64_t mid = 0;
	int64_t low = 0;
	int64_t high = 9999999;
	while( low <= high ){
		mid = (low+high) / 2;
		int64_t t = mid * mid;
		if( t == a ){
			pos = mid;
			break;
		}else if( t < a ){
			pos = mid;
			low = mid + 1;
		}else{
			high = mid - 1;
		}
	}
	return hui_wen_num[pos];

}

int check_hui_wen(int a)
{
	int64_t t;
	t = (int64_t)a * (int64_t)a;
	int temp[100];
	int cnt = 0;
	while( t != 0 ){
		temp[cnt] = t % 10;
		t /= 10;
		cnt++;
	}
	for(int i = 0; i < cnt / 2; ++i){
		if( temp[i] != temp[cnt-1-i] ){
			return 0;
		}
	}
	return 1;

}

int main(int argc,char** argv)
{

	memset(buf,0,sizeof(buf));
	for(int i = 1; i < 10000 ; ++i){
		if(i % 10 == 0) continue;
		int a = 0;
		int t = i;
		int m = 1;
		while( t != 0 ){
			a = a * 10 + t % 10;
			t /= 10;
			m *= 10;
		}
		a = a * m + i;
		if(a<=9999999){
			buf[a] = check_hui_wen(a);
		}
		//printf("%d " , a );
		a = 0;
		t = i;
		m = 1;
		while( t >= 10 ){
			a = a * 10 + t % 10;
			t /= 10;
			m *= 10;
		}
		a = a * m * 10 + i;
		buf[a] = check_hui_wen(a);
		//printf("%d " , a );
	}
	printf("\n");
	printf("\n");
	hui_wen_num[0] = 0;
	for(int i = 1; i < 10000000; ++i ){
		hui_wen_num[i] = hui_wen_num[i-1] + buf[i];
		if( i < 10000 && buf[i] == 1){
			printf("%d, " , i*i );
		}
	}
	FILE* input_file = fopen(argv[1],"r");
	FILE* output_file = fopen(argv[2],"w");
	int test_case_num;
	fscanf(input_file , "%d" , &test_case_num);
	for(int test_case = 0 ; test_case < test_case_num ; ++test_case) {
		int64_t A,B;
		fscanf( input_file , "%I64d%I64d",&A,&B);
		int sum_to_a = find_sum(A-1);
		int sum_to_b = find_sum(B);
		fprintf(output_file,"Case #%d: %d\n" , test_case + 1 , sum_to_b - sum_to_a);
	}
	fclose(input_file);
	fclose(output_file);


	return 0;


}