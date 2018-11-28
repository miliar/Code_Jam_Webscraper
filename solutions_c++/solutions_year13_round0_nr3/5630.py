#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool ispalindrome(char a[],int start,int end)
{
	
	if(start<end)
	{
		if(a[start]==a[end])
		{ //cout<<"here";
			return ispalindrome(a,++start,--end);
			
		}
		else if(a[start]!=a[end])
		{
			return false;
		}
	//	return true;
		
	}
	else
	{
		return true;
	}

}
inline void func(char array[], int &count)
{


if(ispalindrome(array,0,strlen(array)-1))
{
unsigned int num=atoi(array);
 float root=sqrt(num);
unsigned int roota=sqrt(num);
if((root-roota)==0)
{

char temp[100];
sprintf(temp,"%d",roota);
if(ispalindrome(temp,0,strlen(temp)-1))
{
count++;


}


}


}




}
int main()
{


int count;
ifstream handle;
ofstream out;
out.open("output.txt",ios::out);
handle.open("input.in",ios::in);
char temp[200];
handle.getline(temp,200,'\n');
int test=atoi(temp);
unsigned int down,up;
char array[100];

for(int i=1;i<=test;i++)
{count=0;
handle.getline(temp,200,'\n');
down=atoi(strtok(temp," "));
up=atoi(strtok(NULL,"\0"));
//cout<<down<<"*"<<up<<endl;
for(unsigned int j=down;j<=up;j++)
{




sprintf(array,"%d",j);
func(array,count);

}

cout<<"Case #"<<i<<": "<<count<<endl;
out<<"Case #"<<i<<": "<<count<<endl;



}
handle.close();
out.close();

	return 0;
}