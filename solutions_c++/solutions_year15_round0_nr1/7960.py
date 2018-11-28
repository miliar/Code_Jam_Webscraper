#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int chartoInt(string temp)
{
	char *num= new char [temp.size()+1];
				copy(temp.begin(),temp.end(),num);
				num[temp.size()]='\0';
				int number=atoi(num);
				delete [] num;
				num=0;
		return number;
}

void parse()
{
		//////////////////////////////////////////////////
	ifstream ifile; 
	ofstream ofile;
	ofile.open("output.txt");
	if(ofile.fail())
	{

		cout<<"output failed\n";
	}
	ifile.open("1234.in");
	if(ifile.fail())
	cout<<"File Not Found :( ";
	else
	{
		string data;
		
		bool first=0;

		int CASE=0;

		while( getline (ifile,data))
		{
			if(!first)
				first=1;
			else{

		string temp;
		char* A=new char [data.size()+1];
		copy(data.begin(),data.end(),A);
		A[data.size()]='\0';
		char *token;
		int count=0;
		token= strtok(A,", ");


///////////////////////////////////////////////////

		int level=0;
		
		int * members=nullptr;

		while(token!=NULL)
		{
			temp=token;
			
			if(count==0)
			{
				level = chartoInt(temp);

			}
			else if(count==1)
			{
				members = new int [level+1];
				for(int y=0;y<level+1;++y)
					members[y]=0;
				for(int i=0;i<level+1;++i)
				{

					members[i]= temp[i]-48;
			//		cout<<members[i]<< ' ';

				}

		//		cout<<endl;

			}


			token=strtok(NULL," ");
			count++;
		}
		delete [] A;
		A=0;


		int index=0,needed=0,sum=0;

		for(;index<=level;++index)
		{

			
			if(index>sum)
			{

				int x = index-sum;
				sum+=x;
				needed+=x;

			}
			sum += members[index];
		}

		
		ofile<<"Case #"<<++CASE<<": "<<needed<<endl;
		
		if(members!=nullptr)
			delete [] members;

		}
		}

		ifile.close();
		ofile.close();
	}


}




int main()
{

			parse();
			system("pause");
}