#include<fstream.h>
#include<iomanip.h>
void main()
{       ifstream fin;
	ofstream fout;
	fout.open("out.txt") ;
	int T,k,flag;
	double c,f,x,t,t1,t2,p;

  fin.open ("in.txt");
		fin>>T;

		for( k=1; k<=T; k++)
		{   p=2.0;
			 t=0.0;
			 flag=0;
			 t1=0.0;
			 t2=0.0;
			 fout<<"Case #"<<k<<": ";
			 fin>>c;
			 fin>>f;
			 fin>>x;
			 while(flag==0)
		{	 t1=t+(x/p);
			 t2=t+(c/p)+(x/(p+f));
			 if(t1<=t2)
			 {
			 fout<<setiosflags(ios::fixed | ios::showpoint)<< setprecision(7)<<t1<<endl;
			 flag=1;}
			 else
			 {t=t+(c/p);
			 p=p+f;   }
		}

		}
  fin.close();
  fout.close();
}