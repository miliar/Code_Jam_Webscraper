#include <iostream>
#include <map>
#include <fstream>

using namespace std;
inline bool ispal(int a)
{
	int temp1 = a, temp2[4]={-1}, i= 0;
	while ( temp1 != 0)
	{
		temp2[i++]= temp1 % 10;
		temp1 /= 10;

	}
	int j = 0, k= i-1;
	for (j, k; j < i; j++,k--)
		if(temp2[k] != temp2[j])
		{
			return	false;
		}
	return true;	
	 
}

int main()
{
	map <int, int>list;
	map <int,int>::iterator it;

	int cases=0;
	int count =0;
	for(int i = 1; i <= 31;i ++)
		list[i*i]=i;
	fstream file("C-small-attempt0.in",ios::in);
	if (!file)
		exit(0);
	else
	{
		file>>cases;
		int i=0, j;
		int Rstart=0,Rend=0;
		for (i;i < cases; i++)
		{
			file>>Rstart>>Rend;
			count =0;
			for (j = Rstart; j <= Rend; j++)
			{
				if (ispal(j))
				{
					it = list.find(j);
					if (it != list.end())
						if( ispal(list.find(j)->second) )
						{
							count++;
						}
				}
				
			}
			fstream outfile("ProblemC_results.txt",ios :: out | ios :: app);
			if (!file)
				exit(0);
			else
			{
				outfile<<"Case #"<<i+1<<": "<<count<<endl;
			}
			outfile.close();
		}
		
	}
	system("Pause");
	return 0;
}