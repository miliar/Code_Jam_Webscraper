#include <iostream>


#include<fstream>

using namespace std;

int main()

{


	char s[10000];

	int ne[10000],i,re[10000];

	int smax,no,count,count1,t;

	cin>>t;

	for(int j=0;j<t;j++)

	{

		cin>>smax;
	
	int max=smax+1;
	
	for(i=0;i<max;i++)

			cin>>s[i];

		for(i=0;i<=smax;i++)

		{

			if(s[i]==49)

				ne[i]=1;
	
		if(s[i]==50)

				ne[i]=2;
	
		if(s[i]==51)
	
			ne[i]=3;

			if(s[i]==52)

				ne[i]=4;
	
		if(s[i]==53)

				ne[i]=5;
	
		if(s[i]==54)

				ne[i]=6;

			if(s[i]==55)

				ne[i]=7;

			if(s[i]==56)
	
			ne[i]=8;
	
		if(s[i]==57)

				ne[i]=9;
	
		if(s[i]==48)

				ne[i]=0;

		}

		if(smax>0)
	
	{

			no=ne[0];

			count=0;

			for(i=1;i<=smax;i++)

			{

				if(i<=no)

				{
	
					no=no+ne[i];

				}

				else

				{

					if(s[i]==0)

						continue;

					count1=i-no;

					count+=count1;

					no=no+count1;
	
				no=no+ne[i];
	
			}


			}
	
		re[j]=count;
	
	
}

		else
	
	    re[j]=0;

	}

	ofstream Myfile;
	Myfile.open("output.txt");
	for(i=0;i<t;i++)
	{

	    Myfile<<"Case #"<<i+1<<": "<<re[i]<<endl;

	}

	Myfile.close();
	return 0;

}

