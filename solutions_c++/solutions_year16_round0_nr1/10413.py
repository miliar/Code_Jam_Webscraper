#include<iostream>
#include<fstream>
#include<algorithm>
#include<set>
using namespace std;
set<int> s1;
void splitdig(int n,int count,ofstream &output)
{
	long long int tem = n;
	long long int flag = false,i=1;
	while(!flag){
//	cout<<tem<<endl;
	long int long dis = n;
	while(n>0)
	{
		s1.insert(n%10);
		if(s1.size() == 10)
		{
			output<<"Case #"<<count+1<<": "<<dis<<"\n";
			flag = true;
			break;	
		}
		n = n/10;
	}
	n = tem *(i+1);
	i++;
}
	
}
int main(int argc , char *argv[])
{
ifstream input(argv[1]);
ofstream output(argv[2]);
long long int test_number=0;
input>>test_number;
for(int count=0;count<test_number;count++)
{
long long int val = 0;
input>>val;
if(val){
	splitdig(val,count,output);
}
else
	output<<"Case #"<<count+1<<": "<<"INSOMNIA\n";
	s1.clear();
	
}

}
