#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
#include<algorithm>
#include<set>
#include<deque>
#include<map>
#include<math.h>
using namespace std;

#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 

	//cout.txt file using c library
	//FILE* fp=fopen("C:\\Programming_VS2010\\InterviewStreet\\InsertionSort\\cout.txt","w");
#endif

	int run = 0;
	cin>>run;
	int cs = 1;

	int *OldMc=NULL;
	int *NewMc=NULL;
	int count=0;

	bool itrFlg = false;
	while(run--)
	{
		int c1=0;
		int c2=0;
		int k=0;
		int i=0,j=0;

		cin>>c1;
		cin>>c2;
		c1;
		c2;
		cin>>k;
		
		if(itrFlg)
		{
			//OldMc=NULL;
			//NewMc=NULL;
			count=0;
			cout<<endl;
			//fprintf(fp,"\n");
		}
		itrFlg = true;
		/*
		OldMc=(int*)malloc(c1*(sizeof(int)));
		NewMc=(int*)malloc(c2*(sizeof(int)));

		for(i=0;i<c1;i++)
			OldMc[i]=i;

		for(i=0;i<c2;i++)
			NewMc[i]=i;
		*/
		int res=0;
		for(i=0;i<c1;i++)
		{
			for(j=0;j<c2;j++)
			{
				//res=OldMc[i] & NewMc[j];
				res=i&j;
				//cout<<res<<" ";
				if(res<k)
					count++;
			}
		}

		//free(OldMc);
		//free(NewMc);

		cout<<"Case #"<<cs<<": "<<count;
		cs++;
		
	}

	return 0;
}