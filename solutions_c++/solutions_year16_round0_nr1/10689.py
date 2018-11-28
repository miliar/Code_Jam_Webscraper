#include<bits/stdc++.h>
#include<fstream>
using namespace std;

typedef long long ll;

int main()
{
	int t;
	//fstream filein;
	//fstream fileout;
	//filein.open("A-small-attempt1.in", ios::in);
	//fileout.open("A-small-attempt1.out", ios::out);
	ifstream infile("A-large.in");
	ofstream outfile("out");
	infile >> t;
	for(int b = 0; b < t; b++)
	{
	  int ans = 2;
	  ll n;
	  infile >> n;
	  ll h = n, p = n, arr[10] = {0};
	  if(n == 0)
	  {
	    outfile<<"Case #"<<b+1<<": INSOMNIA\n";
	    continue;
	  }
	  while(ans != 0)
	  {
	    int count = 0;
	    while(h != 0)
	    {
		int dig = h % 10;
		h /= 10;
		arr[dig] = 1;
	    }
	    for(int a = 0, flag = 1; a < 10 && flag != 0; a++)
	    {
	      if(arr[a] == 1)
	        count++;
	      else
	        flag = 0;
	    }
	    if(count == 10)
	    {
		outfile <<"Case #"<<b+1<<": "<< p<<"\n";
		ans = 0;
	    }
	    else
	    {
		p = n * ans;
		ans++;
		h = p;
	    }
	  }
	}
	infile.close();
	outfile.close();
	return 0;
}
