#include <fstream>
#include <algorithm>
using namespace std;
int T;
int E;
int R;
int N;
int v[11];

int best;
//e��ǰʣ��������ǰ���е��ڼ�����
void search(int e,int n,int value)
{
	if(n==N+1)
	{
		//������ϣ����ء�
		best=(value>best)?value:best;
		return ;
	}
	for(int i=0;i<=e;i++)
	{
		int val=value+v[n-1]*i;
		int energy=((e-i+R)>E)?E:(e-i+R);
		search(energy,n+1,val);
	}
}

int main()
{
	
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		fin>>E>>R>>N;
		for(int i=0;i<N;i++)
		{
			fin>>v[i];
		}
		best=0;
		search(E,1,0);
		fout<<"Case #"<<t<<": "<<best<<endl;
	}


	fin.close();
	fout.close();
	return 0;
}

