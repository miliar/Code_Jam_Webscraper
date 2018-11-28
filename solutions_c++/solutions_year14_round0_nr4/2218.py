#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>

using namespace std;

bool cmpfn (int i,int j) { return (i>j); }

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open ("input.txt");
	fout.open ("output.txt");
	int t=0;
	fin>>t;
	for (int i=0; i<t; i++)
	{
		int n=0;
		fin>>n;
		float naomi[1002];
		float ken[1002];
		float kend[1002];
		for(int k=0;k<n;k++){
			fin>>naomi[k];}
		for(int k=0;k<n;k++){
			fin>>ken[k]; kend[k]=ken[k]; }
		
		sort(naomi,naomi+n,cmpfn);
		sort(ken,ken+n);

		int y=0, z=n;
		//war
		for (int k=0;k<n;k++){
			for(int h=0;h<n;h++){
				if(ken[h]>naomi[k])
				{
					z--;
					ken[h]=0;
					break;
				}
			}
		}
		//Dwar
		
		sort(naomi,naomi+n);
		sort(kend,kend+n,cmpfn);

		for (int k=0;k<n;k++){
			for(int h=0;h<n;h++){
				if(naomi[k]>kend[h])
				{
					y++;
					kend[h]=2;
					break;
				}
			}
		}



		fout<<"Case #"<<i+1<<": "<<y<<" "<<z<<endl;
	}
	fin.close();
	fout.close();
}



//int main()
//{
//	ifstream fin;
//	ofstream fout;
//	fin.open ("input.txt");
//	fout.open ("output.txt");
//	int test=0;
//	fin>>test;
//	for (int i=0;i<test; i++){
//		double c=0, f=0, x=0, tc=0, tx=1, t=0, h=0;
//		fin>>c>>f>>x;
//		while (tx>tc)
//		{
//			tx=t+(x/(2+h*f));
//			tc=t+(c/(2+h*f))+(x/(2+((h+1)*f)));;
//			t=t+(c/(2+h*f));
//			h++;
//		}
//		 fout << std::fixed << std::setprecision(7)<<"Case #"<<i+1<<": "<<tx<<endl;	
//	}
//	fin.close();
//	fout.close();
//}



//int main()
//{
//	ifstream fin;
//	ofstream fout;
//	fin.open ("input.txt");
//	fout.open ("output.txt");
//	int t=0;
//	fin>>t;
//	for (int i=0;i<t ; i ++)
//	{
//		int q1=0, q2=0;
//		fin>>q1;
//		int arr[4][4];
//		int tarr1[4];
//		for(int h=0;h<4;h++)
//		{
//			for(int k=0;k<4;k++) {
//				fin>>arr[h][k];
//				if (h==q1-1)
//					tarr1[k]=arr[h][k]; }
//		}
//
//		fin>>q2;
//
//		int tarr2[4];
//		for(int h=0;h<4;h++)
//		{
//			for(int k=0;k<4;k++) {
//				fin>>arr[h][k];
//				if (h==q2-1)
//					tarr2[k]=arr[h][k]; }
//		}
//		int count =0, index=0;
//		for (int l=0;l<4;l++)
//		{
//			for (int k=0;k<4;k++)
//			if(tarr1[l]==tarr2[k]){
//				count++;  index=tarr1[l]; }
//		}
//		if(count==0)
//			fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
//		else if (count==1)
//			fout<<"Case #"<<i+1<<": "<<index<<endl;
//		else 
//			fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
//
//	}
//	fin.close();
//	fout.close();
//}
