#include<iostream>
#include<fstream>
using namespace std;
bool higherAvailable(double *arr1,int blocks,double sam,bool *tar1);
double smallest(double *arr1,int blocks,bool *tar1);
void smallestHigher(double *arr1,int blocks,double sam,bool *tar1);
int main(){
	ifstream ifile;ofstream ofile;ifile.open("war.in");ofile.open("war.txt");
	int cases,blocks,war,dwar;
	double *arr1,*arr2;
	bool *tar1,*tar2;
	ifile>>cases;
	for(int z=0;z<cases;z++){
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
	}
	return 0;
}

bool higherAvailable(double *arr1,int blocks,double sam,bool *tar1)
{
	for(int a=0;a<blocks;a++){
		if(tar1[a]){
			if(arr1[a]>sam)
				return true;}
	}
	return false;
}

double smallest(double *arr1,int blocks,bool *tar1)
{
	float smallest=7;int ind;
	for(int a=0;a<blocks;a++){
		if(tar1[a]){
			if(smallest>arr1[a]){
				smallest=arr1[a];ind=a;}}
	}
	tar1[ind]=false;
	return smallest;
}


void smallestHigher(double *arr1,int blocks,double sam,bool *tar1)
{
	double higher=7;int ind;
	for(int a=0;a<blocks;a++){
		if(tar1[a]){
			if(arr1[a]>sam){
				if(arr1[a]<higher){
					higher=arr1[a];ind=a;}}}}
	tar1[ind]=false;
}