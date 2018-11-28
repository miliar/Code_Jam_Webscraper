#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("C:\\Users\\DeepakG\\Desktop\\input.txt");
	ofstream fout;
	fout.open("C:\\Users\\DeepakG\\Desktop\\output.txt");
	int t,t1=0,n,cnt,fr;
	char *arr;
	fin>>t;
	while(t1<t)
	{
		fin>>n;
		fr=0;
		arr = new char[n+1];
		fin>>arr;
		cnt=(int)arr[0]-48;
		for(int i=1;i<=n;i++)
		{
			if((int)arr[i]==48)continue;
			if(i<=cnt){cnt+=(int)arr[i]-48;continue;}
			fr+=(i-cnt);
			cnt+=fr;
			cnt+=((int)arr[i]-48);
		}
		fout<<"Case #"<<t1+1<<": "<<fr<<"\n";
		t1++;
	}


return 0;
}

