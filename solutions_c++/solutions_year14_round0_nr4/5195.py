#include<fstream>
#include<queue>
using namespace std;

const int inf=0x7fffffff;//�����
const int MAXM=1000;//��Ȧ��
const int MAXN=100;//�˿���
int s,t;//Դ�㡢���
int customer[MAXN+2][MAXN+2];//N+2���ڵ㣨����Դ�㡢��㣩֮�������Cij
int flow[MAXN+2][MAXN+2];//�ڵ�֮�������Fij
int i,j;//ѭ������

void init(ifstream& fin){
	int M,N;//M����Ȧ��Ŀ��N�ǹ˿���Ŀ
	int num;//ÿ���˿͵�Կ����
	int k;//��k����Ȧ��Կ��
	int house[MAXM];//�洢ÿ����Ȧ�������Ŀ
	int last[MAXM];//�洢ÿһ����Ȧ��ǰһ���˿͵����

	memset(last,0,sizeof(last));
	memset(customer,0,sizeof(customer));
	fin>>M>>N;
	s=0;t=N+1;//Դ�㡢���
	for( i=1; i<M; i++){
		fin>>house[i];//����ÿ����Ȧ�������Ŀ	
	}
	for( i=1; i<=N;i++){//����������
		fin>>num;//����ÿ���˿�ӵ�е�Կ����Ŀ
		for( j=0; j<num; j++){
			fin>>k;//����Կ�����
			if( last[k] == 0){
				customer[s][i]+=house[k];//��������ߵ�����			
			}
			else{
				customer[last[k]][i]=inf;//��������ߵ�����		
			}
			last[k]=i;//������Ȧ��ǰһ���˿͵����
		}
		fin>>customer[i][t];//ÿ���˿͵���������ߣ�ȨֵΪ�˿͹����������
	}
}

void ford(){
	int pre[MAXN+2];
	bool vis[MAXN+2];
	queue<int> que;
	memset(pre,-1,sizeof(pre));
	memset(vis,false,sizeof(vis));
	pre[0]=0;
	vis[0]=true;
	que.push(s);
	int p;
	while(1){
		p=que.front();
		que.pop();
		for( i=0; i<MAXN+2; i++){
			if( customer[p][i]>0 ){
			
			
			}
		
		}
	}




}