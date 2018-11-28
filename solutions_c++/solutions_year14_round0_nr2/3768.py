#include<iostream.h>
#include<fstream.h>
#include<math.h>

ifstream fin("a.txt");
ofstream fout("ans.txt");


void main(){
	int total,k=1;
	double C,F,X,div=2,var=0;
	int j;
	double t0,t1,t2;
	fin>>total;
	while(k<=total){
		div=2;
		fin>>C;
		fin>>F;
		fin>>X;
		t0=0.0;
		t1=X/2;
		t0=t0+(C/div);
		t2=t0+X/(div+F);
		var=t1;
		
		while(t2<t1){
			div=div+F;
			var=t2;
			t1=t2;
			t0=t0+(C/(div));
			t2=t0+X/(div+F);
		}
		fout<<"Case #"<<k<<": "<<var<<"\n";
		k++;
	}
}

