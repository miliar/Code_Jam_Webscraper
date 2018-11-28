#include<iostream>
#include<fstream>
#include<vector>
#include<cstdlib>
using namespace std;

int addval(int, int);

int arr[10];
int main()
{
	int n,i;
	int arrlen;
	vector<string> list;
    	ifstream in_stream;
    	string line;
    	in_stream.open("inputold.in");
	int cas =1;
    	while(!in_stream.eof())
    	{

		arrlen=0;
		i=1;
        	in_stream >> line;
		n = atoi(line.c_str());
		while(1)
		{
        		arrlen=addval(i*n,arrlen);
        		if(arrlen==10)
			{
                		break;
        		}
			if(arrlen==0 && i==3)
			{
				break;
			}
			i=i+1;
		}
		if(cas!=1)
                {
		if(arrlen==0)
		{
			cout << "Case #" << cas-1 <<  ": INSOMNIA";
		}
		else
		{
			cout << "Case #" << cas-1 << ": " << i*n;
		}
		cout << endl;
		}
		cas++;
	}
	in_stream.close();
	return 0;
}

int addval(int num, int arrlen)
{
        int i,digit=0;
        int yes=0;

	while(num>0)
	{
		yes=0;
		digit=num%10;
		for(i=0;i<arrlen;i++)
        	{
                	if(arr[i]==digit)
                	yes=1;
        	}
        	if(yes!=1)
        	{
                	arr[arrlen]=digit;
			arrlen++;
        	}
		num=num/10;
	}

	return arrlen;
}
