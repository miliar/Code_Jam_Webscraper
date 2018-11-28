#include <stdio.h>
#include <map>
#include <assert.h>
#include <windows.h>
using namespace std;

/*!
@para _inputfilepath 入力ファイル
@para _testcase_num テストケースの数を格納する変数
@para _width 1テストケースの横幅　要素数
@para _height 1テストケースの行数
*/
//template <typename T>
int testcase=0;
unsigned long long *radius;
unsigned long long  *ink;
unsigned long long *result;

int ReadInput(const char* _inputfilepath){
	// ,int _width=0,int _height=0,T** _inputbuf){
	printf("ファイル名%s\n",_inputfilepath);
	FILE* fp=fopen(_inputfilepath,"rb");//rbの方がいいかもしんない。改行の解釈が変わってくる

	if(fp==NULL){assert(!"ファイル名が間違っている");return false;}
	fscanf(fp,"%d",&testcase);//テストケースの読み取り
	printf("テストケース%d",testcase);
	radius=new unsigned long long[testcase];
	ink=new unsigned long long[testcase];
	result=new unsigned long long[testcase];
	//_inputbuf=new T[_testcase_num*_width*_height];
	//1テストケースは何行だ？ fscanfじゃだめかも
	for(int i=0;i<testcase;i++){
		fscanf(fp,"%llu%llu",&radius[i],&ink[i]);
		//printf("radius=%llu ink=%llu\n",radius[i],ink[i]);
	}
	fclose(fp);
	for(int i=0;i<testcase;i++){
		unsigned  long long  count=0;
		while(ink[i]>=2*radius[i]+1){
			count++;
			ink[i]-=2*radius[i]+1;
			radius[i]+=2;
		}
		result[i]=count;
	}
	return 0;
}
/*
5
1 9
1 10
3 40
1 1000000000000000000
10000000000000000 1000000000000000000


Output 

Case #1: 1
Case #2: 2
Case #3: 3
Case #4: 707106780
Case #5: 49


*/
/*!
@brief 出力用関数
Case #1: 7.000000
↑こういう場合はいいけど、２個の数値を出力するときはきつい。
小数点第何位まで、は関数の引数で対応している。
↓みたいな任意の文字列には対応していない。
Case #1: Possible
Case #3: Too Bad
*/
template <typename T>
bool Output(const char* _outputname,int _testcase_num,T* _result_array){
	FILE* fp=fopen(_outputname,"w");
	string format="Case #%: %llu";
	for(int t=0;t<_testcase_num;t++){
		fprintf(fp,"Case #%d: %llu\n",t+1,_result_array[t]);	
	}
	return 0;
}

void main(){
	
	ReadInput("A-small-attempt0.in");
	Output("A-small.txt",testcase,result);

}