#include<fstream.h>
#include<math.h>
int convert(char x)
{
	if(x=='1')
		return (1);
	else if(x=='2')
		return (2);
	else if(x=='3')
		return (3);
	else if(x=='4')
		return (4);
	else if(x=='5')
		return (5);
	else if(x=='6')
		return (6);
	else if(x=='7')
		return (7);
	else if(x=='8')
		return (8);
	else if(x=='9')
		return (9);
	else if(x=='0')
		return (0);
}
void main()
{
	ifstream infile("large.in");
	ofstream onfile("output.txt",ios::trunc);
	int n;
	infile>>n;
	for(int i=0;i<n;i++)
	{
		int smax;
		char a[1010];
		infile>>smax;
		infile>>a;
		int std=0,frnd=0;
		for(int j=0;j<=smax;j++)
		{
			if(std>=j)
				std+=convert(a[j]);
			else
			{
				frnd+=(j-std);
				std=j+convert(a[j]);
			}
		}
	cout<<"Case #"<<i+1<<": "<<frnd<<endl;
	onfile<<"Case #"<<i+1<<": "<<frnd<<endl;
	}

}
