#include<iostream>
using namespace std;
const int SIZE = 10;
int sizeW,sizeH;
int caseNumber;
int map[SIZE][SIZE];
bool findAns;
bool check(int i,int j)
{
  //up | down
  int t1,t2,t3,t4;
  t1 = j>0? j-1:0;
  t2 = j<(sizeH-1)? j+1:sizeH-1;
  t3 = i>0? i-1:0;
  t4 = i<(sizeW-1)? i+1:sizeW-1;
  int ans = map[i][j];	
 // printf("i=%d j=%d (t1,t2)=(%d,%d) (t3,t4)=(%d,%d)\n",i,j,t1,t2,t3,t4);
  if( ans < map[i][t1] || ans < map[i][t2])
  {
  //	printf("1\n");
	//check horizatal
	for(int k = 0;k<sizeW;k++)
		if(map[k][j]>ans)
			return false;
  }
  else if(ans < map[t3][j] || ans < map[t4][j])
  {
   //check vertical
	for(int k = 0;k<sizeH;k++)
		if(map[i][k]>ans)
			return false;
  }
  bool a,b;
  a = b =false;
  if(i==0 || j==0 || j==(sizeH-1) ||i==(sizeW-1)){
	for(int k=0;k<sizeW;k++)
		if(map[k][j]>ans)
		{
			a= true;
			break;
		}
	for(int k=0;k<sizeH;k++)
		if(map[i][k]>ans)
		{
			b = true;
			break;
		}
  }
  if(a&b)
  	return false;
  return true;
}

int main()
{
	cin>>caseNumber;
	for(int i=0;i<caseNumber;i++)
	{
		cin>>sizeW>>sizeH;
		findAns = true;
		for(int j=0;j<sizeW;j++)
			for(int k=0;k<sizeH;k++)
				cin>>map[j][k];
		for(int j=0;j<sizeW;j++)
		{
			for(int k=0;k<sizeH;k++)
			{
				if(check(j,k)==false)
				{
					printf("Case #%d: NO\n",i+1);
					findAns = false;			
					break;
				}
			}
			if(!findAns)
				break;
		}	
		if(findAns)	
		printf("Case #%d: YES\n",i+1);
	}


}
