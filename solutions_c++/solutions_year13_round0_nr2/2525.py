#include <fstream>
using namespace std;
int T,N,M;
int lawn[100][100];
int flag[100][100];
//�ж�һ�����Ƿ�OK
bool isOk(int n,int m)
{
	//0Ϊ��Ok��1ΪOk
	bool state=true;
	//�����ж��ԡ�
	for(int j=0;j<M;j++)
	{
		if(lawn[n][j]>lawn[n][m])
		{
			state=false;
			break;
		}
	}
	//���ж��ԡ�
	if(state==false)
	{
		state=true;
		for(int i=0;i<N;i++)
		{
			if(lawn[i][m]>lawn[n][m])
			{
				state=false;
				break;
			}
		}
	}
	return state;
}

//�ж������Ƿ�OK
bool isValid()
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			if(!isOk(i,j))
				return false;
		}
	}
	return true;
}
int main()
{
	/*ifstream fin("B-small-attempt2.in");
	ofstream fout("B-small-attempt2.out");*/
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		fin>>N>>M;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				fin>>lawn[i][j];
				flag[i][j]=0;
			}
		}
		bool state;
		if(M==1||N==1) state=true;
		else state=isValid();
		if(state) fout<<"Case #"<<t<<": YES"<<endl;
		else fout<<"Case #"<<t<<": NO"<<endl;

	}
	fin.close();
	fout.close();
	return 0;
}

