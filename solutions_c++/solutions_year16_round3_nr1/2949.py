#include<iostream>
#include<vector>
#include<fstream>
#include<bits/stdc++.h>
#include<conio.h>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fout.open("answers.txt");
    fin.open("a.txt");
	vector <int> a;
	int i, t, z, j, n, x, flag, min, max;
	fin>>t;
	for(z=1;z<=t;z++)
	{
		fin>>n;
		flag=0;
        for(i=0;i<n;i++) {
        	fin>>x;
        	a.push_back(x);
		}
		fout<<"Case #"<<z<<": ";
		min=*min_element(a.begin(), a.end());
		while(flag==0) {
			flag=1;
			for(i=0;i<n;i++) {
				if(a[i]!=min) {
					flag=0;
					break;	
				}
			}
			if(flag!=1) {
				fout<<char((max_element(a.begin(), a.end())-a.begin())+65)<<" ";
				a[(max_element(a.begin(), a.end())-a.begin())]--;
				for(i=0;i<n;i++)
					cout<<a[i]<<" ";
				cout<<endl;
			}
			else {
				if(n%2!=0) {
					if(min%2==0) {
						for(i=0;i<min-1;i++)
							fout<<char(n+64)<<char(n+64)<<" ";
						for(i=0;i<n/2;i++) {
							for(j=0;j<min;j++)
								fout<<char(2*i+65)<<char(2*i+66)<<" ";
						}	
					}
					else {
						fout<<char(n+64)<<" ";
						for(i=0;i<min-2;i++)
							fout<<char(n+64)<<char(n+64)<<" ";
						for(i=0;i<n/2;i++) {
							for(j=0;j<min;j++)
								fout<<char(2*i+65)<<char(2*i+66)<<" ";
						}
					}
					
					
					
				}
				else
					for(i=0;i<n/2;i++) {
						for(j=0;j<min;j++)
							fout<<char(2*i+65)<<char(2*i+66)<<" ";
					}
			}
		}
		fout<<endl;
		a.clear();
    }
    fin.close();
	fout.close();
	return 0;
}
