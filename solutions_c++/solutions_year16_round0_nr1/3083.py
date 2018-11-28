#include<iostream>
using namespace std;
void Sheep_Count()
{
int num,i,j,temp,flag_done[10],mult = 1;
cin>>num;
for(i=0;i<10;i++)
{
	flag_done[i] = 0;
}
for(j=1;j<=500;j++)
{
	temp = j*num;
	for(i=0;i<9;i++)
	{
		flag_done[temp%10] = 1;
		temp = temp/10;
		if(temp == 0)
			break;
	}
	for(i=0;i<10;i++)
	{
		if(flag_done[i] == 0)
			break;
	}
	if(i == 10)
		break;
}
if (j == 501)
	cout<<"INSOMNIA";
else 
	cout<<j*num;

}
int main()
{
int number;
cin>>number;
for(int i=0;i<number;i++)
{
	cout<<"Case #"<<i+1<<": ";
	Sheep_Count();
	if(i != (number-1))
		cout<<endl;
}
return 0;
}
