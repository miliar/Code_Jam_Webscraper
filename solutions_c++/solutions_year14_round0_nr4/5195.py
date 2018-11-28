#include<fstream>
#include<queue>
using namespace std;

const int inf=0x7fffffff;//无穷大
const int MAXM=1000;//猪圈数
const int MAXN=100;//顾客数
int s,t;//源点、汇点
int customer[MAXN+2][MAXN+2];//N+2个节点（包括源点、汇点）之间的容量Cij
int flow[MAXN+2][MAXN+2];//节点之间的流量Fij
int i,j;//循环变量

void init(ifstream& fin){
	int M,N;//M是猪圈数目，N是顾客数目
	int num;//每个顾客的钥匙数
	int k;//第k个猪圈的钥匙
	int house[MAXM];//存储每个猪圈中猪的数目
	int last[MAXM];//存储每一个猪圈的前一个顾客的序号

	memset(last,0,sizeof(last));
	memset(customer,0,sizeof(customer));
	fin>>M>>N;
	s=0;t=N+1;//源点、汇点
	for( i=1; i<M; i++){
		fin>>house[i];//读入每个猪圈中猪的数目	
	}
	for( i=1; i<=N;i++){//构造网络流
		fin>>num;//读入每个顾客拥有的钥匙数目
		for( j=0; j<num; j++){
			fin>>k;//读入钥匙序号
			if( last[k] == 0){
				customer[s][i]+=house[k];//构造有向边的流量			
			}
			else{
				customer[last[k]][i]=inf;//构造有向边的流量		
			}
			last[k]=i;//更新猪圈的前一个顾客的序号
		}
		fin>>customer[i][t];//每个顾客到汇点的有向边，权值为顾客购买猪的数量
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