#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <map>
#include <string>

using namespace std;

// ����ʒux�̗��ʂɂ���p���P�[�L��\�ɂ���̂ɕK�v�ȑ���́A
// 1. �ŏ㕔�̃P�[�L���\�Ȃ痠�Ԃ�
// 2. x�܂ł��܂Ƃ߂ė��Ԃ�
// �Ȃ̂�1��2�X�e�b�v�B�P�[�L�����̍ő�l��100�Ȃ̂ōő�200�X�e�b�v�ȓ��ɂ͏I���
// �ċA�ŒT������ƃX�^�b�N����ʂ�200*101�A��������20kB

// �����Ԃ���I�ǂ܂ł̃X�e�b�v�������������ĒT���������点�΂�������

// �ؖ��͎v�����Ȃ����A���̂ق��̘A�����Ă���\�����p���P�[�L�ɂ͐G��Ȃ��ł��ŒZ�o�H�͕ς��Ȃ��Ƒz��

map<string,int> cost_to_goal;
map<string,int> cost_from_start;

void flip(char *dest,char *src, int N)
{
	strcpy(dest,src);
	for (int i=0;i<N;i++){
		if (src[N-1-i]=='+'){
			dest[i]='-';
		}
		else if (src[N-1-i]=='-'){
			dest[i]='+';
		}
		else assert(0);
	}
	//strcpy(dest+N,src+N);
	//printf("%d %s -> %s\n",N,src,dest);
}

int states = 0;
int max_step = 0;

int search(char *S, int len, int step, int limit)
{
	states++;
	if (step>max_step)max_step=step;
	if (step > limit) return -1;
	//printf("%s %d %d\n",S,len,step);
	// �S���\�Ȃ�I��
	if (len == 0)return 0;
	assert(S[len-1]=='-');
	string key(S);
	// �����ƈ����R�X�g�ŗ�����Ȃ炻��ȏ�̒T�����s���K�v�͂Ȃ�
	if (cost_from_start.find(key)!=cost_from_start.end()){
		if (cost_from_start[key]<=step)
			return -1;
	}
	/*if (cost_to_goal.find(key)!=cost_to_goal.end()){
		// �������ΏۂɈ������������̂Ȃ�I��
		return cost_to_goal[key];
	}*/
	cost_from_start[key]=step;
	// len�܂ł̔��]�����S������
	int min_ret = -1;
	len = strlen(S);
	for (int i=1;i<=len;i++){
		char S_[101];
		int len_=len;
		flip(S_,S,i);
		while (len_>0){
			char c = S_[len_-1];
			if (c=='-')break;
			else if (c=='+'){
				len_--;
			}
			else assert(0);
		}
		// �ċA����
		int ret = search(S_,len_,step+1,limit);
		if (ret >= 0){
			if (min_ret < 0 || ret < min_ret){
				min_ret = ret;
			}
		}
	}
	//assert(cost_to_goal.find(key)==cost_to_goal.end());
	if (min_ret<0)return -1;
	cost_to_goal[key]=min_ret+1;
	return min_ret + 1;
}

int main(int argc,char **argv)
{
	int T;
	scanf("%d\n",&T);
	for (int t=1;t<=T;t++){
		char S[101];
		scanf("%s\n",S);
		int len = strlen(S);
		cost_to_goal.clear();
		cost_from_start.clear();
		//printf("%s\n",S);
		while (len>0){
			char c = S[len-1];
			if (c=='-')break;
			else if (c=='+'){
				len--;
			}
			else assert(0);
		}
		states = 0; max_step = 0;
		printf("Case #%d: %d\n",t,search(S,len,0,strlen(S)*2));
		// printf("states = %d, max_step = %d\n",states,max_step);
	}
	return 0;
}
