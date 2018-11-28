#include<iostream>
using namespace std;

int Check(int** t)
{
	int sum[4] = {0};
	int sum1;
 	for(int i = 0;i<4;i++)//行检查
	{
		sum[i] = t[i][0]+t[i][1]+t[i][2]+t[i][3];
		if(sum[i] == 3 || sum[i] == 4 || sum[i] == -4 || sum[i] == -3)
				return sum[i];
	}
 	for(int j = 0;j<4;j++)//列检查
	{
		sum1 = t[0][j]+t[1][j]+t[2][j]+t[3][j];
		if(sum1 == 3 || sum1 == 4 || sum1 == -4 || sum1 == -3)
				return sum1;
	}
	sum1 = t[0][0]+t[1][1]+t[2][2]+t[3][3];//对角线1
	if(sum1 == 3 || sum1 == 4 || sum1 == -4 || sum1 == -3)
		return sum1;
	sum1 = t[3][0]+t[2][1]+t[1][2]+t[0][3];//对角线2
	if(sum1 == 3 || sum1 == 4 || sum1 == -4 || sum1 == -3)
		return sum1;
	else return sum[0]+sum[1]+sum[2]+sum[3];
}

int main()
{
	int n;
	cin>>n;
	for(int num = 0;num<n;num++)
	{
	int ** ttt = new int*[4];
	for(int i = 0;i<4;i++)
	{
		ttt[i] = new int[4];
	}
	char temp;
	for(int i = 0;i<4;i++)
		for(int j =0; j<4;j++)
		{
			cin>>temp;
			if(temp == 'X')
				ttt[i][j] = 1;
			if(temp == 'O')
				ttt[i][j] = -1;
			if(temp == '.')
				ttt[i][j] = 10;
			if(temp == 'T')
				ttt[i][j] = 0;
		}
	//初始化结束
    int sum = Check(ttt);
	if(sum == 3 || sum == 4 )
		cout<<"case #"<<(num+1)<<":X won"<<endl;
	else if(sum == -3 || sum == -4 )
		cout<<"case #"<<(num+1)<<":O won"<<endl;
		else if(sum<5)
		cout<<"case #"<<(num+1)<<":Draw"<<endl;
			else cout<<"case #"<<(num+1)<<":Game has not completed"<<endl;
	}
}