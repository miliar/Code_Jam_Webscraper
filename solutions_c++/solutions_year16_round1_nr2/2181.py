#include<iostream>
#include<fstream>
#include<string>

using namespace std; 
void compare (int A[], int n);
int main()
{
cout<<"Enter file name";
string file;
cin>>file;

ifstream infile;
infile.open(file);

int N;

infile>>N;

ofstream out;
out.open("output.txt");
for(int i=0;i<N;i++){

	int n;
	infile>>n;
//	int arr[11][20];

	int A[2500];
for(int o=0;o<2500;o++)
{
	A[o]=0;
}
	for(int j=0;j<(2*n)-1;j++){
		for(int k=0;k<n;k++){
			int no;
			infile>>no;
			//arr[j][k]=no;
			compare(A,no);
		}
	}


	int u[2500]; int l=0; 
	for(int i=0;i<2500;i++){
		if(A[i]!=0){
			//cout<<A[i]<<" ";
			u[l]=A[i];
			l++;
		}
	}

	/*for(int q=0;q<l;q++)
		cout<<u[q]<<endl;*/
	
	int c,d,swap;

	for (c = 0 ; c < ( l - 1 ); c++)
  	{
    	for (d = 0 ; d < l - c - 1; d++)
    		{
      		if (u[d] > u[d+1]) /* For decreasing order use < */
      			{
        		swap       = u[d];
        		u[d]   = u[d+1];
        		u[d+1] = swap;
      			}
    		}
  }

/*for(int q=0;q<l;q++)
		cout<<u[q]<<endl; */
	out<<"Case #"<<i+1<<": ";
	for(int y=0;y<l;y++)
  		out<<u[y]<<" ";
  	out<<endl;

}

}

void compare (int A[], int n){
	int c=1;
	int i;
	for(i=0;i<2500;i++)
		if(A[i]==n)
			{
				A[i]=0;
				c=0;
				break;
			}
	if(c)
	{
		for(i=0;i<2500;i++)
		{
			if(A[i]==0)
				{A[i]=n; break;}
		}
		
	}

}