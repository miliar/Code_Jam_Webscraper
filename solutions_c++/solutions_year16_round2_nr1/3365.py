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
	for(int ctr= 0; ctr<t;ctr++)
	{ out<<"Case #"<<ctr+1<<": ";
		string st;
		in>>st;
		int ar[10];
		int z,w,u,x,g,h,f,s,i,o;
		z = 0;
		w = 0;
		u = 0;
		x = 0;
		g = 0;
		h = 0;
		f = 0;
		s = 0;
		i = 0;
		o = 0;
		int length = st.length();
		for (int j = 0; j < length ;j++ )
		{
				switch(st[j])
				{
					case 'Z' :  z++;
								break;
					case 'W' : 	w++;
								break;
					case 'U' :   u++;
								break;			
					case 'X' :  x++;
								break;
					case 'G' : g++;
								break;
					case 'H' : h++;
								break;
					case 'F' : f++;
								break;			
					case 'S' : s++;
								break;
					case 'I' : i++;
								break;
					case 'O' : o++;
								break;




				}
		}
		ar[0] = z ;
		ar[2] = w ;
		ar[4] = u ;
		ar[6] = x ;
		ar[8] = g ;
		ar[3] = h - g;
		ar[5] = f - u;
		ar[7] = s - x;
		ar[9] = i - (f - u  + x + g);
		ar[1] = o - (z + w + u);

		for(int k = 0; k < 10 ; k ++ )
		{
			
			if(ar[k]>0)
				{
					int temp = ar[k];
					while(temp)
					{
						out<<k;
						--temp;

					}
				} 
		}
		out<<endl;
	}

in.close();
out.close();
return 0;

}
