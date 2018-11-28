#include<fstream.h>
int main(){
	int i, t[10][10], a[4], n, c, nr,x,j,h;
	ifstream f("input.in");
	ofstream g("output.out");
	f>>n;
	for(x=1; x<=n; x++)
	{nr=0; c=0; h=0;
		f>>c;	
	for(j=1; j<=4; j++)
		for(i=1; i<=4; i++)
			f>>t[j][i];
		for(i=1; i<=4; i++)
			a[i]=t[c][i];
	f>>c;
		for(j=1; j<=4; j++)
		for(i=1; i<=4; i++)
			f>>t[j][i];
		
		for(i=1; i<=4; i++)
			for(j=1; j<=4; j++)
			if(a[i]==t[c][j])
				{nr++; h=a[i];}
			g<<"Case #"<<x<<": ";
			if(nr==0)
				g<<"Volunteer cheated!"<<"\n";
			else if(nr>1)
				g<<"Bad magician!"<<"\n";
			else if(nr==1) {
		        g<<h<<"\n"; }
	}
	f.close();
	g.close();
	return 0;}
		
		