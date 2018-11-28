#include <iostream>
#include <fstream>
using namespace std;
void sort(char ** arr,int size)
{
	char x[100];
	int i=0;
	for (i=0;i<size-1;i++)
	{
		for(int j=i;j<size;j++)
			if(strlen (arr[i])>strlen(arr[j]))
			{
				strcpy(x,arr[i]);
				strcpy(arr[i],arr[j]);
				strcpy(arr[j],x);
			}
	}
}

int main()
{
	int size,N;
	int flips;
	int index1,index2;
	int * no;
	int center;
	int ctcount,crcount;
	bool flag=true;
	char croldchar, crnewchar,ctoldchar, ctnewchar;
	ifstream fin("A-small-attempt1.in");
	ofstream fout("output.txt");
	fin>>size;
	for(int i=0;i<size;i++)
	{	
		flips=0;
		fin>>N;
		char ** strs=new char*[N];
		for(int j=0;j<N;j++)
			strs[j]= new char[100];
		//index=new int [N];
		no=new int[N];
		center=N/2;

		for (int j=0;j<N;j++)
		{
			fin>>strs[j];
		}
		sort(strs,N);
		for (int j=0;j<N;j++)
		{
			
			ctcount=crcount=0;
			index1=index2=0;
			flag=true;
			while(true)
			{	
				croldchar=strs[j][index1];ctoldchar=strs[center][index2];
				if(croldchar!=ctoldchar)
				{
					flag=false;
					break;
				}
				ctcount=0;
				crcount=0;
				while(true)
				{
					ctnewchar=strs[center][index2];
					crnewchar=strs[j][index1];
					if(ctnewchar==ctoldchar&&ctnewchar!=0)
					{
						index2++;
						ctcount++;
					}
					if(croldchar==crnewchar&&crnewchar!=0)
					{
						index1++;
						crcount++;
					}
					if((croldchar!=crnewchar)&&(ctoldchar!=ctnewchar))
					{
						break;
					}
				}
				flips+=abs(crcount-ctcount);
				if(ctnewchar==0&&crnewchar==0)
					break;
			}
			if (flag==false)
				break;
		}
		if(flag)
		fout<<"Case #"<<i+1<<": "<<flips<<endl;
		else fout<<"Case #"<<i+1<<": Fegla Won"<<endl;
	
	}
	fin.close();
	fout.close();
	return 0;
	
}