#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int r,c;
vector<vector<char> > m;

int comprueba(int posx,int posy)
{
	int dirx,diry;
	int posxant = posx;
	int posyant = posy;
	switch(m[posx][posy])
	{
		case '^':
			dirx=-1;
			diry=0;
			break;
		case 'v':
			dirx=1;
			diry=0;
			break;
		case '<':
			dirx=0;
			diry=-1;
			break;
		case '>':
			dirx=0;
			diry=1;
			break;
	}
	//primero comprobamos si se puede
	posx+=dirx;
	posy+=diry;
	while(true)
	{
		if(posx<=0 || posy<=0 || posx>r || posy>c)
			break;
		if(m[posx][posy]!='.')
			return 0;
		posx+=dirx;
		posy+=diry;
	}
	for(int ii=0;ii<4;ii++)
	{
		switch(ii)
		{
			case 0:
				dirx=-1;
				diry=0;
				break;
			case 1:
				dirx=1;
				diry=0;
				break;
			case 2:
				dirx=0;
				diry=-1;
				break;
			case 3:
				dirx=0;
				diry=1;
				break;
		}
		posx = posxant;
		posy = posyant;
		posx+=dirx;
		posy+=diry;
		while(true)
		{
			if(posx<=0 || posy<=0 || posx>r || posy>c)
				break;
			if(m[posx][posy]!='.')
				return 1;
			posx+=dirx;
			posy+=diry;
		}
	}
	return -1;
}

int main()
{
	int T;
	cin >> T;
	for(int I=0;I<T;I++)
	{
		cin >> r >> c;
		m = vector<vector<char> > (r+2,vector<char>(c+2,'.'));
		for(int i=1;i<=r;i++)
		{
			for(int j=1;j<=c;j++)
				cin >> m[i][j];
		}
		bool basaur = true;
		int res = 0;
		for(int i=1;i<=r && basaur;i++)
		{
			for(int j=1;j<=c && basaur;j++)
			{
				if(m[i][j]=='.')
					continue;
				int asdf = comprueba(i,j);
				if(asdf<0)
					basaur = false;
				if(asdf>0)
					res++;
			}
		}
		cout << "Case #" << I+1 << ": ";
		if(!basaur)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
}
