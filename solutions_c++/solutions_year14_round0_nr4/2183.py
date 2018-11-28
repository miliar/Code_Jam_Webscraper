#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
	clrscr();
	ifstream fin;
	ofstream fout;
	fout.open("warwarwar.txt",ios::out);
	fin.open("war.in",ios::in);
	int cases,blocks;
	fin>>cases;
	float *a,*b;
	int x=0;
	while(cases>0)
	{
		x++;
		fin>>blocks;
		a=new float[blocks];
		b=new float[blocks];
		for(int i=0;i<blocks;i++)
			fin>>a[i];
		for(i=0;i<blocks;i++)
			fin>>b[i];

		float temp;
		for(int j=0;j<blocks-1;j++)
			for(i=0;i<blocks-j-1;i++)
			{
				if(a[i]>a[i+1])
				{
					temp=a[i];
					a[i]=a[i+1];
					a[i+1]=temp;
				}

				if(b[i]>b[i+1])
				{
					temp=b[i];
					b[i]=b[i+1];
					b[i+1]=temp;
				}
			}

			int start=0,ken=0,n=0;
			for(i=0;i<blocks;i++)
			for(j=start;j<blocks;j++)
				if(b[i]>a[j])
				{
					ken++;
					start=j+1;
					break;
				}
			start=0;
			for(i=0;i<blocks;i++)
			for(j=start;j<blocks;j++)
				if(a[i]>b[j])
				{
					n++;
					start=j+1;
					break;
				}
		delete a;
		delete b;
			fout<<"Case #"<<x<<": "<<n<<" "<<blocks-ken<<endl;
			cout<<"Case #"<<x<<": "<<n<<" "<<blocks-ken<<endl;
	cases--;
	}
	getch();
}




