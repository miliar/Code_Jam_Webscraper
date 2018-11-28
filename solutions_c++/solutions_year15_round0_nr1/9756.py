# include<fstream.h>
#include<iostream.h>
#include<conio.h>
int mn,z,i,y,j,p[10],add[10],s,sum,f,lmt;
char c[10];
ifstream fin;
ofstream fout;

void main()
{	clrscr();
	 fin.open("r.in");
	 fout.open("s.txt");
	 fin>>mn;
	 for(z=1;z<=mn;z++)
	 {
	 fin>>lmt;
	 s=0;
//	 cout<<lmt<<"lmt\n";//
	 f=0;
	 fin>>c;
	 for(i=0;i<=lmt;i++)
	 {
		p[i]=c[i]-48;
  //		cout<<"array :"<<p[i]<<" ";       //
	 }
	 for(int l=0;l<10;l++)
	 add[l]=0;
	 for(y=1;y<=lmt;y++)
	 {
		sum=0;
//		cout<<"y"<<y;
		for(j=0;j<y;j++)
		{
			sum=sum+p[j]+add[j];
    //			cout<<"\nsum: "<<j<<" "<<sum<<"\n"; //
		}

		if(y>sum)
		{
		add[y]=y-sum;
		s=s+add[y];
		}
		/*for(int k=0;k<lmt;k++)
		cout<<"add: "<<add<"\n";//
		if(add>=0)
		{
			f=f+add;
		}
		*/
	 }
	 fout<<"Case #"<<z<<": "<<s<<"\n";
      //	 cout<<"\n frnd:"<<s;//
	 }
}
