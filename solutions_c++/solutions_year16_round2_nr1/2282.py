#include<iostream>
#include<vector>
#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fout.open("answers.txt");
    fin.open("a.txt");
	int i, t, a[10], z, c[26];
	string s;
	fin>>t;
	fin.ignore();
	for(z=1;z<=t;z++)
	{
		for(i=0;i<26;i++)
			c[i]=0;
		for(i=0;i<10;i++)
			a[i]=0;
	    fout<<"Case #"<<z<<": ";
		getline( fin, s );
		for(i=0;i<s.length();i++) {
			c[s[i]-65]++;
			if(s[i]=='Z')
				a[0]++;
			if(s[i]=='W')
				a[2]++;
			if(s[i]=='U')
				a[4]++;	
			if(s[i]=='X')
				a[6]++;
			if(s[i]=='G')
				a[8]++;
		}
		for(i=0;i<a[0];i++) {
			c[25]--;
			c[4]--;
			c[17]--;
			c[14]--;
		}
		for(i=0;i<a[2];i++) {
			c[19]--;
			c[22]--;
			c[14]--;
		}
		for(i=0;i<a[4];i++) {
			c[5]--;
			c[14]--;
			c[20]--;
			c[17]--;
		}for(i=0;i<a[6];i++) {
			c[18]--;
			c[8]--;
			c[23]--;
		}
		for(i=0;i<a[8];i++) {
			c[4]--;
			c[8]--;
			c[6]--;
			c[7]--;
			c[19]--;
		}
		a[1]=c[14];
		c[14]=0;
		for(i=0;i<a[1];i++) {
			c[13]--;
			c[4]--;
		}
		a[3]=c[17];
		c[17]=0;
		for(i=0;i<a[3];i++) {
			c[19]--;
			c[7]--;
			c[4]--;
			c[4]--;
		}
		a[5]=c[5];
		c[5]=0;
		for(i=0;i<a[5];i++) {
			c[8]--;
			c[21]--;
			c[4]--;
		}
		a[7]=c[18];
		c[18]=0;
		for(i=0;i<a[7];i++) {
			c[4]--;
			c[21]--;
			c[4]--;
			c[13]--;
		}
		a[9]=c[13]/2;
		c[13]=0;		
		int j;
		for(i=0;i<10;i++) {
			for(j=0;j<a[i];j++)
				fout<<i;
		}
        fout<<endl;
	}
    fin.close();
	fout.close();
	return 0;
	
}
