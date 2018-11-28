#include <fstream>
using namespace std;
int lawn[100][100]={0};
int checkline(int a,int b,int n,int m)
{
	int flag1=0,flag2=0;
    for(int i=0;i<m;++i)
    	if(lawn[a][b]<lawn[a][i])
    		flag1=1;
    for(int j=0;j<n;++j)
    	if(lawn[a][b]<lawn[j][b])
    		flag2=1;
    if(flag1==1&&flag2==1)
    	return 0;
    return 1;
}

int main ()
{
	ifstream R("B-large.in");
    ofstream W("B-large.out");
    
    int t;
    R>>t;
    for (int ti=1;ti<=t;++ti)
    {
    	
    	int n,m,stat=-1;
    	R>>n>>m;
    	for(int i=0;i<n;++i)
    		for(int j=0;j<m;++j)
    		    R>>lawn[i][j];
    	for(int i=0;i<n;++i)
    	{
    		for(int j=0;j<m;++j)
    		{
    			stat=checkline(i,j,n,m);
    			if(stat==0)
    				break;
    		}
    		if(stat==0)
    			break;
    	}
    	if(stat==0)
    		W<<"Case #"<<ti<<": NO"<<endl;
    	else
    		W<<"Case #"<<ti<<": YES"<<endl;
	}
}

