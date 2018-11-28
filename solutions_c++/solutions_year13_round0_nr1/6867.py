#include<iostream>
#include<string>
#include<vector>

using namespace std;

struct sum
{
	int x;
	int o;
	int t;
};

int check(sum count)
{
	if((count.x+count.t)==4)
		return 1;
	else if((count.o+count.t)==4)
		return 2;
	return 0;
}

void result(int res)
{
	static int k=0;
	k++;
	cout<<"Case #"<<k<<":";
	switch (res)
	{
		case 1:
			cout<<" X won"<<endl;
			break;
		case 2:
			cout<<" O won"<<endl;
			break;
		case 3:
			cout<<" Draw"<<endl;
			break;
		case 4:
			cout<<" Game has not completed"<<endl;
	}
}
int main()
{
	vector<sum> val;
	sum tmp;
	tmp.x=0;
	tmp.o=0;
	tmp.t=0;
	int len=0;
	vector<string> row_val;
	string row;
	int flag=0;
	int dot=0;
	int res=0;	
	for(int i=0;i<4;i++)
		row_val.push_back(" ");
	for(int i=0;i<7;i++)
		val.push_back(tmp);
	cin>>len;
	for(int k=0;k<len;k++)
	{
		flag=0;
		dot=0;
		for(int h=1;h<7;h++)
				val[h] = tmp;
		for(int i=0;i<4;i++)
		{
			val[0]=tmp;
			cin>>row;
			if(flag==1)
				continue;
			for(int j=0;j<4;j++)
			{
				if(row.at(j)=='.')
				{	
					dot=1;
					continue;
				}
				if(row.at(j)=='X')
				{
					val[0].x++;
					val[j+1].x++;
					if(i==j)
						val[5].x++;
					if((3-i)==j)
						val[6].x++;
				}
				else if(row.at(j)=='T')
				{
					val[0].t++;
					val[j+1].t++;
					if(i==j)
						val[5].t++;
					if((3-i)==j)
						val[6].t++;
				}
				else if(row.at(j)=='O')
				{
					val[0].o++;
					val[j+1].o++;
					if(i==j)
						val[5].o++;
					if((3-i)==j)
						val[6].o++;
				}
			}
			res=check(val[0]);
			if(res!=0)
			{
				result(res);
				flag=1;
			}
		}
		if(flag==1)
				continue;
		for(int l=1;l<7;l++)
		{
			res=check(val[l]);
			if(res!=0)
			{
				result(res);
				flag=1;
				break;
			}
		}	
		if(flag==1)
			continue;
		if(dot==1)
			result(4);	
		else
			result(3);
	}
}
