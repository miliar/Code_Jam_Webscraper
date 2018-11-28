#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
	int t;
	in>>t;
	for(int i = 0;i<t;i++)
	{long n,temp,n_copy;
	int ar[10]={0};
	in>>n;
	n_copy=n;
	begin : temp = n;
	if(temp==0)
	{out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
	continue;}
	else while(temp)
	{
	  int digit;
	  digit = temp%10;
	  switch(digit)
	  {
		  case 1 : ar[1]++; break;
		  case 2 : ar[2]++; break;
		  case 3 : ar[3]++; break;
		  case 4 : ar[4]++; break;
		  case 5 : ar[5]++; break;
		  case 6 : ar[6]++; break;
		  case 7 : ar[7]++; break;
		  case 8 : ar[8]++; break;
		  case 9 : ar[9]++; break;
		  case 0 : ar[0]++; break;
	  }
	  temp = temp/10;

		}
		if(ar[1]==0||ar[2]==0||ar[3]==0||ar[4]==0||ar[5]==0||ar[6]==0||ar[7]==0||ar[8]==0||ar[9]==0||ar[0]==0)
		{
			n = n + n_copy;
			goto begin;
		}
		else out<<"Case #"<<i+1<<": "<<n<<endl;
	}
	in.close();
	out.close();
	return 0;
}
