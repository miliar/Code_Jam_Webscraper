#include<iostream.h>
#include<sstream>
#include<string.h>
#include<stdlib.h>
#include<fstream.h>
using namespace std;
main()
{
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	int a[2][4];
	int cases;
	in>>cases;
	string s;
	for(int i=0;i<cases;i++)
	{for(int e=0;e<2;e++){
		cout<<"aa\n";
		int nor;
		in>>nor;
		getline(in,s);
		for(int ls=0;ls<nor-1;ls++)
			getline(in,s);
		for(int z=0;z<4;z++)
		{
			in>>a[e][z];
		}
		getline(in,s);
		for(int zu=0;zu<4-nor;zu++)
		getline(in,s);
		
	}
	int c=0,pu;
	int arr[4]={0};
	for(int l=0;l<4;l++){
		for(int q=0;q<4;q++)
		if(a[0][l]==a[1][q]){
			arr[l]++;
			pu=l;
		}
	}
	for(int kl=0;kl<4;kl++){
	if(arr[kl]>0)
	c++;}
	if(c==0)
	{
        out<<"Case #"<<i+1<<": Volunteer cheated!\n";
	}else
	if(c==1)
	out<<"Case #"<<i+1<<": "<<a[0][pu]<<endl;
	else
	  out<<"Case #"<<i+1<<": Bad magician!\n";
	
	}
	
}