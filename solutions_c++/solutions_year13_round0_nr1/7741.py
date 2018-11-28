#include <iostream>
#include <string>
using namespace std;

string rows_check(char arr[16])
{
	for(int i=0;i<16;i+=4)
	{
		if( arr[i]=='X' && arr[i+1]=='X' && arr[i+2]=='X' &&arr[i+3]=='T')
			return "X";
		if( arr[i]=='T' && arr[i+1]=='X' && arr[i+2]=='X' &&arr[i+3]=='X')
			return "X";
		if( arr[i]=='X' && arr[i+1]=='X' && arr[i+2]=='X' &&arr[i+3]=='X')
			return "X";

		if( arr[i]=='O' && arr[i+1]=='O' && arr[i+2]=='O' &&arr[i+3]=='T')
			return "O";
		if( arr[i]=='T' && arr[i+1]=='O' && arr[i+2]=='O' &&arr[i+3]=='O')
			return "O";
		if( arr[i]=='O' && arr[i+1]=='O' && arr[i+2]=='O' &&arr[i+3]=='O')
			return "O";

	}
	return "D";
}


string columns_check(char arr[16])
{
	for(int i=0;i<4;i++)
	{
		if( arr[i]=='X' && arr[i+4]=='X' && arr[i+8]=='X' &&arr[i+12]=='T')
			return "X";
		if( arr[i]=='T' && arr[i+4]=='X' && arr[i+8]=='X' &&arr[i+12]=='X')
			return "X";
		if( arr[i]=='X' && arr[i+4]=='X' && arr[i+8]=='X' &&arr[i+12]=='X')
			return "X";

		if( arr[i]=='O' && arr[i+4]=='O' && arr[i+8]=='O' &&arr[i+12]=='T')
			return "O";
		if( arr[i]=='T' && arr[i+4]=='O' && arr[i+8]=='O' &&arr[i+12]=='O')
			return "O";
		if( arr[i]=='O' && arr[i+4]=='O' && arr[i+8]=='O' &&arr[i+12]=='O')
			return "O";

	}
	return "D";
}


string diognal_check(char arr[16])
{

	if(arr[0]=='X'&&arr[5]=='X'&&arr[10]=='X'&&arr[15]=='T')
		return "X";
	if(arr[0]=='T'&&arr[5]=='X'&&arr[10]=='X'&&arr[15]=='X')
		return "X";
	if(arr[0]=='X'&&arr[5]=='X'&&arr[10]=='X'&&arr[15]=='X')
		return "X";

	if(arr[3]=='X'&&arr[6]=='X'&&arr[9]=='X'&&arr[12]=='T')
		return "X";
	if(arr[3]=='T'&&arr[6]=='X'&&arr[9]=='X'&&arr[12]=='X')
		return "X";
	if(arr[3]=='X'&&arr[6]=='X'&&arr[9]=='X'&&arr[12]=='X')
		return "X";



	if(arr[0]=='O'&&arr[5]=='O'&&arr[10]=='O'&&arr[15]=='T')
		return "O";
	if(arr[0]=='T'&&arr[5]=='O'&&arr[10]=='O'&&arr[15]=='O')
		return "O";
	if(arr[0]=='O'&&arr[5]=='O'&&arr[10]=='O'&&arr[15]=='O')
		return "O";

	if(arr[3]=='O'&&arr[6]=='O'&&arr[9]=='O'&&arr[12]=='T')
		return "O";
	if(arr[3]=='T'&&arr[6]=='O'&&arr[9]=='O'&&arr[12]=='O')
		return "O";
	if(arr[3]=='O'&&arr[6]=='O'&&arr[9]=='O'&&arr[12]=='O')
		return "O";
	return "D";
}


int main()
{
	char arr[16];
	int testcases;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	string result1,result2,result3;
		cin>>testcases;
	
	for(int i=1;i<=testcases;i++)
	{
		bool draw=false;
		bool space=false;
		for(int j=0;j<16;j++)
		{
			cin>>arr[j];
			if(arr[j]=='.')
				space =true;
		}
		getchar();
		getchar();

		result1=rows_check(arr);
		result2=columns_check(arr);
		result3=diognal_check(arr);
		cout<<"Case #"<<i<<": ";
		if(result1=="D"&&result2=="D"&&result3=="D")
		{
			if(space)
				cout<<"Game has not completed"<<endl;
			else
			cout<<"Draw"<<endl;
		}
		else if (result1=="X"||result2=="X"||result3=="X")
			cout<<"X won"<<endl;
		else if (result1=="O"||result2=="O"||result3=="O")
			cout<<"O won"<<endl;
	}
	return 0;
}