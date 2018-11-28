#include <stdio.h>
#include <map>
#include <assert.h>
#include <windows.h>
using namespace std;

/*!
@para _inputfilepath ���̓t�@�C��
@para _testcase_num �e�X�g�P�[�X�̐����i�[����ϐ�
@para _width 1�e�X�g�P�[�X�̉����@�v�f��
@para _height 1�e�X�g�P�[�X�̍s��
*/
//template <typename T>
int testcase=0;
unsigned long long *radius;
unsigned long long  *ink;
unsigned long long *result;

int ReadInput(const char* _inputfilepath){
	// ,int _width=0,int _height=0,T** _inputbuf){
	printf("�t�@�C����%s\n",_inputfilepath);
	FILE* fp=fopen(_inputfilepath,"rb");//rb�̕���������������Ȃ��B���s�̉��߂��ς���Ă���

	if(fp==NULL){assert(!"�t�@�C�������Ԉ���Ă���");return false;}
	fscanf(fp,"%d",&testcase);//�e�X�g�P�[�X�̓ǂݎ��
	printf("�e�X�g�P�[�X%d",testcase);
	radius=new unsigned long long[testcase];
	ink=new unsigned long long[testcase];
	result=new unsigned long long[testcase];
	//_inputbuf=new T[_testcase_num*_width*_height];
	//1�e�X�g�P�[�X�͉��s���H fscanf���Ⴞ�߂���
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
@brief �o�͗p�֐�
Case #1: 7.000000
�����������ꍇ�͂������ǁA�Q�̐��l���o�͂���Ƃ��͂����B
�����_�扽�ʂ܂ŁA�͊֐��̈����őΉ����Ă���B
���݂����ȔC�ӂ̕�����ɂ͑Ή����Ă��Ȃ��B
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