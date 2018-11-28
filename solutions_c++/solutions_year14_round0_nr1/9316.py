#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int mat1[4][4]={{0}};
	int mat2[4][4]={{0}};
	vector<int> result;
	int T=0;
	cin>>T;
	int temT=T;
	int ans1=0,ans2=0;
	int count=0,temValue=0;
	while(temT)
	{
		cin>>ans1;
		cin>>mat1[0][0]>>mat1[0][1]>>mat1[0][2]>>mat1[0][3];
		cin>>mat1[1][0]>>mat1[1][1]>>mat1[1][2]>>mat1[1][3];
		cin>>mat1[2][0]>>mat1[2][1]>>mat1[2][2]>>mat1[2][3];
		cin>>mat1[3][0]>>mat1[3][1]>>mat1[3][2]>>mat1[3][3];
		cin>>ans2;
		cin>>mat2[0][0]>>mat2[0][1]>>mat2[0][2]>>mat2[0][3];
		cin>>mat2[1][0]>>mat2[1][1]>>mat2[1][2]>>mat2[1][3];
		cin>>mat2[2][0]>>mat2[2][1]>>mat2[2][2]>>mat2[2][3];
		cin>>mat2[3][0]>>mat2[3][1]>>mat2[3][2]>>mat2[3][3];
		count=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(mat1[ans1-1][i]==mat2[ans2-1][j])
				{
					count++;
					temValue=mat1[ans1-1][i];
				}
			}
		}
		if(count==1) result.push_back(temValue);
		else if(count>1) result.push_back(-1);	//bad
		else if(count==0) result.push_back(-2);//cheated
		temT--;
	}

	int i=0;
	for(vector<int> ::iterator p=result.begin();p!=result.end();p++)
	{
		i++;
		if((*p)>0) cout<<"Case #"<<i<<": "<<(*p)<<endl;
		else if((*p)>=-1) cout<<"Case #"<<i<<": Bad magician!"<<endl;
		else if((*p)>=-2) cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
	}

	return 0;
}