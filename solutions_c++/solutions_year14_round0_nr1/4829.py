#include<iostream>
#include<fstream>
using namespace std;


int rep_num(int *a,int *b,int & x);
int main()
{
	ifstream in;
	ofstream out;
	
	in.open("A-small-attempt0.in");		
	out.open("A-small-attempt0.op");
	int num_l,v_ans;
	int a[4][4];
	in>>num_l;
	int ch1[4];
	int ch2[4];
	
	for(int i=0;i<num_l;i++)
	{
		int card;
		in>>v_ans;
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				in>>a[i][j];

		for(int k=0;k<4;k++)
				ch1[k]=a[v_ans-1][k];

			
			
			in>>v_ans;
			
		for(int l=0;l<4;l++)
			for(int m=0;m<4;m++)		
				in>>a[l][m];				
								
		
		for(int i=0;i<4;i++)
			ch2[i]=a[v_ans-1][i];
			
			
			
	if( rep_num(ch1,ch2,card)==1)
			{
				out<<"Case #"<<i+1<<": "<<card<<endl;	
			}
			if(rep_num(ch1,ch2,card)>1)
			{
				out<<"Case #"<<i+1<<": Bad magician!"<<endl;	
			}
			if(rep_num(ch1,ch2,card)==0)
			{
				out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;	
			}
	}
	
	
	return 0;
}
int rep_num(int *a,int *b,int & x)
{
	int sum=0;

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(a[i]==b[j] )
			{
				sum++;
				x=a[i];
				break;
				
			}
		
		}
				
	}
	
	return sum;
}