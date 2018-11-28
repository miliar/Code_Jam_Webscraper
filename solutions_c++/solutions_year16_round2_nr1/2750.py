#include<iostream>
#include<vector>
#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
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

		c[25]=c[25]-a[0];
		c[4]=c[4]-a[0]-a[8];
		c[17]=c[17]-a[0]-a[4];
		c[14]=c[14]-a[0]-a[2]-a[4];
		c[19]=c[19]-a[2]-a[8];
		c[22]=c[22]-a[2];
		c[5]=c[5]-a[4];
		c[20]=c[20]-a[4];
		c[18]=c[18]-a[6];
		c[8]=c[8]-a[6]-a[8];
		c[23]=c[23]-a[6];
		c[6]=c[6]-a[8];
		c[7]=c[7]-a[8];

    	a[1]=c[14];
		c[14]=0;
        c[13]-=a[1];
        c[4]-=a[1];
    cout<<a[1];
		a[3]=c[17];
		c[17]=0;
		c[19]-=a[3];
		c[7]-=a[3];
		c[4]-=a[3];
		c[4]-=a[3];

		a[5]=c[5];
		c[5]=0;
		c[8]-=a[5];
		c[21]-=a[5];
		c[4]-=a[5];

		a[7]=c[18];
		c[18]=0;
        c[4]-=a[7];
        c[21]-=a[7];
        c[4]-=a[7];
        c[13]-=a[7];

		a[9]=c[13]/2;

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
