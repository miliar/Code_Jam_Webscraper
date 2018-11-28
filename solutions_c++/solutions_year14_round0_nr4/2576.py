#include "math.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <conio.h>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;



int main()
{
	
	int a=0,i=0;
	ifstream in("Input.txt");	
    if (!in) {
    cout << "Cannot open file.\n";
    return 0;
     }
	freopen("Output.txt", "w", stdout);
    in>>a;
	
	for(i=1;i<=a;i++)
	{
		int k=0,j=0,z=0,y=0,r=0,m=0;
		
		in>>k;
		
		vector<double> s1(k, 0), s2(k, 0), d(k, 0);
		for(j=0;j<k;j++)
			in>>s1[j];
		for(j=0;j<k;j++)
			in>>s2[j];

		sort(s1.begin(), s1.end());
		sort(s2.begin(), s2.end());

		//for(j=0;j<k;j++)
			//d[j]=s1[j]-s2[j];
		//for(r=0;r<k;r++)
		 for(j=k-1;j>=0;j--)
		 {
			if(s1[j]>s2[k-1-r]){z=z+1;}
			else {r=r+1;}
		 }

		for(j=0;j<k;j++)
			if(s1[j]<s2[j-y])
				y=y+1;
			else m=m+1;

		printf("Case #%d: %d %d\n",i,k-y,z);
	}
	fclose (stdout);
	in.close();

 return 0;
}