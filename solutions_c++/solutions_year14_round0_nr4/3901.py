#include<iostream>
#include<fstream>

using namespace std;

bool higherAvailable(double *ken,int size,double sam,bool *tar1)
{
	for(int a=0;a<size;a++){
		if(tar1[a]){
			if(ken[a]>sam)
				return true;}
	}
	return false;
}

double smallest(double *ken,int size,bool *tar1)
{
	float smallest=7;int ind;
	for(int a=0;a<size;a++){
		if(tar1[a]){
			if(smallest>ken[a]){
				smallest=ken[a];ind=a;}}
	}
	tar1[ind]=false;
	return smallest;
}


void smallestHigher(double *ken,int size,double sam,bool *tar1)
{
	double higher=7;int ind;
	for(int a=0;a<size;a++){
		if(tar1[a]){
			if(ken[a]>sam){
				if(ken[a]<higher){
					higher=ken[a];ind=a;}}}}
	tar1[ind]=false;
}
int main()
{
	ifstream ifile;
	ifile.open("D-large.in");

	ofstream ofile;
	ofile.open("output.txt");
	int cases,blocks,war,dwar;
	double *arr1,*arr2;
	bool *tar1,*tar2;
	ifile>>cases;
	for(int z=0;z<cases;z++)
	{
		war=dwar=0;
		ifile>>blocks;
		arr1=new double [blocks];
		arr2=new double [blocks];
		tar1=new bool [blocks];
		tar2=new bool [blocks];
		for(int a=0;a<blocks;a++)
			ifile>>arr1[a];
		for(int a=0;a<blocks;a++)
			ifile>>arr2[a];
		for(int a=0;a<blocks;a++)
			tar1[a]=tar2[a]=true;
		for(int a=0;a<blocks;a++){
			if(!higherAvailable(arr2,blocks,arr1[a],tar2))
			{
				smallest(arr2,blocks,tar2);
				war++;
			}
			else
			{
				smallestHigher(arr2,blocks,arr1[a],tar2);
			}
		}
		for(int a=0;a<blocks;a++){
			if(!higherAvailable(arr1,blocks,arr2[a],tar1))
			{
				smallest(arr1,blocks,tar1);
			}
			else
			{
				smallestHigher(arr1,blocks,arr2[a],tar1);
				dwar++;
			}
		}
		ofile<<"Case #"<<z+1<<": "<<dwar<<" "<<war<<endl;

		delete [] arr1;
		delete [] arr2;
		delete [] tar1;
		delete [] tar2;
	}
	ifile.close();
	ofile.close();

	return 0;
}