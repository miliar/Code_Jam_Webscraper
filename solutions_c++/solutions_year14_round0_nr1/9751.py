#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){

	int x,y,z,a,b,d,y2,zz;
	int c[100][100],c2[100][100];
	int result[100];
	int found[100][1];
	int i,ii,iii;
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\George\\Downloads\\A-small-attempt0.in");
	fout.open("C:\\Users\\George\\Downloads\\outr.txt");
	int count;
	fin >> x ;

	for(a=0;a<x;a++)
	{
		 count=0;
		fin >> y;
		y=y-1;
		
		for(i=0;i<4;i++)
		{
			for(ii=0;ii<4;ii++)
				fin >> c[i][ii];
		}
		fin >> y2;
		
		y2=y2-1;
		for(i=0;i<4;i++)
		{
			for(ii=0;ii<4;ii++)
				{
					fin >> c2[i][ii];
					if(i==y2)
					{
						for(zz=0;zz<4;zz++){
						if(c2[i][ii]==c[y][zz])
						{
							count++;
							found[a][0]=1;
							result[a]=c[y][zz];
							
							
						}

						}
						if(count >1){found[a][0]=2;}
					}
				}
			if(count ==0)
				found[a][0]==0;
		}
		//result=0;
	}
	for(a=0;a<x;a++){
	fout << "Case #"<<a+1<<": " ;
	if(found[a][0]==1)
		{
		fout	<<result[a]<<endl;
	}
	else if(found[a][0]==2)
		{
		fout	<< "Bad magician!"<<endl;
	}
	else
		{
		fout	<< "Volunteer cheated!"<<endl;
	}


	
	//fout << "Case #" << a+1 << ": " << result[a][1]+1<<" "<< result[a][0]+1<<endl;
	
	}

	return 0;
}