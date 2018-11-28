#include<fstream.h>
 void main()
 {      ifstream fin;
	ofstream fout;
	fout.open("out.txt") ;
	int T,y,i,j,k;
	int A[4][4],B[4][4],a,b,f;

  fin.open ("in.txt");
		fin>>T;
		for( k=1; k<=T; k++)
		{
			 fout<<"Case #"<<k<<": ";
			  fin>>a;
			  for(i=0;i<4;i++)
			  {
					for(j=0;j<4;j++)
					{fin>>A[i][j];}
			  }
			  fin>>b;
			  for(i=0;i<4;i++)
			  {
					for(j=0;j<4;j++)
					{fin>>B[i][j];}
			  }
				f=0;
			  for(i=0;i<4;i++)
			  {
					for(j=0;j<4;j++)
					{
						if(A[a-1][i]==B[b-1][j])
						{
							f++;
							y=B[b-1][j];
						}
					}
			  }
			  if(f==0)
			  {fout<<"Volunteer cheated!"<<endl;}
			 else if(f==1)
			  {fout<<y<<endl;}
			 else if(f>1)
			  {fout<<"Bad magician!"<<endl;}



		}
  fin.close();
  fout.close();
}