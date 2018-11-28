#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	ifstream infile("A-small-attempt5.in",ios::in);
	ofstream outfile("A-small-attempt5.out",ios::out);
	int case_num=0;
	char temp;
	while((temp=infile.get())!='\n')
		case_num=case_num*10+(temp-'0');
	int k=1;
	while(k<=case_num)
	{
		int row1=0;
		while((temp=infile.get())!='\n')
			row1=row1*10+(temp-'0');
		for(int i=1;i<row1;i++)
			while((temp=infile.get())!='\n');
		int r1[4]={0};
		for (int j=0;j<4;j++){
			temp=infile.get();
			while(temp!='\n' && temp!=' '){
				r1[j]=r1[j]*10+(temp-'0');
				temp=infile.get();
			}
		}
		for(int k=row1;k<4;k++)
			while((temp=infile.get())!='\n');
		int row2=0;
		while((temp=infile.get())!='\n')
			row2=row2*10+(temp-'0');
		for(int i=1;i<row2;i++)
			while((temp=infile.get())!='\n');
		int r2[4]={0};
		for (int j=0;j<4;j++){
			temp=infile.get();
			while(temp!='\n' && temp!=' ' && temp!=EOF){
				r2[j]=r2[j]*10+(temp-'0');
				temp=infile.get();
			}
		}
		for(int k=row2;k<4;k++){
			temp=infile.get();
			while(temp!='\n' && temp!=EOF){temp=infile.get();}
		}
		int same=0,same_num;
		for(int l=0;l<4;l++){
			for(int m=0;m<4;m++){
				if(r1[l]==r2[m]){
					same++;
					same_num=r1[l];
				}
			}
		}
		if(same==0)
			outfile<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		else{
			if(same==1)
				outfile<<"Case #"<<k<<": "<<same_num<<endl;
			else
				outfile<<"Case #"<<k<<": Bad magician!"<<endl;
		}
		k++;
	}

	system("pause");
	return 0;
}
