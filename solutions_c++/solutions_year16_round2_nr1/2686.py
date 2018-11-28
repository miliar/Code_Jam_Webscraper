#include<iostream>
#include<fstream>
#include<string>

using namespace std; 

int main()
{
cout<<"Enter file name";
string file;
cin>>file;

ifstream infile;
infile.open(file);

int N;

infile>>N;
cout<<N;
ofstream out;
out.open("output.txt");
for(int k=0;k<N;k++){
	int num[3000];
	int j=0;


	char A[3000];
	infile>>A;
	int alpha[26];
int i;
	for (i=0;A[i]!='\0';i++){
		alpha[(int)A[i]-65]++;
	}

	for(i=0;i<alpha[(int)'Z'-65];i++){
		num[j]=0;
		j++;
		alpha[(int)'E'-65]--;
		alpha[(int)'R'-65]--;
		alpha[(int)'O'-65]--;
	}
	alpha[(int)'Z'-65]=0;

	for(i=0;i<alpha[(int)'W'-65];i++){
		num[j]=2;
		j++;
		alpha[(int)'T'-65]--;
		alpha[(int)'O'-65]--;
	}
	alpha[(int)'W'-65]=0;

	for(i=0;i<alpha[(int)'U'-65];i++){
		num[j]=4;
		j++;
		alpha[(int)'F'-65]--;
		alpha[(int)'O'-65]--;
		alpha[(int)'R'-65]--;
	}
	alpha[(int)'U'-65]=0;

	for(i=0;i<alpha[(int)'X'-65];i++){
		num[j]=6;
		j++;
		alpha[(int)'S'-65]--;
		alpha[(int)'I'-65]--;
	}
	alpha[(int)'X'-65]=0;

	for(i=0;i<alpha[(int)'G'-65];i++){
		num[j]=8;
		j++;
		alpha[(int)'E'-65]--;
		alpha[(int)'I'-65]--;
		alpha[(int)'H'-65]--;
		alpha[(int)'T'-65]--;
	}
	alpha[(int)'G'-65]=0;

	for(i=0;i<alpha[(int)'O'-65];i++){
		num[j]=1;
		j++;
		alpha[(int)'N'-65]--;
		alpha[(int)'E'-65]--;
	}
	alpha[(int)'O'-65]=0;

	for(i=0;i<alpha[(int)'F'-65];i++){
		num[j]=5;
		j++;
		alpha[(int)'I'-65]--;
		alpha[(int)'V'-65]--;
		alpha[(int)'E'-65]--;
	}
	alpha[(int)'F'-65]=0;

	for(i=0;i<alpha[(int)'V'-65];i++){
		num[j]=7;
		j++;
		alpha[(int)'S'-65]--;
		alpha[(int)'E'-65]--;
		alpha[(int)'E'-65]--;
		alpha[(int)'N'-65]--;
	}
	alpha[(int)'V'-65]=0;

	for(i=0;i<alpha[(int)'I'-65];i++){
		num[j]=9;
		j++;
		alpha[(int)'N'-65]--;
		alpha[(int)'E'-65]--;
		alpha[(int)'N'-65]--;
	}
	alpha[(int)'I'-65]=0;

	for(i=0;i<alpha[(int)'T'-65];i++){
		num[j]=3;
		j++;
		alpha[(int)'H'-65]--;
		alpha[(int)'E'-65]--;
		alpha[(int)'E'-65]--;
		alpha[(int)'R'-65]--;
	}
	alpha[(int)'T'-65]=0;
int c,d,swap;
for (c = 0 ; c < ( j - 1 ); c++)
  {
    for (d = 0 ; d < j - c - 1; d++)
    {
      if (num[d] > num[d+1]) /* For decreasing order use < */
      {
        swap       = num[d];
        num[d]   = num[d+1];
        num[d+1] = swap;
      }
    }
  }
 

	out<<"Case #"<<k+1<<": ";
	for(int i=0;i<j;i++){
		out<<num[i];
	}
	out<<endl;

}
	

}


