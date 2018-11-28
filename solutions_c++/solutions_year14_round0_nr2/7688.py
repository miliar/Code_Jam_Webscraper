#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>
#include<iomanip> 
using namespace std;

int main()
{
	ifstream infile("B-large.in",ios::in);
	ofstream outfile("B-large.out",ios::out);
	ofstream outfile1("num.out",ios::out);
	int case_num=0;
	char temp;
	while((temp=infile.get())!='\n')
		case_num=case_num*10+(temp-'0');
	int k=1;
	while(k<=case_num)
	{
		double C=0,F=0,X=0,frac;
		temp=infile.get();
		while(temp!='.'){
			C=C*10+(temp-'0');
			temp=infile.get();
		}
		temp=infile.get();
		frac=10.0;
		while(temp!=' '){
			C=C+double(temp-'0')/frac;
			frac*=10.0;
			temp=infile.get();
		}
		temp=infile.get();
		while(temp!='.'){
			F=F*10+(temp-'0');
			temp=infile.get();
		}
		temp=infile.get();
		frac=10.0;
		while(temp!=' '){
			F=F+double(temp-'0')/frac;
			frac*=10.0;
			temp=infile.get();
		}
		temp=infile.get();
		while(temp!='.'){
			X=X*10+(temp-'0');
			temp=infile.get();
		}
		temp=infile.get();
		frac=10.0;
		while(temp!='\n' && temp!=EOF){
			X=X+double(temp-'0')/frac;
			frac*=10.0;
			temp=infile.get();
		}
		double num=(F*X-(2.0+F)*C)/(F*C);
		outfile1<<num<<endl;
		int N_min;
		if(num<=0)
			N_min=0;
		else
		{
			if((num-floor(num))<0.0001)
				N_min=floor(num);
			else
				N_min=ceil(num);
		}
		double result=0;
		for(int i=0;i<N_min;i++)
			result+=C/(2+F*i);
		result=result+X/(2+double(N_min)*F);
		outfile<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<result<<endl;
		k++;
	}

	system("pause");
	return 0;
}
